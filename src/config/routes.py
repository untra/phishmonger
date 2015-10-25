"""
Routing configuration.
"""

import tornado.web
from handlers.index_handler import IndexHandler
from handlers.target_handler import TargetHandler
from handlers.campaigns_handler import CampaignsHandler
from handlers.phish_handler import PhishHandler

# Tornado pro-tip: regex routing is optimized by putting more frequently
# accessed routes and simpler regexes before other routes.
routes = [
    (r"/", IndexHandler),
    (r"/targets", TargetHandler),
    (r"/targets/((?:[a-f]|[0-9]|\-)+)", TargetHandler),
    (r"/campaigns", CampaignsHandler),
    (r"/phish/((?:[a-f]|[0-9]|\-)+)", PhishHandler)
]
