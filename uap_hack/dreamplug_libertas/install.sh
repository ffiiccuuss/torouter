#!/bin/sh

set -e

if [ -n "$1" ]
then
    kernelversion=$1
else
    echo "Need to specify a kernel version!" > /dev/stderr
    exit 1
fi

mkdir -p /lib/modules/$kernelversion/kernel/drivers/net/wireless/libertas_uap
cp uap8xxx.ko-$kernerlversion /lib/modules/$kernelversion/kernel/drivers/net/wireless/libertas_uap/uap8xxx.ko
depmod -a
cp -r firmware/mrvl /lib/firmware/mrvl
cp modprobe_libertas_uap.conf /etc/modprobe.d/libertas_uap
