#!/bin/bash

#postgres管理者アカウントを使うのはセキュリティ上良くないため、DBユーザーを作成
createuser develop17
echo 'develop17ユーザを作成しました'

#データベース作成(オーナーはdevelop17)
createdb dw2018db -O develop17
echo 'dw2018dbデータベースを作成しました'

#develop17ユーザのパスワードを設定
psql -c "alter user develop17 with password 'develop17'"
echo 'develop17ユーザのパスワードを設定しました(パスワードはdevelop17) '

