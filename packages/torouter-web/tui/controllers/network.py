import web
import view, config
from view import render
from tui.utils import session,configuration

"""
This function is used to generate the network
submenus.
"""
def menu(n):
  a = [] 
  for i in range(0,5):
    if i == n:
      a.append("sel")
    else:
      a.append("")
  print a
  return """<ul id="submenu">
  <li><a href="/network" class="%s">Main</a></li>
  <li><a href="/network/firewall" class="%s">Firewall</a></li>
  <li><a href="/network/wireless" class="%s">Wireless</a></li>
  <li><a href="/network/wired" class="%s">Wired</a></li>
  <li><a href="/network/status" class="%s">Status</a></li>
</ul>
""" % tuple(a)

"""
The main page for network configuration
"""
class main:
  # XXX do all the backend stuff
  def update_config(self, data):
    return True

  def GET(self):
    if session.is_logged() > 0:
      return render.base(render.main(),menu(0))
    else:
      return render.base(render.login())

  def POST(self):
    if session.is_logged() > 0:
      self.update_config(web.input())
      return render.base(render.main(),menu(0))
    else:
      return render.base(render.login())

"""
The firewall configuration page
"""
class firewall:
  # XXX do all the backend stuff 
  def update_config(self, data):
    return True

  def GET(self):
    if session.is_logged() > 0:
      return render.base(render.firewall(configuration.get_form("firewall")),menu(0))
    else:
      return render.base(render.login())

  def POST(self):
    if session.is_logged() > 0:
      self.update_config(web.input())
      return render.base(render.firewall(),menu(1))
    else:
      return render.base(render.login())
  


"""
Wireless network configuration page
"""
class wireless:
  # XXX do all the backend stuff
  def update_config(self, data):
    return True

  def GET(self):
    if session.is_logged() > 0:
      return render.base(render.wireless(configuration.get_form("wireless")),menu(2))
    else:
      return render.base(render.login())

  def POST(self):
    if session.is_logged() > 0:
      self.update_config(web.input())
      print web.input()
      return render.base(render.saved(web.input()),menu(2))
    else:
      return render.base(render.login())

"""
Wired network configuration page
"""
class wired:
  # XXX do all the backend stuff
  def update_config(self, data):
    return True

  def GET(self):
    if session.is_logged() > 0:
      return render.base(render.wired(configuration.get_form("wired")),menu(3))
    else:
      return render.base(render.login())

  def POST(self):
    if session.is_logged() > 0:
      self.update_config(web.input())
      return render.base(render.wired(),menu(3))
    else:
      return render.base(render.login())

"""
General status page, displays a bit more detail than main
"""
class status:
  def GET(self):
    return render.base(render.status(),menu(4))

  def POST(self):
    return render.base(render.status(),menu(4))
 
