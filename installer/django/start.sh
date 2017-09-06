#!/bin/sh
project=projecttest
#djangoのプロジェクト作成
django-admin startproject ${project}

#設定ファイルに書き込み
sed -i -e "s/'django.db.backends.sqlite3'/'django.db.backends.postgresql_psycopg2'/g" ~/dw2018_server/${project}/${project}/settings.py
sed -i -e "s/os.path.join(BASE_DIR, 'db.sqlite3')/'dw2018db'/g" ~/dw2018_server/${project}/${project}/settings.py 
sed -i -e "79a\        \'USER': 'develop17'," ~/dw2018_server/${project}/${project}/settings.py
sed -i -e "80a\        \'PASSWORD' : 'develop17'," ~/dw2018_server/${project}/${project}/settings.py
sed -i -e "81a\        \'HOST' : '127.0.0.1'," ~/dw2018_server/${project}/${project}/settings.py
sed -i -e "82a\        \'PORT' : '5432'," ~/dw2018_server/${project}/${project}/settings.py
