#!/bin/sh

# no errors
set -x

echo "This program will now reconfigure your Debian system into a Torouter"

export config_dir="/usr/share/torouter-prep/example-configs/"

# Add a user to administrate the Torouter later
export ADMINUSER="torouter"
export ADMINGROUP="torouter"
export TORADMINGROUP="debian-tor"

# This is the main Tor repo apt pubkey
apt-key add $config_dir/tmp/A3C4F0F979CAA22CDBA8F512EE8CBC9E886DDD89.apt-key

# This is the temp torrouter archive pubkey; this should be updated when we
# freeze this repo and know what we want to do
apt-key add $config_dir/tmp/047E6A24.asc

# We need to prep apt to understand that we want packages from other repos
cp $config_dir/etc/sources.list /etc/apt/sources.list

apt-get -y update

# add packages (hopefully many of these will already be installed)
apt-get -y install apt-utils vim less screen lsof wireless-tools iputils-ping \
  lsof net-tools tcptraceroute traceroute mtr-tiny uaputl uapevent denyhosts \
  ufw openntpd tor tor-geoipdb libnatpmp-dev libnatpmp1 libminiupnpc-dev \
  libminiupnpc5 tor-arm ttdnsd dnsmasq isc-dhcp-client unbound torouterui

# TODO: check if uap8xxx is existant; if not, try to install libertas_uap
# drivers

# do the heavy lifting
torouter_preboot.sh

echo "Syncing filesystem just in case..."
sync

echo "Exiting torouter_config.sh!"

