#!/usr/bin/env python
# tui - Tor web UI
# by Arturo Filasto' <hellais@torproject.org>
#

import sys, time, os
from daemon import Daemon
import web
from tui import config
import tui.controllers

from tui.utils import session
from tui.view import render

# This is the main structure of URLs
urls = (
   '/', 'tui.controllers.main.index',
# '/config/(tor|router)', 'tui.controllers.main.config',
   '/network', 'tui.controllers.network.main',
   '/network/firewall', 'tui.controllers.network.firewall',
   '/network/wireless', 'tui.controllers.network.wireless',
   '/network/wired', 'tui.controllers.network.wired',
   '/network/status', 'tui.controllers.network.status',
   '/tor', 'tui.controllers.tor.status',
   '/tor/config', 'tui.controllers.tor.torrc',
   '/logout', 'tui.controllers.main.logout'
   )
# '/wizard/([0-9a-f]{1,2})?', 'tui.controllers.wizard.step',
# '/status', 'tui.controllers.status')

app = web.application(urls, globals())
# add session management to the app
session.add_session_to_app(app)
app.internalerror = web.debugerror

class TorWebDaemon(Daemon):
  def run(self):
    app.run()

DEBUG = False
if __name__ == "__main__":
  if DEBUG:
    app.run()
  service = TorWebDaemon(os.path.join(os.getcwd(),'tui.pid'))
  if len(sys.argv) == 2:
    if 'start' == sys.argv[1]:
      sys.argv[1] = '8080'
      service.start()
    elif 'stop' == sys.argv[1]:
      service.stop()
    elif 'restart' == sys.argv[1]:
      service.restart()
    else:
      print "Unknown command"
      sys.exit(2)
    sys.exit(0)
  else:
    print "usage: %s start|stop|restart" % sys.argv[0]
    sys.exit(2)


