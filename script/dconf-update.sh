#!/bin/bash 

printf "Updating dconf... "
cat ~/.config/dconf/user.d/* | dconf load /
printf "done\n"
