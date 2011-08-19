# These functions are for parsing /etc/network/interface
# files, they will be used inside torouter to visualize
# and edit configuration
import os, re

class interfaces:
  def __init__(self,filename):
    self.filename = filename
    self.fp = open(filename, "r")
    self.wifi = {}
    self.eth1 = {}
    self.eth0 = {}

  def exclude_output(self, iexclude):
    iface = None
    output = ""
    self.fp = open(self.filename, "r")
    for line in self.fp.readlines():
      if line.lstrip().startswith("iface"):
        iface = line.split(" ")[1]
      if iface == iexclude:
        continue
      else:
        output += line
    return output

  def parse_line(self, line, iface):
    name   = line.split(" ")[0]
    values = " ".join(line.split(" ")[1:]).rstrip()
    if iface == "uap0":
      if self.wifi.has_key(name):
        if type(self.wifi[name]) is list:
          self.wifi[name].append(values)
        else:
          self.wifi[name] = [self.wifi[name],values]
      else:
        self.wifi.update({name : values})
    elif iface == "eth1":
      if self.eth1.has_key(name):
        if type(self.eth1[name]) is list:
          self.eth1[name].append(values)
        else:
          self.eth1[name] = [self.eth1[name],values]
      else:
        self.eth1.update({name : values})
    elif iface == "eth0":
      if self.eth0.has_key(name):
        if type(self.eth0[name]) is list:
          self.eth0[name].append(values)
        else:
          self.eth0[name] = [self.eth0[name],values]
      else:
        self.eth0.update({name : values})
  
  def parse(self):
    iface = None
    for line in self.fp.readlines():
      line = line.lstrip()
      if line.startswith("#") or line == "":
        continue
      if line.startswith("iface"):
        iface = line.split(" ")[1]
      if iface:
        self.parse_line(line, iface)

  def html_output(self, data):
    output = "<h3>Interface %s</h3>\n" % data['iface'].split(" ")[0]
    output += "<table class=\"interface\" id=\"%s\">\n" % data['iface'].split(" ")[0]
    
    for item in data.items():
      if item[0] != "iface":
        if type(item[1]) is list:
          for i in item[1]:
            output += "<tr><td>%s</td><td>%s</td></tr>\n" % (item[0], i)
        else:
          output += "<tr><td>%s</td><td>%s</td></tr>\n" % (item[0],item[1])
    output += "</table>"
    print output
    return output 

  def output(self, data):
    output = "iface %s" % data['iface']
    for item in data.items():
      if item[0] != "iface":
        if type(item[1]) is list:
          for i in item[1]:
            output += item[0] + " " + i + "\n"
        else:
          output += item[0] + " " + item[1] + "\n"
    return output

  def set_ssid(self, essid):
    i = 0
    for entry in self.wifi['post-up']:
      if re.search("sys_cfg_ssid", entry):
        print essid
        self.wifi['post-up'][i] = 'post-up /usr/bin/uaputl sys_cfg_ssid "' + essid + '"'
      i += 1

  # XXX currently works for one pre-up entry, must make it work also for arrays
  def set_mac(self, mac):
    self.wifi['pre-up'] = 'ifconfig uap0 hw ether ' + mac
    

class torrc:
  def __init__(self,filename):
    self.fp = open(filename, "r")
    self.parsed = []

  def parse(self):
    for line in self.fp.readlines():
      line = line.lstrip()
      if line.startswith("#") or line == "":
        continue
      else:
        self.parsed.append(line)

  def output(self):
    output = ""
    for line in self.fp.readlines():
      print line
      output += line
    return output

  def html_output(self):
    output = "<ul id=\"torrc\">"
    for line in self.parsed:
      if line != "\n":
        output += "<li><em>%s</em> %s</li>" % (line.split(" ")[0], " ".join(line.split(" ")[1:]))
    output += "</ul>"
    print output
    return output

#interfaces_file = os.getcwd() + "/../../../torouter-prep/configs/interfaces"
#itfc = interfaces(interfaces_file)
#itfc.parse()
#itfc.html_output(itfc.wifi)
#itfc.html_output(itfc.eth1)
#itfc.html_output(itfc.eth0)
  
