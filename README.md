# Django CRM (Customer Relationship Management) Application

This is a simple CRM (Customer Relationship Management) web application built using Django. It allows users to manage customer records, including creating, updating, viewing, and deleting customer information.

## Features

- User authentication: Users can register, log in, and log out.
- Dashboard: Each user has a personalized dashboard displaying their customer records.
- Customer Records: Users can perform CRUD (Create, Read, Update, Delete) operations on customer records.
- Access Control: Users can only manage their own customer records.

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/your-username/django-crm.git
   ```

2. Create and activate a virtual environment (optional but recommended):

   ```bash
   python -m venv venv
   source venv/bin/activate
   ```

3. Install project dependencies:

   ```bash
   pip install -r requirements.txt
   ```

4. Apply database migrations:

   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

5. Create a superuser (admin) account to access the admin panel:

   ```bash
   python manage.py createsuperuser
   ```

6. Start the development server:

   ```bash
   python manage.py runserver
   ```

7. Access the application at `http://localhost:8000` in your web browser.

## Usage

1. Register a new user account or log in with an existing account.
2. Once logged in, you'll be directed to your personalized dashboard.
3. Use the navigation links to create, view, update, or delete customer records.
4. Log out when done.

## Contributing

Contributions are welcome! If you'd like to contribute to this project, please follow these steps:

1. Fork the repository.
2. Create a new branch for your feature or bug fix: `git checkout -b feature-name`
3. Make your changes and commit them: `git commit -m 'Add feature-name'`
4. Push to your forked repository: `git push origin feature-name`
5. Create a pull request on the original repository.
