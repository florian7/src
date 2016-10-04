#!/bin/bash

function configure
{
	env LDFLAGS=-ldl \
	./configure --prefix=/opt/apache \
		--enable-so \
		--enable-file-cache=shared \
		--enable-cache=shared \
		--enable-disk-cache=shared \
		--enable-mem-cache=shared \
		--enable-log-forensic=shared \
		--enable-mime-magic=shared \
		--enable-headers=shared \
		--enable-usertrack=shared \
		--enable-fcgid=shared \
		--enable-rewrite=shared \
		--enable-ssl=static \
		--with-ssl=/opt/openssl
}

if [ -z "$1" ]; then
	command=-a
else
	command=$1
fi

case $command in
	-c)
		configure
		;;
	-m)
		make
		;;
	-i)
		make install
		;;
	-a)
		set +e
		configure
		make
		make install
		;;
esac
