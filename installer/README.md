# 使用環境
* pyenv 1.1.3-25-gfd0b8fc
* Django1.11.4(python3.5.0)
* Git
* VirtualBox
* Vagrant

# 環境設定
1.Windows上でgit、virtualbox、vagrantをインストールする。(各自のPCがWindowsであるとして解説)  

2.vagrantに仮想マシンを追加する。(カレントディレクトリにpackage.boxをダウンロードしておく。GitBashを起動(右クリックで選べる))  

    $ vagrant box add dw2018_server package.box

3.仮想マシンを作成する。(Vagrantfileという設定ファイルが作られる。)  

    $ vagrant init dw2018_server

5.そのままvagrantを起動。仮想環境に入る。  

    $ vagrant up
    $ vagrant ssh

6.後はgit cloneでNAKKA-K/sw2018_serverを取得して、開発に参加する。  

    $ git clone https://github.com/NAKKA-K/dw2018_server.git

7.開発のテストをするためにvagrantの設定を編集する。vagrant設定のwikiを参照してください。  
※各インストール方法については下に書いているのでそちらを参照  


## Windows上(Git,VirtualBox,Vagrant)
指定のGoogleDriveからインストーラー(git,virtualbox,vagrant)をダウンロードして、起動。  
GUIのインストーラーが立ち上がるので、すべてデフォルトで進めていけば問題なく終了。  

## 仮想マシン上
今回はすでに環境を構築し終わったpackageをそのまま使用しますが、一部のみのインストールなどを別途したい場合は下記を参照してください。  

### pyenv  
このページのpyenvディレクトリに移動してREADMEを参照  

### Django
詳しくはこのページのwikiにあるdjangoの紹介ページを参照  
※前項目のpyenvの内容が終わった後にインストールする。  

    pip install django

### Git
pyenvをインストールする際に必要になるため、その時に自動インストールされる。  

