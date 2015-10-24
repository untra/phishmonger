"""
Routing configuration.
"""

import tornado.web
from handlers.index_handler import IndexHandler
from handlers.target_handler import TargetHandler

# Tornado pro-tip: regex routing is optimized by putting more frequently
# accessed routes and simpler regexes before other routes.
routes = [
    (r"/", IndexHandler),
    (r"/targets", TargetHandler)
]
