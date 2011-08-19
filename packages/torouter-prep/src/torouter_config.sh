#!/bin/bash -x

export VERSION="0.1"

echo "This program will now reconfigure your Debian system into a Torouter"

# For every file we touch, move it to the temp_dir and then tar it up in the end
export temp_dir="`mktemp -d`"
export config_dir="/usr/share/torouter-prep/example-configs/"

# Add a user to administrate the Torouter later
export ADMINUSER="torouter"
export ADMINGROUP="torouter"

addgroup $ADMINGROUP
useradd -g $ADMINGROUP -s /bin/bash $ADMINUSER

# Install the Tor repo key
# gpg --keyserver keys.gnupg.net --recv 886DDD89
# gpg --export A3C4F0F979CAA22CDBA8F512EE8CBC9E886DDD89 | apt-key add -
# This is the main Tor repo apt pubkey
apt-key add $config_dir/A3C4F0F979CAA22CDBA8F512EE8CBC9E886DDD89.apt-key

# This is the temp torrouter archive pubkey; this should be updated when we
# freeze this repo and know what we want to do
apt-key add $config_dir/047E6A24.asc

# Set us to have a default host name and hosts file
cp $config_dir/hostname /etc/hostname
cp $config_dir/hosts /etc/hosts

# We need to prep apt to understand that we want packages from other repos
cp $config_dir/sources.list /etc/apt/sources.list

# We're creating this file to ensure we get updates
cp $config_dir/apt-preferences.d-backports /etc/apt/preferences.d/backports
cp $config_dir/apt.conf /etc/apt/apt.conf

apt-get -y update

# Remove a bunch of stuff:
apt-get -y remove exim4-base exim4-config exim4-daemon-light dbus

# Install the weird wireless control for the DreamPlug
apt-get install -y -t sid uaputl

# Install some other packages here:
apt-get -y install denyhosts ufw

# Allow us to set the clock:
apt-get -y -t squeeze-backports install openntpd

# Install Tor and deps:
apt-get -y install tor tor-geoipdb

# To build with natpmp support
apt-get -y -t experimental install libnatpmp-dev
apt-get -y -t experimental install libnatpmp0

# To build with miniupnpc support
apt-get -y -t squeeze-backports install libminiupnpc-dev
apt-get -y -t squeeze-backports install libminiupnpc5

# XXX
# We want to apt-get source tor and build it for the 0.2.3.x branch
#

# Install a Tor controller:
apt-get -y install tor-arm

# Install the ttdnsd program:
apt-get -y install ttdnsd

# Install a normal dns cache for eth1
apt-get -y install dnsmasq

##
## Configuration stage of the script
##

# Configure arm
zcat $config_dir/armrc.sample.gz > ~$ADMINUSER/.armrc

# Reconfigure /etc/inittab here
cp $config_dir/inittab /etc/inittab

# Configure the network
# eth0 is our "internet" interface with a dhcp client
cp $config_dir/interfaces /etc/network/interfaces

# Configure dnsmasq
cp $config_dir/dnsmasq.conf /etc/dnsmasq.conf

# Configure ntp
cp $config_dir/ntp.conf /etc/ntp.conf
cp $config_dir/openntpd-default /etc/default/openntpd

# XXX We should configure ufw here
# XXX We should configure denyhosts

cp $config_dir/torrc /etc/tor/torrc
cp $config_dir/ttdnsd-default /etc/default/ttdnsd

# Configure sshd
cp $config_dir/sshd_config /etc/ssh/sshd_config

# Clean up our cache
apt-get -y clean

## Disable ipv6 support for now
cp $config_dir/modprobe.d-blacklist.conf /etc/modprobe.d/blacklist.conf
echo net.ipv6.conf.all.disable_ipv6=1 > /etc/sysctl.d/disableipv6.conf

##
## Restart services here
##

/etc/init.d/ssh restart
/etc/init.d/tor restart
/etc/init.d/ttdnsd restart

##
## Touch a stamp to show that we're now a Torouter
##

echo "torouter $VERSION" > /etc/torouter
