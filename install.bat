echo off
set virtual="VirtualBox.exe"
set git="Git.exe"
set vagrant="vagrant.msi"
set file="false"

if exist %virtual% if exist %git% if exist %vagrant% set file="true"

if %file%=="true" (
	echo OK�A�C���X�g�[�����J�n���܂�
	rem VirtualBox���C���X�g�[��
	call %virtual%

	rem git���C���X�g�[��
	call %git%

	rem Vagrant���C���X�g�[��
	msiexec/i %vagrant%
) else (
	echo �����ꂩ�̃t�@�C����������܂���ł����B
)
pause
