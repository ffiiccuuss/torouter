import web
from tui.config import db

def new_config(conf):
  db.insert('router_config', 
            essid=conf['essid'],
            field1=conf['field1'],
            field2=conf['field2']
            )
  

def write_config():
  db.update('router_config', 
            essid=conf['essid'],
            field1=conf['field1'],
            field2=conf['field2']
            )
 

