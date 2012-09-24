#!/bin/sh

set -e

if ! [ `uname -r` = "3.2.0-3-kirkwood" ]
then
    echo "Got: `uname -r`, need 3.2.0-3-kirkwood"
    echo "Wrong kernel version, binary module won't work. Try a source install?"
    exit 1
fi

mkdir /lib/modules/$(uname -r)/kernel/drivers/net/wireless/libertas_uap
cp uap8xxx.ko-$(uname -r) /lib/modules/$(uname -r)/kernel/drivers/net/wireless/libertas_uap
depmod -a
cp -r firmware/mrvl /lib/firmware/mrvl
cp modprobe_libertas_uap.conf /etc/modprobe.d/libertas_uap
