# About the project

djangopizza is a Django application that allows users to store information about different types of pizzas. It also contains an API interface to handle different transactions.

---

### Technology stack

Python Django, SQLite 3, Django Rest Framework and Django filters.

---

### Description and features

### General functionality

- CRUD operations on different sizes the pizzas are available in.
- CRUD operations on different toppings a pizza can have.
- CRUD operations on different pizzas that are added in the database.

### The general page breakdown is as follows:

### API Pages

- API Root
    - api_baseURL = http://localhost:8000/
- Size List (URL: `api_baseURL/api/size/`)
    - List of sizes the pizzas are availabe in
    - Request types allowed - *GET*, *POST*
- Size Instance (URL: `api_baseURL/api/size/<id>/`)
    - Details of size instance
    - Request types allowed - *GET*, *PUT*, *DELETE*
- Topping List (URL: `api_baseURL/api/topping/`)
    - List of toppings available for pizzas
    - Request types allowed - *GET*, *POST*
- Topping Instance (URL: `api_baseURL/api/topping/<id>/`)
    - Details of size instance
    - Request types allowed - *GET*, *PUT*, *DELETE*
- Pizza List (URL: `api_baseURL/api/pizza/`)
    - List of all the pizzas added
    - Request types allowed - *GET*, *POST*
    - Allows filtering on `size` and `type` fields of the pizza.
    - In that case the non-mandatory query parameters are appended to the URL resulting in `api_baseURL/api/pizza/?size={size_value}&type={type_value}`
- Pizza Instance (URL: `api_baseURL/api/pizza/<id>/`)
    - Details of size instance
    - Request types allowed - *GET*, *PUT*, *DELETE*

---
### Steps to run the application

### 1: Create virtual environment

1. Create a top level (1) folder called 'Pizza'
2. Create a second level (2) folder called 'djangopizzaproject' and download this repository code into this folder
3. Open a command promt terminal and navigate to 'Pizza' folder
4. To set up a virtual environment, run `python -m venv <virtual_environment_name>`

### 2: Activate virtual environment and install dependencies

1. Navigate(cd) to the top level (1) 'Pizza' folder and run `<virtual_environment_name\Scripts\activate>`
2. Install dependencies by moving (cd) into the 'djangopizzaproject' folder and running `pip install -r 'requirements.txt'`

### 3: Initialise the database

- Run `python ./manage.py syncdb` to create the DDL statements
- Run `python ./manage.py migrate` to execute the DDl statements and create the required models

### 4: Run Django server

- Run `python manage.py runserver`

### 5: View application

- Open up `http://localhost:8000/` in your browser

---

### Application Structure

- `pizzaproject/` where key settings are specified
  - `settings/` where all the key settings have been specified
  - `urls/` handles application routing
- `djangopizza/` for the application
  - `migrations/` for all the database migrations
  - `models.py` for all the database table models
  - `views.py` for key views and related data
  - `serializers.py` for api serializer definiton and related data
- `db.sqlite3` database

---
