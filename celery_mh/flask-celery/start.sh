
# start celery worker
celery -A celery_module.celery worker -l info  &

# start python web app

python main.py

