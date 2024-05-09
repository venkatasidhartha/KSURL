python manage.py makemigrations
python manage.py collectstatic --no-input
python manage.py migrate

gunicorn --config gunicorn.conf.py KSURL.wsgi:application