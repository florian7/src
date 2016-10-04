#!/bin/bash 

RUN_NAME=$(basename $0)

function usage ()
{
	echo "Usage: $RUN_NAME [options] <file[s]>"
	echo ""
	echo "    Options:"
	echo "        -b      Keep a backup file (.bak). Only applies if - is not set."
	echo "        -t n    Replace tabs (\t) with n spaces."
	echo "        -       Print to stdout rather than replace the files."
	echo ""
	echo "    Files:"
	echo "        List of text files. Programming languages like shell which"
	echo "        require \ on line-breaks are not supported."
	echo ""
	echo "    Author:"
	echo "        Vincent Pasquier <vincentpasquier@posteo.net>"

	exit
}

function options ()
{
	while [[ $1 =~ -[a-z]? ]]; do

		case $1 in
			-b)
				KEEP_BAK=1
				;;
			-t)
				shift
				[[ ! $1 =~ [0-9]+ ]] && usage

				REPLACE_TABS=$(printf "%-${1}s" " ")
				;;
			-)
				STDOUT=1
				;;
		esac

		shift
	done

	args=$@
}

function main ()
{
	[[ ! -f $1 ]] && usage

	while [[ -f $1 ]]; do

		TMP_FILE=${1}.tmp
		TMP2_FILE=${1}.tmp2
		BAK_FILE=${1}.bak
		ORI_FILE=$1

		if [[ -n $KEEP_BAK ]]; then
			cp $ORI_FILE $BAK_FILE
		fi

		fmt -c -s -w 80 $ORI_FILE > $TMP_FILE

		if [[ -n $REPLACE_TABS ]]; then
			sed "s/\t/$REPLACE_TABS/" $TMP_FILE> $TMP2_FILE
			mv $TMP2_FILE $TMP_FILE
		fi

		if [[ -n $STDOUT ]]; then
			cat $TMP_FILE	
		else
			cp $TMP_FILE $ORI_FILE
		fi

		rm $TMP_FILE
		shift
	done

	args=$@
}

args=$@

options $args
main $args
