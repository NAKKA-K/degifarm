#!/bin/bash

#postgres管理者アカウントを使うのはセキュリティ上良くないため、新しくユーザーを作成
psql -c "create role develop17 with superuser login 'develop17'"
#createuser develop17
echo -e 'develop17ユーザを作成しました\n'

#データベース作成
createdb dw2018db
echo -e 'dw2018dbデータベースを作成しました\n'

#このDBが不正アクセスされないように権限を削除
psql -c "revoke connect on database dw2018db from public"
echo -e 'dw2018dbデータベースの権限を削除しました\n'

#develop17ユーザからのみのアクセスを受け付ける
psql -c "grant connect on database dw2018db to develop17"
echo -e 'develop17ユーザからのアクセスのみできるように設定しました\n'

#作成したDBのオーナーを変更
psql -c "alter database dw2018db owner to develop17"
echo -e '作成したdw2018dbのオーナーをdevelop17に変更'

#develop17ユーザにスーパユーザを付与
psql -c "alter role develop17 with superuser"
echo -e 'develop17ユーザにスーパユーザを付与しました'

#dw2018dbのオーナーをdevelop17ユーザに
psql -c "alter database dw2018db owner to develop17"
echo -e 'dw2018dbのオーナーをdevelop17ユーザに変更しました'

#develop17ユーザのパスワードを設定
psql -c "alter role develop17 with password develop17"
echo -e 'develop17ユーザのパスワードを設定しました(develop17)'
