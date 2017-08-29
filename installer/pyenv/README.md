# pyenv_installer
pyenvをインストールするスクリプト  

※インストールにgitを使用するため、自動的にgitもインストールされます。  


# pyenv Install手順
※dw2018_serverのディレクトリにいると仮定して記述

    $ sh pyenv_installer.sh
    $ source ~/.bash_profile


# pythonの環境設定
※3.5.0をインストールする場合

    $ sh pyenv_setting.sh

インストールが完了すれば、インストールしたものを有効化する。
今回はglobalに設定する。(個人の責任で別の設定も可)

    $ pyenv global 3.5.0

とすれば、設定できる。詳しくはwikiのpyenvについてを参照。
