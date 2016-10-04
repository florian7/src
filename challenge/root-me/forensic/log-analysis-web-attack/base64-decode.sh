#!/bin/bash 

if [[ -z $1 ]]; then
	echo "Usage: $0 <file>"
	exit
fi 


timestamp=0
i=-1
IFS=$'\n'
for line in $(cat $1); do

	date=$(echo $line | sed -n 's/.*:\([0-9]\{2\}:[0-9]\{2\}:[0-9]\{2\}\).*/\1/p')

	old_timestamp=$timestamp
	timestamp=$(date -d $date +%s)
	difference=$((timestamp - old_timestamp))

	echo "==================================================="
	echo $line | cut -f -5 -d " "
	echo "---------------------------------------------------"
	echo $line | awk '{print $7}' | sed 's/^.*order=//' | sed 's/%3D/=/g' | base64 -d
	echo
	echo "---------------------------------------------------"
	echo "Timestamp: $timestamp"
	echo "Difference: $difference"	
done
