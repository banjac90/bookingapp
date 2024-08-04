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
python manage.py tests
python manage.py runserver
```
### 5. Setup React Frontend
```
cd bookingsfrontend
npm install
npm start
```
### 6. Access the Application
Once both servers are running, you can access the application at:
- Django backend: http://127.0.0.1:8000
- React frontend: http://localhost:3000
  
First create few flats and bookings.
You can do that by creating superuser and access admin panel or do it on links http://127.0.0.1:8000/api/flats and http://127.0.0.1:8000/api/bookings


