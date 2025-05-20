# Employer Management System

A Django-based RESTful API application for managing employer information with custom user authentication using Django REST Framework (DRF) and Simple JWT.


## Overview

The Employer Management System is designed to provide a robust API for managing employer details. It features custom user authentication with email and password login, token-based authentication using Simple JWT, and CRUD operations for employers. Each employer is associated with a user.

## Features

- **Custom User Authentication**:
  - Register new users with email and password.
  - Login to generate JWT tokens (access and refresh).
  - Retrieve the current user's profile.
- **Employer Management**:
  - Create, list, retrieve, update, and delete employer records.
  - Only the owner of the employer record has permission to get list, create, update and delete.
  - Employers are linked to users (one user can have multiple employers).
- **API Endpoints**:
  - `POST /api/auth/signup/` - Register a new user.
  - `POST /api/auth/login/` - Login and get JWT tokens.
  - `GET /api/auth/profile/` - Get logged-in user's profile.
  - `POST /api/employers/` - Create an employer.
  - `GET /api/employers/` - List all employers for the logged-in user.
  - `GET /api/employers/<id>/` - Retrieve a specific employer.
  - `PUT /api/employers/<id>/` - Update a specific employer.
  - `DELETE /api/employers/<id>/` - Delete a specific employer.

## Project Structure

```
EmployerManagement/                  
├── accounts/             
│   ├── __init__.py
│   ├── models.py         
│   ├── serializers.py   
│   ├── urls.py
│   └── views.py         
├── employer/              
│   ├── __init__.py
│   ├── models.py      
│   ├── permissions.py   
│   ├── serializers.py   
│   ├── urls.py
│   └── views.py          
├── EmployerManagement/    
│   ├── __init__.py
│   ├── settings.py
│   ├── urls.py
├── .gitignore            
├── LICENSE               
├── manage.py            
├── README.md            
└── requirements.txt      
```


## Prerequisites

- Python 3.12.3
- pip (Python package manager)
- Virtualenv 

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/imsnto/EmployerManagement.git
   cd EmployerManagement
   ```

2. Create and activate a virtual environment:
   ```bash
   python -m venv .venv
   source .venv/bin/activate  # On Windows: .venv\Scripts\activate
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Apply migrations:
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

5. Create a superuser for admin access:
   ```bash
   python manage.py createsuperuser
   ```

6. Run the development server:
   ```bash
   python manage.py runserver
   ```
   
## Usage

- **Authentication**:
  - Register a user via `POST /api/auth/signup/` with 
  ``` 
   { 
      "first_name": "<your-first-name>", 
      "last_name": "<your-last-name>", 
      "email": "<user@example.com>", 
      "password": "<your-password>", 
      "password2": "<your-password>" 
   }
  ```
  - Login via `POST /api/auth/login/` to get JWT tokens: 
  ```
    { 
        "email": "<your-email>", 
        "password": "<password>" 
    }
  ```
  - Use the access token in the `Authorization` header (e.g., `Bearer <token>`) for protected endpoints.
  - Retrieve profile via `GET /api/auth/profile/`.
- **Employer Management**:
  - Create an employer via `POST /api/employers/` with 
  ```
  {
    "contact_person_name": "<name>",
    "company_name": "<your-comapny-name>",
    "email": "<your-email>",
    "phone_number": "<your-phone>",
    "address": "<your-address>"
  }
  ```
  - List employers via `GET /api/employers/`.
  - Retrieve, update, or delete an employer via `GET`, `PUT`, or `DELETE /api/employers/<id>/`.

## Authentication

- Uses a custom User model extending `AbstractBaseUser` and `PermissionsMixin`.
- Token-based authentication with `djangorestframework-simplejwt`.
- All `/employers/` endpoints require authentication and restrict access to the logged-in user's employers.