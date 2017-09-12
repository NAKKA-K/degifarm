#!/bin/bash

#postgresqlをインストール
sudo apt-get update
sudo apt-get -y install postgresql libpq-dev python-psycopg2
echo -e 'postgresqlをインストールしました\n'

#posgreを起動
sudo /etc/init.d/postgresql start
echo -e 'postgresqlを起動しました\n'

#postgresql管理者アカウントのパスワードを新しく設定(postgresに統一)
echo -e 'パスワードを設定してください。postgresに統一します。\n'
sudo passwd postgres
echo -e 'postgresユーザのパスワードを設定しました\n'

#develop17ユーザを作成
echo -e '開発用に使用するdevelop17ユーザを作成します。\nパスワードはdevelop17(2回入力)に統一してください。\n入力し終わった後は、5回エンターキーを押してもらった後にIs the information correct?と聞かれるので、Yを入力して下さい。\n'
sudo adduser develop17
echo -e 'develop17ユーザを作成しました\n'

#postgresユーザのホームディレクトリにpsql_setdb.shを実行できるようにコピーしておく
sudo cp ~/dw2018_server/postgresql/psql_setdb.sh /var/lib/postgresql/psql_setdb.sh 
echo -e 'psql_setdbをpostgresユーザのホームディレクトリに移動しました\n'

#postgresqlにログイン
echo -e 'postgresユーザに切り替えます。パスワードはpostgresです。\n'
su - postgres
