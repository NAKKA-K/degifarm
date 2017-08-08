@echo off
SET virtual="VirtualBox.exe"
SET git="Git.exe"
SET vag="vagrant.msi"
IF EXIST %virtual%==true %git%==true %vag%==true (GOTO FILE_TRUE) ELSE GOTO FILE_FALSE

:FILE_TRUE

rem VirtualBoxをインストール
call %virtual%

rem gitをインストール
call %git%

rem Vagrantをインストール
msiexec/i %vag%

:FILE_FALSE
  echo "いずれかのファイルが存在しません"
