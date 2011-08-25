# tui, Tor web UI
# by Arturo Filasto' <hellais@torproject.org>
#

import web, os

cache = False

globals = {}

# Add your own (username, password) pair
authinfo = ("test", "test")

# Network devices
network_devices = ('uap0', 'eth0', 'eth1')

#interfaces_file = os.getcwd() + "/../../torouter-prep/configs/interfaces"
#torrc_file = os.getcwd() + "/../../torouter-prep/configs/torrc"
torrc_file = "/var/tmp/tor-tui/torrc"
interfaces_file = "/var/tmp/tor-tui/interfaces"

