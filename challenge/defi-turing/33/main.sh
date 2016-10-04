#!/bin/bash 

sum=0
for year in {2001..9999}; do
	if ncal -e $year | grep "April" -q; then
		sum=$((sum + 1))
	fi
done

echo $sum
