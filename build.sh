#!/user/bin/env bash

set -o errexit
pip install -r requirements.txt
python manage.py collectstatic --no-input

python manage.py migrate

#set -o errexit
#pip install -r r.txt
#python manage.py collectstatic --no-input
#python manage.py makemigrations
#python manage.py migrate


#python manage.py createsuperuser --no-input
#python manage.py loaddata store/fixtures/products.json	
#python manage.py loaddata store/fixtures/news.json
