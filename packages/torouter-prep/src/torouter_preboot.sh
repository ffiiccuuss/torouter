#!/usr/bin/env dash

echo "Inside torouter_preboot.sh..."

export VERSION="0.2"

export config_dir="/usr/share/torouter-prep/example-configs/"

# Add a user to administrate the Torouter later
export ADMINUSER="torouter"
export ADMINGROUP="torouter"
export TORADMINGROUP="debian-tor"

# TODO: check that dependancies are already installed, or fail
#   tor, torouterui, ttdnsd, etc
# if [ `apt-get --simulate install apt-utils tor torouterui ttdnsd` ]

# Set us to have a default host name and hosts file
install -o root -g root -m 644 $config_dir/etc/hostname /etc/hostname
install -o root -g root -m 644 $config_dir/etc/hosts /etc/hosts

# We need to prep apt to understand that we want packages from other repos
install -o root -g root -m 644 $config_dir/etc/apt/sources.list /etc/apt/sources.list

# Reconfigure /etc/inittab here
install -o root -g root -m 644 $config_dir/etc/inittab /etc/inittab

# Reconfigure fstab
install -o root -g root -m 644 $config_dir/etc/fstab /etc/fstab

# Configure the network
# eth0 is our "internet" interface with a dhcp client
install -o root -g root -m 644 $config_dir/etc/network/interfaces /etc/network/interfaces

# Configure dnsmasq
install -o root -g root -m 644 $config_dir/etc/dnsmasq.conf /etc/dnsmasq.conf
install -o root -g root -m 644 $config_dir/etc/dnsmasq_lan.conf /etc/dnsmasq_lan.conf
install -o root -g root -m 644 $config_dir/etc/dnsmasq_wifi.conf /etc/dnsmasq_wifi.conf

# new dns scheme
install -o root -g root -m 644 $config_dir/etc/default/dnsmasq /etc/default/dnsmasq
install -o root -g root -m 754 $config_dir/etc/init.d/dnsmasq_lan /etc/init.d/dnsmasq_lan
install -o root -g root -m 754 $config_dir/etc/init.d/dnsmasq_wifi /etc/init.d/dnsmasq_wifi

# Configure ntp
install -o root -g root -m 644 $config_dir/etc/ntp.conf /etc/ntp.conf
install -o root -g root -m 644 $config_dir/etc/default/openntpd /etc/default/openntpd

# Configure ssh
install -o root -g root -m 644 $config_dir/etc/ssh/sshd_config /etc/ssh/sshd_config

# XXX We should configure ufw here
# XXX We should configure denyhosts

# torrc permissions get overwritten below
install -o root -g root -m 644 $config_dir/etc/tor/torrc /etc/tor/torrc

install -o root -g root -m 644 $config_dir/etc/default/ttdnsd /etc/default/ttdnsd

# install tor firewall helper
install -o root -g root -m 754 $config_dir/sbin/tor-wireless-firewall.sh /usr/sbin/

# Remove a bunch of stuff
apt-get -f -y remove --purge polipo minissdpd
apt-get -y remove exim4-base exim4-config exim4-daemon-light dbus isc-dhcp-server

# Clean up apt
#apt-get -y autoremove
apt-get install -f
apt-get -y clean

## Disable ipv6 support for now
install -o root -g root -m 644 $config_dir/etc/modprobe.d/blacklist.conf /etc/modprobe.d/blacklist.conf

## add users and groups (ignore failures if groups already exist)
addgroup $ADMINGROUP
useradd -g $ADMINGROUP -G $TORADMINGROUP -s /bin/bash $ADMINUSER
# TODO: $ADMINUSER passwd?

# give Tor permission to modify it's own configuration
chgrp $TORADMINGROUP /etc/tor/ /etc/tor/*
chmod g+rw /etc/tor/ /etc/tor/*

# Configure arm
zcat $config_dir/tmp/armrc.sample.gz > /home/$ADMINUSER/.armrc

## Add arm startup trick with cron for shared screen run as $ADMINUSER
crontab -u $ADMINUSER $config_dir/tmp/tor-arm-crontab

## Touch a stamp to show that we're now a Torouter
echo "torouter $VERSION" > /etc/torouter

