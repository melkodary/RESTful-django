# RESTful_Django

This is a simple django project:
- Custom user model that uses the phone number as the primary key instead.
- Basic Custom user manager & serializers
- Basic REST-API for creating new users and authentication to retrieve a oauth token.
- Admin Page available.

To run:
- Clone repo and go to repo.
- Create virtualenv: 'python3 -m venv env'
- activate the virtual env: source env/bin/activate
- install all packages requirements: pip3 install -r requirements.txt
- Django orm: makemigrations and migrate
  - 'python manage.py makemigrations'
  - 'python manage.py migrate'
  
- run server and enjoy :)
  - 'python manage.py runserver 8000'  
  

REST urls:
- localhost:8000/admin
- localhost:8000/users/register/
- localhost:8000/users/api-token-auth/


NOTE: Check email_username branch which includes country code also as a field. 