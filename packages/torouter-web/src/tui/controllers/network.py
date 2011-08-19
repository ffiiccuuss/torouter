import web
from tui import config
from tui import view
from tui.view import render
from tui.utils import session, configuration, parsing, fileio

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
      return render.base(render.firewall(configuration.get_form("firewall")),menu(1))
    else:
      return render.base(render.login())

  def POST(self):
    if session.is_logged() > 0:
      self.update_config(web.input())
      return render.base(render.firewall(configuration.get_form("firewall")),menu(1))
    else:
      return render.base(render.login())
  


"""
Wireless network configuration page
"""
class wireless:
  # XXX do all the backend stuff
  def update_config(self, data):
    itfc = parsing.interfaces(config.interfaces_file)
    itfc.parse()
    itfc.set_ssid(data.essid)
    itfc.set_mac(data.mac)
    itfc.wifi['netmask'] = data.netmask
    itfc.wifi['address'] = data.address
    filecontent = itfc.exclude_output("uap0") + itfc.output(itfc.wifi)
    files = [('/etc/network/interfaces', filecontent)]
    fileio.write(files)
    #print itfc.output(itfc.wifi)
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
    itfc = parsing.interfaces(config.interfaces_file)
    itfc.parse()
    network = itfc.html_output(itfc.wifi) + itfc.html_output(itfc.eth0) + itfc.html_output(itfc.eth1)
    return render.base(render.status(network),menu(4))

  def POST(self):
    itfc = parsing.interfaces(config.interfaces_file)
    itfc.parse()
    network = itfc.html_output(itfc.wifi) + itfc.html_output(itfc.eth0) + itfc.html_output(itfc.eth1)
    return render.base(render.status(),menu(4))
 
