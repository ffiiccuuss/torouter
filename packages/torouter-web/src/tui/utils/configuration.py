import web
import config

def get(name):
  conf = {}
  # XXX The content of these functions are just
  #     skeletons
  if name == "wireless":
    conf['essid'] = "Torouter"
    conf['encryption'] = "WPA2"
    conf['key'] = "ljdasjkbcuBH12389Ba"   
    return conf
  elif name == "firewall":
    conf['el1'] = "Element 1"
    conf['el2'] = "Element 2"
    conf['el3'] = "Element 3"
    return conf
  elif name == "wired":
    conf['el1'] = "Element 1"
    conf['el2'] = "Element 2"
    conf['el3'] = "Element 3"
    return conf
  elif name == "tor":
    conf['el1'] = "Element 1"
    conf['el2'] = "Element 2"
    conf['el3'] = "Element 3"
    return conf
  
def write(name, data):
  if name == "wireless":
    return True
  elif name == "firewall":
    return True
  elif name == "wired":
    return True
  elif name == "tor":
    return True
  
def get_form(name):
  # Also these are just skeletons
  if name == "wireless":
    c = get(name)
    return web.form.Form(
      web.form.Textbox(name='essid',
        description='Wireless ESSID', value=c['essid']),
      web.form.Dropdown(name='enctype', args=['WPA2', 'WPA', 'WEP (not reccomended)', 'open'],
        description='Wireless encryption scheme', value=c['encryption']),
      web.form.Password(name='key',
        description='key', value=c['key']),
      web.form.Button('save')
    )
  elif name == "firewall":
    c = get(name) 
    return web.form.Form(
      web.form.Textbox(name='el1',
        description='The first element', value=c['el2']),
      web.form.Dropdown(name='el2', args=['WPA2', 'WPA', 'WEP (not reccomended)', 'open'],
        description='The second selement', value=c['el2']),
      web.form.Password(name='el3',
        description='The third element', value=c['el3']),
      web.form.Button('save')
    )
  elif name == "wired":
    c = get(name)
    return web.form.Form(
      web.form.Textbox(name='el1',
        description='The first element', value=c['el2']),
      web.form.Dropdown(name='el2', args=['WPA2', 'WPA', 'WEP (not reccomended)', 'open'],
        description='The second selement', value=c['el2']),
      web.form.Password(name='el3',
        description='The third element', value=c['el3']),
      web.form.Button('save')
    )
  elif name == "tor":
    c = get(name)
    return web.form.Form(
      web.form.Textbox(name='el1',
        description='The first element', value=c['el2']),
      web.form.Dropdown(name='el2', args=['WPA2', 'WPA', 'WEP (not reccomended)', 'open'],
        description='The second selement', value=c['el2']),
      web.form.Password(name='el3',
        description='The third element', value=c['el3']),
      web.form.Button('save')
    )

