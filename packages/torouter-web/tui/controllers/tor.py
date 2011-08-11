import web
import view, config
from view import render
from tui.utils import session

"""
The main Tor status page
"""
class status:
  def GET(self):
    return render.base(render.torstatus())

  def POST(self):
    return render.base(render.torstatus())

"""
Tor configuration page
"""
class config:
  def GET(self):
    return render.base(render.torconfig())

  def POST(self):
    return render.base(render.torconfig())

