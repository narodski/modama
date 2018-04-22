from flask_appbuilder.security.views import AuthDBView
from flask_appbuilder.security.forms import LoginForm_db
from flask import flash, redirect, g, request, make_response
import jwt
from flask_appbuilder._compat import as_unicode
from flask_appbuilder.views import expose
from flask_login import login_user
from datetime import datetime, timezone, timedelta


class AuthDBJWTView(AuthDBView):

    @expose('/login/', methods=['GET', 'POST'])
    def login(self):
        config = self.appbuilder.get_app.config
        cookie_secure = config.get('SESSION_COOKIE_SECURE', True)
        expiration = config.get('JWT_EXPIRATION_HOURS', -1)
        base_payload = {}
        if expiration > 0:
            valid_until = datetime.now(timezone.utc) + \
                timedelta(hours=expiration)
            base_payload['exp'] = valid_until
        secret = config.get('JWT_SECRET')
        redir_url = request.args.get('orig_url',
                                     self.appbuilder.get_url_for_index)
        if g.user is not None and g.user.is_authenticated():
            payload = {'user': {'id': g.user.id, 'username': g.user.username}}
            payload.update(base_payload)
            token = jwt.encode(payload, secret, algorithm='HS256')
            resp = make_response(redirect(redir_url))
            resp.set_cookie('modama_jwt', token, expires=valid_until,
                            secure=cookie_secure, httponly=True)
            return resp
        token = request.cookies.get('modama_jwt', False)
        if token:
            try:
                payload = jwt.decode(token, secret, algorithms='HS256')
                userid = payload['user']['id']
                user = self.appbuilder.sm.get_user_by_id(userid)
                login_user(user)
                payload.update(base_payload)
                token = jwt.encode(payload, secret, algorithm='HS256')
                resp = make_response(redirect(redir_url))
                resp.set_cookie('modama_jwt', token, expires=valid_until,
                                secure=cookie_secure, httponly=True)
                return resp
            except jwt.exceptions.InvalidTokenError:
                pass
        form = LoginForm_db()
        if form.validate_on_submit():
            user = self.appbuilder.sm.auth_user_db(form.username.data,
                                                   form.password.data)
            if not user:
                flash(as_unicode(self.invalid_login_message), 'warning')
                return redirect(redir_url)
            login_user(user, remember=False)
            payload = {'user': {'id': user.id, 'username': user.username}}
            payload.update(base_payload)
            token = jwt.encode(payload, secret, algorithm='HS256')
            resp = make_response(redirect(redir_url))
            resp.set_cookie('modama_jwt', token, expires=valid_until,
                            secure=cookie_secure, httponly=True)
            return resp
        return self.render_template(self.login_template,
                                    title=self.title,
                                    form=form,
                                    appbuilder=self.appbuilder)
