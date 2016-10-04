#!/bin/bash 

if [[ -z $1 ]]; then
	echo "Usage: $0 <file.colorscheme>"
	exit
fi

while read line; do

	if [[ ! $line =~ ^Color ]]; then
		echo $line
	
	else
		rgb=$(echo ${line#Color=} | sed 's/,/ /g')
		hex=$(ruby -pae '$_=?#+"%02X"*3%$F' <<< $rgb)

		echo "Color=$hex"

	fi

done < $1
