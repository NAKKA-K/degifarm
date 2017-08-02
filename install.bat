@echo off

rem VirtualBoxをインストール
call VirtualBox-5.1.26-117224-Win.exe

rem gitをインストール
call Git-2.13.3-64-bit.exe

rem Vagrantをインストール
msiexec/i vagrant_1.9.7_x86_64.msi
