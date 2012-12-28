#!/bin/sh

set -e

if [ -n "`mount | grep 'mnt'`" ]
then
    echo "/mnt mount point is in use?"
    exit 1
fi

if ! [ -b "$1" ]
then
    echo "need to specify a target boot partition (/dev/sdb1)"
    exit 1
else
    BOOTDEV=$1
fi

if ! [ -b "$2" ]
then
    echo "need to specify a target root partition (/dev/sdb2)"
    exit 1
else
    ROOTDEV=$2
fi

echo "mounting rootdev..."
mount $ROOTDEV /mnt
echo "rsyncing over rootfs"
rsync -atv --progress --delete --exclude=boot build/armhf/ /mnt/
echo "sync filesystems..."
sync
echo "un-mounting rootdev..."
umount /mnt

echo "mounting bootdev..."
mount $BOOTDEV /mnt
echo "copying boot files..."
cp -v build/armhf/boot/* /mnt
echo "sync filesystems..."
sync
echo "un-mounting bootdev..."
umount /mnt
