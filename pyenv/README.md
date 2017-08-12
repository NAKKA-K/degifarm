# pyenv_installer
pyenvをインストールするスクリプト  

※インストールにgitを使用するため、自動的にgitもインストールされます。  


# pyenv Install手順
※dw2018_serverのディレクトリにいると仮定して記述

    $ cd pyenv/
    $ chmod +x pyenv_installer.sh
    $ ./pyenv_installer.sh
    $ source ~/.bash_profile


# pythonの環境設定
※3.5.0をインストールする場合

    $ pyenv install 3.5.0

とすればインストールされる場合はそれで問題ないが、当方の環境では警告&エラーが発生してインストールできなかった。  
その場合の解決策として必要なライブラリをインストールするスクリプトを用意したので、そちらを実行すれば問題なくインストールされた。  

    $ chmod +x pyenv_setting.sh
    $ ./pyenv_setting.sh

とすれば、同時に`$ pyenv install 3.5.0`も実行されるので、エラーがなければインストール完了。  
インストールが完了すれば、インストールしたものを有効化する。
今回はglobalに設定する。

    $ pyenv global 3.5.0

とすれば、設定できる。詳しくはwikiのpyenvについてを参照。
