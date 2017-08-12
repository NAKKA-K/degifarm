#postgresqlをインストール
sudo apt-get update
sudo apt-get -y install postgresql

echo 'postgresqlをインストールしました'

#58行目に他ホストからもアクセスできるように追加
sudo sed -i -e "58a listen_address = '*'" /etc/postgresql/9.4/main/postgresql.conf

#posgreを再起動
sudo /etc/init.d/postgresql start

#postgresql管理者アカウントのパスワードを新しく設定(postgresに統一)
echo 'パスワードを設定してください。postgresに統一します。'
sudo passwd postgres

#postgresqlにログイン
su - postgres
