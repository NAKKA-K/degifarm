@echo off
SET virtual="VirtualBox.exe"
SET git="Git.exe"
SET vag="vagrant.msi"
IF EXIST %virtual%==true %git%==true %vag%==true (GOTO FILE_TRUE) ELSE GOTO FILE_FALSE

:FILE_TRUE

rem VirtualBox���C���X�g�[��
call %virtual%

rem git���C���X�g�[��
call %git%

rem Vagrant���C���X�g�[��
msiexec/i %vag%

:FILE_FALSE
  echo "�����ꂩ�̃t�@�C�������݂��܂���"
