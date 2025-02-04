# Django App

## Overview

A Django-based web application designed for inventory management.

## Features

- /inventory will display the list of inventories and their suppliers
    - can search inventory by name or supplier name
- /inventory/id to display inventory detail

## Requirements

- Python 3.10.x or later
- Django 5.x or later

## Installation

### 1. Clone the repository:

```
git clone https://github.com/fatjan/inventory
cd inventory
```

2. Create a virtual environment:
```
python -m venv venv
```

3. Activate the virtual environment:
```
source venv/bin/activate
```

4. Install dependencies
```
pip install -r requirements.txt
```

5. Set up environment variables:
Copy the .env.example and paste it as .env file, fill in the required fields

6. Run migrations
```
python manage.py migrate
```

7. Create a superuser (for admin access):
```
python manage.py createsuperuser
```
Follow the prompts to create an admin user for accessing the Django admin panel.

8. Run the development server:
```
python manage.py runserver
```

Your app will be accessible at http://127.0.0.1:8000/

9. Testing
To run tests for the app, use the following command:
```
python manage.py test
```

10. If any new package or dependency is installed, add it to the requirements.txt
```
pip freeze > requirements.txt
```