#!/usr/bin/bash 


if [[ $UID != 0 ]]; then
	echo "$0 must be run as root."
	exit
fi

if [[ -z $1 ]]; then
	echo "Usage: $0 {[c]onnect|[d]isconnect}"
fi

action=$1
tun=tunvpn
vpn_user=vincent.pasquier1
unix_user=helvethor
cafile=/home/helvethor/owncloud/heia/documents/vpn/VeriSignClass3PublicPrimaryCertificationAuthority-G5.pem


function connect {

	openvpn --mktun --dev $tun
	ip link set $tun up
	openconnect vpn.hefr.ch --authgroup=1 -i $tun -U $unix_user -u $vpn_user --cafile=$cafile

}


function disconnect {

	ip link set $tun down 
	openvpn --rmtun --dev $tun

}


case $action in

	c|connect)
		connect
		;;

	d|disconnect)
		disconnect
		;;

esac
