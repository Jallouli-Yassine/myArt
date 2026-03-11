import os
os.environ['DJANGO_SUPERUSER_PASSWORD'] = 'admin123'
os.environ['DJANGO_SUPERUSER_USERNAME'] = 'admin'
os.environ['DJANGO_SUPERUSER_EMAIL'] = 'admin@myart.com'
os.system('python manage.py createsuperuser --noinput')
