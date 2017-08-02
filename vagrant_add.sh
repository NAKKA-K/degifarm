#!/bin/bash
packageName='samurai'
#vagrant box add dw2018_server "${packageName}"

#指定のパッケージが追加されているか判定
boxList="`vagrant box list | grep "${packageName}"`"
echo $boxList

if [ boxList == ".*${packageName}.*" ]; then
  echo OK! Added package!
else
  echo NO! Not added package!
fi
