import web
from tui import config
from tui import view
from tui.view import render
from tui.utils import session 

"""
The main page for network configuration
"""
class index:
  def GET(self):
    if session.is_logged() > 0:
      return render.base(render.index())
    else:
      return render.base(render.login())

  def POST(self):
    if session.check_login(web.input()) == 0:
      return render.base(render.index())
    else:
      return render.base(render.login())

class logout:
  def GET(self):
    session.logout()
    return render.base(render.logout())

