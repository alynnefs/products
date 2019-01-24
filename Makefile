clean:
	./manage.py clean_pyc

setup: requirements-dev createsuperuser migrate

requirements-dev:
	pip install -r requirements/dev.txt

run:
	./djangoRest/manage.py runserver

migrate:
	./djangoRest/manage.py migrate

migrations:
	./djangoRest/manage.py makemigrations

showmigrations:
	./djangoRest/manage.py showmigrations

urls:
	./djangoRest/manage.py show_urls

shell:
	./djangoRest/manage.py shell_plus

shell-sql:
	./djangoRest/manage.py shell_plus --print-sql

collectstatic:
	./djangoRest/manage.py collectstatic

createsuperuser:
	./djangoRest/manage.py createsuperuser

test:
	cd djangoRest/ && ./manage.py test

showdoc:
	cd djangoRest/doc/_build/html && firefox index.html
