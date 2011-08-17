import web
import view, config
from view import render
from tui.utils import session, parsing

"""
The main Tor status page
"""
class status:
  def GET(self):
    trc = parsing.torrc(config.torrc_file)
    trc.parse()
    output = trc.html_output()
    return render.base(render.torstatus(output,config.torrc_file))

  def POST(self):
    trc = parsing.torrc(config.torrc_file)
    trc.parse()
    output = trc.html_output()
    return render.base(render.torstatus(output,config.torrc_file))

"""
Tor configuration page
"""
class torrc:
  def update_config(self, data):
    return True

  def GET(self):
    return render.base(render.torconfig())

  def POST(self):
    self.update_config(web.input())
    return render.base(render.torconfig())

