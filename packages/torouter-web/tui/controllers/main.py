import web
import view, config
from view import render

"""
The main page for network configuration
"""
class index:
  def GET(self):
    return render.base(render.index())

  def POST(self):
    return render.base(render.index())

