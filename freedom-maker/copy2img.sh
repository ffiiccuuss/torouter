#!/bin/sh

set -e

if [ -b "$1" ]
then
    DEV=$1
else
    echo "need to specify a card device (eg, /dev/sdb)"
    exit 1
fi

NAME="torouter-dev"
if [ -n "$2" ]
then
    NAME=$2
fi

echo "dd-ing $DEV to $NAME.img"
dd if=$DEV of=$NAME.img bs=1M
echo "gzip compressing image"
gzip $NAME.img

