echo off
set virtual="VirtualBox.exe"
set git="Git.exe"
set vagrant="vagrant.msi"
set file="false"

if exist %virtual% if exist %git% if exist %vagrant% set file="true"

if %file%=="true" (
	echo OK、インストールを開始します
	rem VirtualBoxをインストール
	call %virtual%

	rem gitをインストール
	call %git%

	rem Vagrantをインストール
	msiexec/i %vagrant%
) else (
	echo いずれかのファイルが見つかりませんでした。
)
pause
