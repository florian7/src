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
	echo $storage_dir/$(						\
		echo $dconf_dir 		\
			| sed 's/^\///g' 	\
			| sed 's/\/$//g' 	\
			| sed 's/\//-/g').conf
}

function action () {
	for dconf_dir in $dconf_dirs; do
		action_$1 $dconf_dir
	done
}

function action_dump () {
	dconf_dir=$1
	file=$(storage_file $dconf_dir)

	echo Dumping $file ...
	dconf dump $dconf_dir > $file
}

function action_load () {
	dconf_dir=$1
	file=$(storage_file $dconf_dir)

	echo Loading $file ...
	dconf load $dconf_dir < $file
}

function action_diff () {
	dconf_dir=$1
	file=$(storage_file $dconf_dir)
	tmp_file=$file.tmp

	echo Looking for differences in $file ...
	dconf dump $dconf_dir > $tmp_file
	diff $file $tmp_file
	rm $tmp_file
}

function help () {
	echo "Usage: $1 {load|dump}"
}

case $1 in
	dump)
		action dump
		;;
	load)
		action load
		;;
	diff)
		action diff
		;;
	*)
		help $0
		;;
esac
