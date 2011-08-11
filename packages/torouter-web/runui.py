# tui - Tor web UI
# by Arturo Filasto' <hellais@torproject.org>
#

import web
import config
import tui.controllers

from tui.utils import session
from view import render


# This is the main structure of URLs
urls = (
    '/', 'tui.controllers.main.index',
#    '/config/(tor|router)', 'tui.controllers.main.config',
    '/network', 'tui.controllers.network.main',
    '/network/firewall', 'tui.controllers.network.firewall',
    '/network/wireless', 'tui.controllers.network.wireless',
    '/network/wired', 'tui.controllers.network.wired',
    '/network/status', 'tui.controllers.network.status',
    '/tor', 'tui.controllers.tor.status',
    '/tor/config', 'tui.controllers.tor.config'
    )
#    '/wizard/([0-9a-f]{1,2})?', 'tui.controllers.wizard.step',
#    '/status', 'tui.controllers.status')

if __name__ == "__main__":
  app = web.application(urls, globals())
  # Add session management to the app
  session.add_session_to_app(app)
  app.internalerror = web.debugerror
  app.run()

