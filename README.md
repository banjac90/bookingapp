# Simple Django Project for Book Flat

## Overview
This is a simple project that uses Django for the backend and React for the frontend.

## Setup Steps

### 1. Setup Python Virtual Environment
First, create and activate a Python virtual environment. 

```
bash
python -m venv env
source env/bin/activate  # On Windows use `env\Scripts\activate
```
### 2. Clone repo
```
git clone https://github.com/banjac90/bookingapp
cd bookingapp
```
### 3. Install Backend Dependencies
```
pip install -r requirements.txt
```
### 4. Set Up Django
Also here are tests, we do it before run server, to be sure that everything runs smoothly
```
python manage.py migrate
python manage.py test
python manage.py runserver
```
### 5. Setup React Frontend
```
cd bookingsfrontend
npm install
npm start
```
### 6. Access the Application
First stop servers and create superuser in Django. 

Then in admin panel create few flats and bookings. Once you have some data in database run both servers. 
```
python manage.py runserver
```
and in bookingsfrontend folder
```
npm start
```

You can access the application at:
- Django backend: http://127.0.0.1:8000
- React frontend: http://localhost:3000

Now try it!





