#!/bin/bash 

# System configuration tunner
# Run as root

if [[ $UID != 0 ]]; then
	echo "This script must be run as root"
	exit
fi


# Libreoffice should use GTK till GTK3 is better supported

expression="export SAL_USE_VCLPLUGIN=gtk"
files="/etc/profile.d/libreoffice-fresh.sh /etc/profile.d/libreoffice-still.sh"

for file in $files; do
	if [[ -e $file ]]; then
		echo "Patching $file to use GTK"
		sed -i "s/^#$expression$/$expression/" $file
	fi
done


# Makepkg MAKEFLAGS

expression="MAKEFLAGS="
file=/etc/makepkg.conf 

if [[ -e $file ]]; then
	echo "Optimizing makepkg compilation"
	sed -i "s/^#$expression.*/MAKEFLAGS=\"-j$(nproc)\"/" $file
fi
