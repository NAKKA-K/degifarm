# DW 2YearsGroup

## 製品概要



## 使用環境
* pyenv
* Django(python3.5.0)
* Git
* VirtualBox
* Vagrant(virtualBox)

## 環境設定
1.Windows上でgit、virtualbox、vagrantをインストールする。(各自のPCがWindowsであるとして解説)  
2.vagrantに仮想マシンを追加する。(dw2018_server/vagrant/README.mdを参照)  
3.dw2018_serverでGitBashを起動(右クリックで選べる)。  
4.GitBashで下記のコマンドを打ち込むとVagrantfileという設定ファイルが作られる。  

    $ vagrant init dw2018_server

5.そのままvagrantを起動。仮想環境に入る。  

    $ vagrant up
    $ vagrant ssh

6.pyenvとDjangoをインストール。  

※各インストール方法については下に書いているのでそちらを参照  


### Windows上(Git,VirtualBox,Vagrant)
指定のGoogleDriveからインストーラー(git,virtualbox,vagrant)をダウンロードして、プロジェクトの先頭にコピー。  
3つのインストーラーがそろったうえで、install.batを起動。  
GUIのインストーラーが順番に立ち上がるので、すべてデフォルトで進めていけば問題なく終了。  

### 仮想マシン上
#### pyenv  
このページのpyenvディレクトリに移動してREADMEを参照  

#### Django
※前項目のpyenvの内容が終わった後にインストールする。  
このページのwikiにあるdjangoの紹介ページを参照  

#### Git
pyenvをインストールする際に必要になるため、その時に自動インストールされる。  

