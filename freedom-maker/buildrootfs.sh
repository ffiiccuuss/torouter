#!/bin/bash
# 
# Copyright 2011 by Bdale Garbee <bdale@gag.com>
# 
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
# 
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
# 
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
# 

# based on work by <ivan@sanchezortega.es>, who released his script under
# the following license terms:
#  ----------------------------------------------------------------------------
#  "THE BEER-WARE LICENSE" (Revision 42):
#  As long as you retain this notice you can do whatever you want with 
#  this stuff. If we meet some day, and you think this stuff is worth it, 
#  you can buy me a beer in return.
#  ----------------------------------------------------------------------------

# mk_dreamplug_rootfs
#
# Runs multistrap and readies the resulting root filesystem to silently 
# complete package configuration on the first boot-up.
#
# Accepts the multistrap config file name as an argument.

# We don't tolerate errors.
set -e

architecture='armel'
kernelversion='3.2.0-3-kirkwood'
if [ -n "$1" ]
then
    architecture=$1
fi
export kernelversion

config=multistrap-configs/torouter-$architecture.conf
if [ -n "$2" ]
then
    config=$2
fi

# users
hostname='torouter'
rootpassword='freedom'
user='torouter'
userpassword='freedom'
export hostname
export rootpassword
export user
export userpassword

# where to build images, etc
basedir=`pwd`/build
source=`pwd`/source
target=$basedir/$architecture
tmpdir=$basedir/tmp
pkgcache=$tmpdir/aptcache
homedir=$target/home/$user
export basedir
export source
export target
export tmpdir
export pkgcache
export homedir

# clear any old cruft
if (mount | grep $target/var/cache/apt) 
then
    umount $target/var/cache/apt/
fi

# make the directories we'll need.
mkdir -p $target
rm -rf $target/*
mkdir -p $tmpdir
mkdir -p $pkgcache
mkdir -p $target/var/cache/apt/ && mount -o bind $pkgcache $target/var/cache/apt/
mkdir -p $target/var/cache/apt/archives
mkdir -p $target/usr/bin
mkdir -p $homedir

echo "Multistrapping..."
# XXX: DEATH: work around torrouter.torproject.org GPG key issue
# XXX: see also auth=false in multistrap config files
# multistrap -f $config -d $target
multistrap --no-auth -f $config -d $target
rm -f $target/etc/apt/sources.list.d/multistrap-debian.list

# un-do the bind mount so we don't trip over it later
umount $target/var/cache/apt/

# copy!
echo "Copying the source directory to the torouter rootfs..."
rsync -av $source/ $target

# add extra packages to the image
bin/packages

# cleanup and finalize the image so it boots correctly.
echo "Finalizing..."
bin/finalize

# finish!
echo "Syncing..."
sync
echo "Finished. You may now copy the rootfs to the plug."
