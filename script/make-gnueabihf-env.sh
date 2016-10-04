#!/bin/bash 
[[ "${BASH_SOURCE[0]}" == "${0}" ]] && printf "This script is meant to be sourced.\nExiting.\n" && exit 0

PATH=$(find /home/helvethor/toolchain -iname bin | head -n 1):$PATH
ARCH=arm
CROSS_COMPILE=arm-linux-gnueabihf-

export PATH ARCH CROSS_COMPILE

echo "Environnement set."
