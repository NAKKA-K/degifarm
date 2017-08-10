#!/bin/bash

#postgres管理者アカウントを使うのはセキュリティ上良くないため、DBユーザーを作成
createuser develop17

#データベース作成(オーナーはdevelop17)
createdb dw2018db -O develop17

#dw2018dbに接続
psql dw2018db

#86行目に他ユーザ(デフォのvagrantユーザなど)からもpsqlのdevelop17ユーザにアクセスできるように追加(仮)
sudo sed -i -e "85a local   all             develop17                               md5" /etc/postgresql/9.4/main/pg_hba.conf
 
