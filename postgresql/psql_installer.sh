#postgresqlをインストール
sudo apt-get update
sudo apt-get -y install postgresql
echo -e 'postgresqlをインストールしました\n'

#58行目に他ホストからもアクセスできるように追加
sudo sed -i -e "58a listen_address = '*'" /etc/postgresql/9.4/main/postgresql.conf

#posgreを起動
sudo /etc/init.d/postgresql start
echo -e 'postgresqlを起動しました\n'

#postgresql管理者アカウントのパスワードを新しく設定(postgresに統一)
echo -e 'パスワードを設定してください。postgresに統一します。\n'
sudo passwd postgres
echo -e 'postgreユーザのパスワードを設定しました\n'

#develop17ユーザを作成
echo -e '開発用に使用するdevelop17ユーザを作成します。\nパスワードはdevelop17(2回入力)に統一してください。\n入力し終わった後は、5回エンターキーを押してもらった後にIs the information correct?と聞かれるので、Yを入力して下さい。\n'
sudo adduser develop17
echo -e 'develop17ユーザを作成しました\n'

#postgresqlにログイン
echo 'postgresユーザに切り替えます。パスワードはpostgresです。\n'
su - postgres
