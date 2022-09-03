release: python manage.py makemigrations && python manage.py migrate
web: gunicorn hike_slovakia.wsgi:application