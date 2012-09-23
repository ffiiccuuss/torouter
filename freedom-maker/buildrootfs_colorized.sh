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

./buildrootfs.sh $1 $2 2> >(while read line; do echo -e "\e[01;31m$line\e[0m"; done)

