#!/bin/bash
packageName='package.box'
vagrantBoxName='dw2018_server'
vagrant box add "${vagrantBoxName}" "${packageName}"

#指定のパッケージが追加されているか判定
boxList="`vagrant box list | grep "${vagrantBoxName}"`"

if [[ "${boxList}" =~ (.*)${vagrantBoxName}(.*) ]]; then
  echo OK! Added box!
else
  echo NO! Not added box!
fi
