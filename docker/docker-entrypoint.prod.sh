python manage.py collectstatic --no-input
python manage.py migrate --no-input
celery -A bipad beat -l info --scheduler django_celery_beat.schedulers:DatabaseScheduler &
celery -A bipad worker --concurrency=4 -l info &
gunicorn --bind 0.0.0.0:8000 bipad.wsgi:application
