web: gunicorn ocp.wsgi --log-file -
worker: celery -A ocp worker --loglevel=info
