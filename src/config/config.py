"""
Application configuration.
"""
import os.path
import tornado.web
from tornado.options import define, options
from routes import routes

SETTINGS = {
    'cookie_secret': "8goWPH9uTyO+9e2NzuaW6pbR6WKH1EbmrXIfxttXq00=",
    'xsrf_cookies': False,
    'login_url': '/login',
    'autoreload': True,
    'template_path':'./templates/',
    'static_path':'./static/',
}

define("port", default=8000, help="run on the given port", type=int)

application = tornado.web.Application(handlers=routes, **SETTINGS)
