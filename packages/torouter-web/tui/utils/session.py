import web

# The main session class
  
def add_session_to_app(app):

  if web.config.get("_session") is None:
    store = web.session.DiskStore('sessions')
    session = web.session.Session(app, store, initializer={'login': 0, 'privilege': 0})
    web.config._session = session
  else:
    session = web.config._session

def is_logged():
  return web.config._session.login

def check_login(data):
  if (data.user == "test") and (data.password == "test"):
    web.config._session.login = 1
    return 0
  return 1

