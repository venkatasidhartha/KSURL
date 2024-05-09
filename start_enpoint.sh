python manage.py makemigrations
python manage.py migrate
gunicorn --config gunicorn.conf.py KSURL.wsgi:application