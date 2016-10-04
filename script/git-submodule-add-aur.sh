#!/bin/bash 

if [[ $1 != -f ]]; then
	echo "This script is disabled, force it with -f"
	exit
fi
shift

HOME_DIR=~
AUR_DIR=~/src/aur
AUR_PROJECTS=$(ls $AUR_DIR)

for project in $AUR_PROJECTS; do
	if ! grep -q "$project" ~/.gitmodules; then

		project_dir=$AUR_DIR/$project
		url=$(cat $project_dir/.git/config | grep "url")
		path=${project_dir#$HOME_DIR/}

		printf "[submodule \"$path\"]\n" >> $HOME_DIR/.gitmodules
		printf "\tpath = $path\n" >> $HOME_DIR/.gitmodules
		printf "$url\n" >> $HOME_DIR/.gitmodules

	fi
done
