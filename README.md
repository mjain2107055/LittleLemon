# LittleLemon
## commands
### activate the shell
python3 -m pipenv shell
### install django
python3 -m pipenv install django
### install rest_framework
python3 -m pipenv install djangorestframework
### install mysqlclient 
python3 -m pipenv install myslqclient
### install djoser 
python3 -m pipenv install djoser


## my SQL details - 
username - admindjango <br />
databasename - littlelemon <br />
password - employee@123! <br />
Port - 3306 <br />
HOST - 127.0.0.1 <br />

# super user login details
  username - admin <br />
  password  - admin@123! <br />

# UI & APIs
  **Home Page** - http://127.0.0.1:8000/ <br />
  **About Page** - http://127.0.0.1:8000/about/ <br />
  **Menu Page** - http://127.0.0.1:8000/menu/ <br />
  **Book table page for user** - http://127.0.0.1:8000/book/ <br />
  **All - Reservation detail page** - http://127.0.0.1:8000/reservations/ <br />
  **ALL Menu API to get all menu permission to authenticated user only can use GET, POST Method*** - http://127.0.0.1:8000/api/menu-items/ <br />
  **Single Menu Item API permission for autheniticated user for PUT, PATCH, DELETE** - http://127.0.0.1:8000/api/bookings/1 <br />
  **ALL Booking API permission for autheniticated user for GET, POST Method** - http://127.0.0.1:8000/api/bookings/ <br />
  **Single Booking API permission for autheniticated user for PUT, PATCH, DELETE** - http://127.0.0.1:8000/api/bookings/1 <br />
  **List of All users Add new user, Edit existing user** - http://127.0.0.1:8000/auth/users/ <br />
  **Current User** - http://127.0.0.1:8000/auth/users/me/  <br />
  **Generate Token by provding user credential** - http://127.0.0.1:8000/auth/token/login/ <br />

# Test Details
  **test_create_item (file - test_model.py)**  to test the Menu model Run OK  <br />
  **BookingTest(file - test_model.py)** - to check the booking Model Run Ok  <br />
  **MenuItemSerializerTestCase(file - test_serializers.py)** - check if serializer data display correctly  <br />
  **test_menu_serializer_update(file - test_serializers.py)** - check if serializer data updated correctly  <br />

  
