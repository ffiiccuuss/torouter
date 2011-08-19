import web
import re
from tui.utils import parsing
from tui import config

def get(name):
  conf = {}
  itfc = parsing.interfaces(config.interfaces_file)
  itfc.parse()
 
  if name == "wireless":
    conf['essid'] = "tor"
    conf['mac'] = "00:11:22:33:44:55"
    for entry in itfc.wifi['post-up']:
      if re.search("sys_cfg_ssid", entry):
        conf['essid'] = entry.split(" ")[2].split("\"")[1]
   
    if type(itfc.wifi['pre-up']) is str:
      conf['mac'] = itfc.wifi['pre-up'].split(" ")[4]
    else:
      for entry in itfc.wifi['pre-up']:
        if re.search("ether", entry):
          print "hahah"
          conf['mac'] = entry.split(" ")[4]

    conf['netmask'] = itfc.wifi['netmask']
    conf['address'] = itfc.wifi['address']
    conf['encryption'] = "open"
    conf['key'] = ""
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
        description='ESSID', value=c['essid']),
      web.form.Textbox(name='mac',
        description='MAC address', value=c['mac']),
      web.form.Textbox(name='address',
        description='IP address', value=c['address']),
      web.form.Textbox(name='netmask',
        description='Netmask address', value=c['netmask']),
      web.form.Dropdown(name='enctype', args=['WPA2', 'WPA', 'WEP (not reccomended)', 'open'],
        description='Encryption scheme', value=c['encryption']),
      web.form.Password(name='key',
        description='Key', value=c['key']),
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

