#!/bin/bash 

files=$(ls *.nasm)

for file in $files; do

	file=${file%.nasm}
	echo $file

	if echo $file | grep -q "64"; then
		nasm -g -f elf64 $file.nasm
		ld -o $file $file.o
	else
		nasm -g -f elf $file.nasm
		ld -m elf_i386 -o $file $file.o
	fi

	objdump -d $file
	
	shellcode=$(objdump -d $file | grep "[0-9a-f]:\+" | awk -F "\t" '{print $2}' | tr -d '[:space:]' | perl -pe 's/([0-9a-f]{2})/chr hex $1/gie')

	echo $shellcode | hexdump
	echo $shellcode > $file.shc
done
