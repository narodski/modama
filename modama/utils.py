from flask import Markup


def make_image(img_url, link_url, alt='Photo'):
    if img_url is not None:
        return Markup('<a href="' + link_url + '" class="thumbnail">' +
                      '<img src="' + img_url + '" alt="' + alt +
                      '" class="img-rounded img-responsive"></a>')
    else:
        return Markup('<a href="' + link_url + '" class="thumbnail">' +
                      '<img src="//:0" alt="' + alt +
                      '" class="img-responsive"></a>')
