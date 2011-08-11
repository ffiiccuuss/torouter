import web
import view, config
from view import render

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
  return """<ul>
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
  def GET(self):
    return render.base(render.main(),menu(0))

  def POST(self):
    return render.base(render.main(),menu(0))

"""
The firewall configuration page
"""
class firewall:
  def GET(self):
    return render.base(render.firewall(),menu(1))

  def POST(self):
    return render.base(render.firewall(),menu(1))

"""
Wireless network configuration page
"""
class wireless:
  def get_current_config(self):
    conf = {'essid' : None, 'encryption' : None, 'key' : None}
    
    # XXX Dummy default config for testing purposes
    #     plugin here the actual code for config retreival
    conf['essid'] = "Torouter"
    conf['encryption'] = "WPA2"
    conf['key'] = "ljdasjkbcuBH12389Ba"
    

    return conf

  def build_form(self):
    c = self.get_current_config()
    ret_form = web.form.Form(
      web.form.Textbox(name='essid', 
        description='Wireless ESSID', value=c['essid']),
      web.form.Dropdown(name='enctype', args=['WPA2', 'WPA', 'WEP (not reccomended)', 'open'],
        description='Wireless encryption scheme', value=c['encryption']),
      web.form.Password(name='key',
        description='key', value=c['key']),
      web.form.Button('save')
    )
    self.form = ret_form
    
    return True
  
  def update_config(self, data):
    return True

  def GET(self):
    if self.build_form():
      return render.base(render.wireless(self.form()),menu(2))

  def POST(self):
    self.update_config(None)
    print web.input()
    return render.base(render.saved(web.input()),menu(2))

"""
Wired network configuration page
"""
class wired:
  def GET(self):
    return render.base(render.wired(),menu(3))

  def POST(self):
    return render.base(render.wired(),menu(3))

"""
General status page, displays a bit more detail than main
"""
class status:
  def GET(self):
    return render.base(render.status(),menu(4))

  def POST(self):
    return render.base(render.status(),menu(4))
 
