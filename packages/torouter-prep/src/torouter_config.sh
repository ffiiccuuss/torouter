#!/bin/bash -x

echo "This program will reconfigure your Debian system into a Torouter"
exit 0
echo "This is where we'd take over the entire Torouter system"

# For every file we touch, move it to the temp_dir and then tar it up in the end
temp_dir="`mktemp -d`"
config_dir="/usr/share/doc/torouter-prep/example-configs/"

# Add a user
ADMINUSER="toradmin"
ADMINGROUP="toradmin"

# Install the Tor repo key
gpg --keyserver keys.gnupg.net --recv 886DDD89
gpg --export A3C4F0F979CAA22CDBA8F512EE8CBC9E886DDD89 | apt-key add -

cp /etc/hosts $temp_dir/
# Stomp on the hosts file
cat << EOF > /etc/hosts
127.0.0.1 localhost
EOF

cp /etc/hostname $temp_dir/
# Set us to have a default host name
cp /usr/share/doc/

# We need to prep apt to understand that we want packages from other repos
# We append to the current package list
cat << EOF >> /etc/apt/sources.list
# Tor's debian package repo:
deb http://deb.torproject.org/torproject.org squeeze main
deb http://deb.torproject.org/torproject.org experimental-squeeze main

# Add Debian backports for OpenNTPD, libminiupnpc-dev, libminiupnpc5
# http://packages.debian.org/squeeze-backports/libminiupnpc-dev
deb http://backports.debian.org/debian-backports squeeze-backports main contrib non-free

# Add Debian experimental for libnatpmp0
# http://packages.debian.org/experimental/libnatpmp0
deb http://ftp.debian.org/debian experimental main
deb-src http://ftp.debian.org/debian experimental main

EOF

# We're creating this file to ensure we get updates
cat << 'EOF' > /etc/apt/preferences.d/backports
Package: *
Pin: release a=squeeze-backports
Pin-Priority: 200
EOF

apt-get -y update

# Install some other packages here:
apt-get -y install denyhosts ufw 

# Allow us to set the clock:
apt-get -y -t squeeze-backports install openntpd

# Install Tor and deps:
apt-get -y install tor tor-geoipdb

# To build with natpmp support
apt-get -y -t experimental install libnatpmp0

# To build with miniupnpc support
apt-get -y -t squeeze-backports install libminiupnpc-dev
apt-get -y -t squeeze-backports install libminiupnpc5

# XXX
# We want to apt-get source tor and build it for the 0.2.3.x branch
#

# Install a Tor controller:
apt-get -y install tor-arm

# Install a normal dns cache for eth1
apt-get -y install dnsmasq

##
## Configuration stage of the script
##

# Configure arm
zcat /usr/share/doc/tor-arm/armrc.sample.gz > ~$(ADMINUSER)/.armrc
# XXX This is where we will call torrc-takeover.py when it is packaged

# XXX We should reconfigure /etc/inittab here

# Configure the network
# eth0 is our "internet" interface with a dhcp client
cat << 'EOF' >  /etc/network/interfaces
# The primary network interface
allow-hotplug eth0
iface eth0 inet dhcp

#
# XXX Configure eth1 and ap0 here
#

EOF

# XXX We should configure ufw here
# ufw allow 
# XXX We should configure denyhosts
# XXX We should configure dnsmasq
# XXX We should configure the DHCP server here

cp /etc/tor/torrc $temp_dir/
# configure Tor and stomp on the current Tor config
cat << 'EOF' > /etc/tor/torrc
# Run Tor as a bridge/relay only, not as a client
SocksPort 0

# What port to advertise for incoming Tor connections
ORPort 443

# We're on a flash file system
AvoidDiskWrites 1

# Be a bridge
BridgeRelay 1

# Rate limited
BandwidthRate 50KB

# Don't allow any Tor traffic to exit
Exitpolicy reject *:*

# Allow a controller (tor-arm) on this system to configure Tor:
ControlPort 9051
ControlListenAddress 127.0.0.1:9051
CookieAuthentication 1
EOF

# Remove a bunch of stuff:
apt-get -y remove exim4-base exim4-config exim4-daemon-light dbus 

## Disable ipv6 support
cp /etc/sysctl.d/disableipv6.conf $temp_dir/
echo net.ipv6.conf.all.disable_ipv6=1 > /etc/sysctl.d/disableipv6.conf
cp /etc/sshd_config $temp_dir/
echo "AddressFamily inet" >> /etc/ssh/ssh_config

##
## Restart services here
##

/etc/init.d/ssh restart
/etc/init.d/tor restart

##
## Touch a stamp to show that we're now a Torouter
##

echo "torouter" > /etc/torouter
