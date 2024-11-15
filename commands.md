# Packages
Django
python-dotenv 1.0.1
djangorestframework==3.15.2
pytest==8.3.3
pytest-django==4.9.0
black==24.10.0
flake8==7.1.1
django-mptt==0.16.0
router==0.1
drf-spectacular==0.27.2
coverage==7.6.7
pytest-cov==6.0.0
factory_boy==3.3.1


# Commands
django.admin startproject 'name_of_project'
./manage.py runserver
from django.core.management.utils import get_random_secret_key
print(get_random_secret_key())
pip install python-dotenv
python.exe -m pip install --upgrade pip
pip install djangorestframework
pip install -U pytest
pip install black
pip install flake8
pip install django-mptt
pip install router
pip install drf-spectacular
pip install coverage
pip install pytest-cov
pip install pytest-factoryboy


## Pytest
pip install pytest-django
pytest -h   # prints options _and_ config file settings


## drf_spectacular (.yml)
python manage.py spectacular --file schema.yml


## coverage
coverage run -m pytest