# tui, Tor web UI
# by Arturo Filasto' <hellais@torproject.org>
#

import web, os

cache = False

globals = {}

# Add your own (username, password) pair
authinfo = ("test", "test")

