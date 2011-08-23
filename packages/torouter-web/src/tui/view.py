import os
import web
from tui import config

t_globals = dict(
  datestr=web.datestr,
    )

# get the path where the script currently resides
current_path = "/".join(os.path.abspath(__file__).split("/")[:-1])
# create the render object
render = web.template.render(current_path+'/views', cache=config.cache,  globals=t_globals)
render._keywords['globals']['render'] = render

