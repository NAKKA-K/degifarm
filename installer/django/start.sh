#djangoのプロジェクト作成
django-admin startproject projecttest

#設定ファイルに書き込み
echo 'DATABASES = {' >> ~/projecttest/projecttest/setting.py
echo '   'default': {' >> ~/projecttest/projecttest/setting.py
echo '        'ENGINE': 'django.db.backends.postgresql_psycopg2',' >> ~/projecttest/projecttest/setting.py
echo '        'NAME': 'dw2018db',' >> ~/projecttest/projecttest/setting.py
echo '        'USER': 'develop17',' >> ~/projecttest/projecttest/setting.py
echo '        'PASSWORD' : 'develop17',' >> ~/projecttest/projecttest/setting.py
echo '        'HOST' : '127.0.0.1',' >> ~/projecttest/projecttest/setting.py
echo '        'PORT' : 5432,' >> ~/projecttest/projecttest/setting.py
echo '    }' >> ~/projecttest/projecttest/setting.py
echo '}' >> ~/projecttest/projecttest/setting.py
