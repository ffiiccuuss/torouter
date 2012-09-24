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
cp $config_dir/etc/hostname /etc/hostname
cp $config_dir/etc/hosts /etc/hosts

# We need to prep apt to understand that we want packages from other repos
cp $config_dir/etc/apt/sources.list /etc/apt/sources.list

# Reconfigure /etc/inittab here
cp $config_dir/etc/inittab /etc/inittab

# Reconfigure fstab
cp $config_dir/etc/fstab /etc/fstab

# Configure the network
# eth0 is our "internet" interface with a dhcp client
cp $config_dir/etc/network/interfaces /etc/network/interfaces

# Configure dnsmasq
cp $config_dir/etc/dnsmasq.conf /etc/dnsmasq.conf

# Configure ntp
cp $config_dir/etc/ntp.conf /etc/ntp.conf
cp $config_dir/etc/default/openntpd /etc/default/openntpd

# Configure ssh
cp $config_dir/etc/ssh/sshd_config /etc/ssh/sshd_config

# XXX We should configure ufw here
# XXX We should configure denyhosts

cp $config_dir/etc/tor/torrc /etc/tor/torrc
cp $config_dir/etc/default/ttdnsd /etc/default/ttdnsd

# Remove a bunch of stuff
apt-get -f -y remove --purge polipo minissdpd
apt-get -y remove exim4-base exim4-config exim4-daemon-light dbus

# Clean up apt
#apt-get -y autoremove
apt-get install -f
apt-get -y clean

## Disable ipv6 support for now
cp $config_dir/etc/modprobe.d/blacklist.conf /etc/modprobe.d/blacklist.conf

## add users and groups (ignore failures if groups already exist)
addgroup $ADMINGROUP
useradd -g $ADMINGROUP -G $TORADMINGROUP -s /bin/bash $ADMINUSER
# TODO: $ADMINUSER passwd?

# Configure arm
zcat $config_dir/armrc.sample.gz > /home/$ADMINUSER/.armrc

## Add arm startup trick with cron for shared screen run as $ADMINUSER
crontab -u $ADMINUSER $config_dir/tor-arm-crontab

## Touch a stamp to show that we're now a Torouter
echo "torouter $VERSION" > /etc/torouter

