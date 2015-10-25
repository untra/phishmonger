"""
Routing configuration.
"""

import tornado.web
from handlers.index_handler import IndexHandler
from handlers.target_handler import TargetHandler
from handlers.campaigns_handler import CampaignsHandler
from handlers.phish_handler import PhishHandler
from handlers.webhook_handler import WebhookHandler

# Tornado pro-tip: regex routing is optimized by putting more frequently
# accessed routes and simpler regexes before other routes.
routes = [
    (r"/", IndexHandler),
    (r"/targets", TargetHandler),
    (r"/targets/((?:[a-f]|[0-9]|\-)+)", TargetHandler),
    (r"/campaigns", CampaignsHandler),
    (r"/campaigns/((?:[a-f]|[0-9]|\-)+)", CampaignsHandler),
    (r"/phish", PhishHandler),
    (r"/phish/((?:[a-f]|[0-9]|\-)+)", PhishHandler),
    (r"/webhook", WebhookHandler)
]
