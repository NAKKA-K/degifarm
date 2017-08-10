#!/bin/bash

#install git
sudo apt-get -y install git


#pyenv download
git clone https://github.com/yyuu/pyenv.git ~/.pyenv

#Write pyenv setting on ~/.bash_profile
echo 'export PYENV_ROOT="$HOME/.pyenv"' >> ~/.bash_profile
echo 'export PATH="${PYENV_ROOT}/bin:$PATH"' >> ~/.bash_profile
echo 'eval "$(pyenv init -)"' >> ~/.bash_profile

#~/.bash_profileの変更を更新($ source ~/.bash_profile)
