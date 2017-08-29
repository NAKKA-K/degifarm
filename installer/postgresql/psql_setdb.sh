#!/bin/bash

#postgres管理者アカウントを使うのはセキュリティ上良くないため、新しくユーザーを作成
createuser develop17
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

