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
2.vagrantにboxを追加する。

    指定のGoogleDriveのvagrantフォルダからpackage.boxをダウンロードして、自分のdw2018_server/vagrantにコピー。
    自分のdw2018_server/vagrant/vagrant_add.shを実行。(OK！とでたら完了)

3.自分のdw2018_serverでGitBashを起動(右クリックで選べる)。
4.GitBashで下記のコマンドを打ち込むとVagrantfileという設定ファイルが作られる。

    $ vagrant init dw2018_server

5.そのままvagrantの仮想環境に入る。

    $ vagrant up
    $ vagrant ssh

6.pyenvとDjangoをインストール。

※各インストール方法については下に書いているのでそちらを参照


### Windows上はこちらで一括
指定のGoogleDriveからインストーラー(git,virtualbox,vagrant)をダウンロードして、プロジェクトの先頭にコピー。
3つのインストーラーがそろったうえで、install.batを起動。
GUIのインストーラーが順番に立ち上がるので、すべてデフォルトで進めていけば問題なく終了。

### pyenv
このページのpyenvディレクトリに移動してREADMEを参照

### Django
このページのDjangoディレクトリに移動してREADMEを参照

### Git
**Mac**  
今回は割愛

**Linux**  
Debian系統のディストリビュージョンであれば  
`$ apt-get install git`

Fedora系統のディストリビュージョンであれば  
`$ yum install git`

でインストールできます。

### VirtualBox
**Mac**  
今回は割愛

**Linux**  
今回は割愛

### Vagrant
**Mac**  
今回は割愛

**Linux**
今回は割愛


