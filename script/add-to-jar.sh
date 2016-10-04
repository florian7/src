#!/bin/bash 

profile_dir=~/.minecraft/versions
profile_name=$1
profile=$profile_dir/$profile_name/$profile_name.jar

mod_dir=~/owncloud/minecraft
mod_name=$2
mod=$mod_dir/$mod_name

tmp_dir=/tmp/add-to-jar
tmp_profile_dir=$tmp_dir/profile
tmp_mod_dir=$tmp_dir/mod

mkdir $tmp_dir
mkdir $tmp_profile_dir
mkdir $tmp_mod_dir

unzip $profile -d $tmp_profile_dir
unzip $mod -d $tmp_mod_dir

cp -r $tmp_mod_dir/* $tmp_profile_dir
[ -e $tmp_profile_dir/META-INF ] && rm -rf $tmp_profile_dir/META-INF

mv $profile $profile.bak

old_dir=$(pwd)
cd $tmp_profile_dir

zip $profile *
cd $old_dir
