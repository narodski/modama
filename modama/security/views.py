from flask_appbuilder.security.views import AuthDBView
from flask_appbuilder.security.forms import LoginForm_db
from flask import flash, redirect, g, request, make_response, jsonify
import jwt
from flask_appbuilder._compat import as_unicode
from flask_appbuilder.views import expose
from flask_login import login_user
from datetime import datetime, timezone, timedelta


class AuthDBJWTView(AuthDBView):

    @expose('/login_app', methods=['POST', 'OPTIONS', 'GET'])
    def login_app(self):
        user = self.getUserFromAuthHeader()
        if user is not None:
            login_user(user)
            token = self.encodeJWT(self.getJWT())
            return jsonify({'success': True, 'token': token,
                            'message': 'Login successful'})
        form = LoginForm_db(csrf_enabled=False)
        if form.validate_on_submit():
            user = self.appbuilder.sm.auth_user_db(form.username.data,
                                                   form.password.data)
            if not user:
                return jsonify({'success': False,
                                'message': self.invalid_login_message})
            login_user(user, remember=False)
            token = self.encodeJWT(self.getJWT())
            return jsonify({'success': True, 'token': token,
                            'message': 'Login successful'})
        else:
            message = "\n".join(["{}: {}".format(f, ";".join(e))
                                 for f, e in form.errors.items()])
            return jsonify({'success': False, "message": message})

    def getUserFromAuthHeader(self):
        auth_header = request.headers.get('Authorization')
        user = None
        if auth_header:
            token = auth_header.split(" ")[1]
            try:
                user = self.getUserFromJWT(token)
            except jwt.exceptions.InvalidTokenError:
                pass
        return user

    def getUserFromCookie(self):
        token = request.cookies.get('modama_jwt', None)
        user = None
        if token is not None:
            try:
                user = self.getUserFromJWT(token)
            except jwt.exceptions.InvalidTokenError:
                pass
        return user

    def getUserFromJWT(self, token):
        """
        Get the user object from the userid in the token.
        First decode the token (and validate it).
        Potentially raises a jwt.exceptions.InvalidTokenError
        if the token is invalid.
        """
        config = self.appbuilder.get_app.config
        secret = config.get('JWT_SECRET')
        payload = jwt.decode(token, secret, algorithms='HS256')
        userid = payload['user']['id']
        user = self.appbuilder.sm.get_user_by_id(userid)
        return user

    def encodeJWT(self, token):
        config = self.appbuilder.get_app.config
        secret = config.get('JWT_SECRET')
        if token is not None:
            return jwt.encode(token, secret, algorithm="HS256").decode('UTF-8')

    def getJWT(self):
        config = self.appbuilder.get_app.config
        expiration = config.get('JWT_EXPIRATION_HOURS', -1)
        base_payload = {}
        if expiration > 0:
            valid_until = datetime.now(timezone.utc) + \
                timedelta(hours=expiration)
            base_payload['exp'] = valid_until
        if g.user is not None and g.user.is_authenticated():
            payload = {'user': {'id': g.user.id, 'username': g.user.username}}
            payload.update(base_payload)
            return payload
        return None

    @expose('/login/', methods=['GET', 'POST'])
    def login(self):
        redir_url = request.args.get('orig_url',
                                     self.appbuilder.get_url_for_index)
        config = self.appbuilder.get_app.config
        cookie_secure = config.get('SESSION_COOKIE_SECURE', True)

        # Get the token for the currently logged-in user (if any)
        token = self.getJWT()
        if token is not None:
            valid_until = token.get('exp', None)
            resp = make_response(redirect(redir_url))
            encoded_token = self.encodeJWT(token)
            resp.set_cookie('modama_jwt', encoded_token,
                            expires=valid_until, secure=cookie_secure,
                            httponly=True)
            return resp

        # Not currently logged-in, so check for token in cookie
        user = self.getUserFromCookie()
        if user is not None:
            login_user(user)
            token = self.getJWT()
            valid_until = token.get('exp', None)
            resp = make_response(redirect(redir_url))
            resp.set_cookie('modama_jwt', self.encodeJWT(token),
                            expires=valid_until, secure=cookie_secure,
                            httponly=True)
            return resp

        # No token in cookie, show login form and check username/password
        form = LoginForm_db()
        if form.validate_on_submit():
            user = self.appbuilder.sm.auth_user_db(form.username.data,
                                                   form.password.data)
            if not user:
                flash(as_unicode(self.invalid_login_message), 'warning')
                return redirect(redir_url)
            login_user(user, remember=False)
            token = self.getJWT()
            valid_until = token.get('exp', None)
            resp = make_response(redirect(redir_url))
            resp.set_cookie('modama_jwt', self.encodeJWT(token),
                            expires=valid_until, secure=cookie_secure,
                            httponly=True)
            return resp
        return self.render_template(self.login_template,
                                    title=self.title,
                                    form=form,
                                    appbuilder=self.appbuilder)
