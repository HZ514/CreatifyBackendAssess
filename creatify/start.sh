#!/bin/bash
python manage.py collectstatic --noinput&&
python manage.py makemigrations&&
python manage.py migrate&&
# 暂时采用开发服务，后续配置使用wsgi。
python manage.py runserver 0.0.0.0:8000&&
#tail -f /dev/null

exec "$@"
