#!/bin/bash 

storage_dir=~/.config/dconf/user.d

read -r -d '' dconf_dirs << EOM 
	/org/gnome/evolution/
	/org/gnome/evolution-data-server/
	/org/gnome/desktop/
	/org/gnome/shell/
	/org/gnome/terminal/
	/org/gnome/polari/
EOM


function storage_file () {
	dconf_dir=$1
	echo $(						\
		echo $dconf_dir 		\
			| sed 's/^\///g' 	\
			| sed 's/\/$//g' 	\
			| sed 's/\//-/g').conf
}

function dump () {
	for dconf_dir in $dconf_dirs; do
		file=$(storage_file $dconf_dir)
		echo Dumping $file ...
		dconf dump $dconf_dir > $storage_dir/$file
	done
}

function load () {
	for dconf_dir in $dconf_dirs; do
		file=$(storage_file $dconf_dir)
		echo Loading $file ...
		dconf load $dconf_dir < $storage_dir/$file
	done
}

function help () {
	echo "Usage: $1 {load|dump}"
}

case $1 in
	dump)
		dump
		;;
	load)
		load
		;;
	*)
		help $0
		;;
esac
