import web 

from web import form
from config import view

class step:
  cur_step = 1
  next_step = 2
  wiztext = []
  wizform = []

  wiztext.append("Tor Configuration")
  wizform.append(form.Form(
          form.Textbox('Nickname',
            form.notnull, description="Relay Nickname"),
          form.Textbox('RelayBandwidthRate',
            form.notnull, description="Relay Bandwidth Rate"),
          form.Textbox('RelayBandwidthBurst',
            form.notnull, description="Relay Bandwidth Burst"),
          form.Textbox('ContactInfo',
            form.notnull, description="Contact Info"),
          form.Textbox('ExitPolicy',
            form.notnull, description="Exit Policy"),
          form.Button('Next Step')
          ))

  wiztext.append("Wireless setup")
  wizform.append(form.Form(
          form.Textbox('essid',
            form.notnull, description="Wireless ESSID"),
          form.Textbox('mac',
            form.notnull, description="MAC address"),
          form.Textbox('whatever',
            form.notnull, description="Wireless ESSID"),
          form.Button('Next Step')
          ))

  wiztext.append("")
  wizform.append(form.Form(
          form.Textbox('essid',
            form.notnull, description="Wireless ESSID"),
          form.Textbox('mac',
            form.notnull, description="MAC address"),
          form.Textbox('whatever',
            form.notnull, description="Wireless ESSID"),
          form.Button('Next Step')
          ))

  wiztext.append("")
  wizform.append(form.Form(
          form.Textbox('essid',
            form.notnull, description="Wireless ESSID"),
          form.Textbox('mac',
            form.notnull, description="MAC address"),
          form.Textbox('whatever',
            form.notnull, description="Wireless ESSID"),
          form.Button('Next Step')
          ))
  
  def GET(self, step):
    if step:
      self.cur_step = int(step)
      self.next_step = int(step) + 1
    else:
      self.cur_step = 1
      self.next_step = 2
    if len(self.wizform) < int(self.cur_step):
      return "Done!"
    return view.wizard(self.wizform[self.cur_step-1], self.wiztext[self.cur_step-1], self.cur_step, self.next_step)

  def POST(self, step):
    x = web.input()
    self.cur_step = int(step)
    self.next_step = int(step) + 1
    if len(self.wizform) < int(self.cur_step):
      return "Done!"
    return view.wizard(self.wizform[self.cur_step-1], self.wiztext[self.cur_step-1], self.cur_step, self.next_step)




