#!/bin/bash
packageName = 'package.box'
vagrant box add dw2018_server $packageName

if [ vagrant box list | grep "${packageName}" != "" ]; then
  echo OK! Added package!
else
  echo NO! Not added package!
fi
