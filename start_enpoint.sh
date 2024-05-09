python manage.py makemigrations --no-input
python manage.py collectstatic --no-input
python manage.py migrate --no-input
gunicorn --config gunicorn.conf.py KSURL.wsgi:application