#!/bin/bash 

sudo aptitude install libncurses5-dev libgnome2-dev libgnomeui-dev \
	libgtk2.0-dev libatk1.0-dev libbonoboui2-dev \
	libcairo2-dev libx11-dev libxpm-dev libxt-dev python-dev \
	ruby-dev git -y

sudo aptitude remove vim vim-runtime gvim vim-tiny vim-common vim-gui-common -y

git clone https://github.com/vim/vim 

cd vim

./configure --with-features=huge \
	--enable-multibyte \
	--enable-rubyinterp \
	--enable-pythoninterp \
	--enable-perlinterp \
	--enable-luainterp \
	--enable-termtruecolor \
	--with-tlib=ncurses \
	--with-python-config-dir=/usr/lib/python2.7/config \
	--enable-gui=gtk2 --enable-cscope --prefix=/opt/vim

make VIMRUNTIMEDIR=/opt/vim/share/vim/vim74

sudo make install

PATH=$PATH:/opt/vim/bin/ 
export PATH

sudo update-alternatives --install /usr/bin/editor editor /opt/vim/bin/vim 1
sudo update-alternatives --set editor /opt/vim/bin/vim
sudo update-alternatives --install /usr/bin/vi vi /opt/vim/bin/vim 1
sudo update-alternatives --set vi /opt/vim/bin/vim

vim --version
