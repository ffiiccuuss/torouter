import web
from tui import config
from tui import view
from tui.view import render
from tui.utils import session, parsing, fileio

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
    # Now it will just write to /tmp/torrc
    files = [('/tmp/torrc',data.torrc)]
    fileio.write(files)

    return True

  def GET(self):
    trc = parsing.torrc(config.torrc_file)
    output = trc.output()
    return render.base(render.torconfig(output))

  def POST(self):
    self.update_config(web.input())
    trc = parsing.torrc(config.torrc_file)
    trc.parse()
    output = trc.html_output()
    return render.base(render.torstatus(output,config.torrc_file))


