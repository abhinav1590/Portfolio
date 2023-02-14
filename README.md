# Personal Portfolio

This is a portfolio website built using Django Framework, where users can view my professional experience, education, and projects.

Technologies Used
-----------------

-   Python 3.9.5
-   Django 3.2.4
-   HTML5
-   CSS3

Features
--------

-   Home page with an introduction and links to other sections of the website
-   About Me page with a brief overview of my professional experience and education
-   Projects page with a list of my past projects, including descriptions, technologies used, and links to GitHub repositories
-   Contact page with a form to submit inquiries and feedback
-   Admin panel for managing the website content

Installation
------------

1.  Clone the repository: `git clone https://github.com/abhinav1590/Portfolio.git`
2.  Install the required packages: `pip install -r requirements.txt`
3.  Apply the database migrations: `python manage.py migrate`
4.  Create a superuser for the admin panel: `python manage.py createsuperuser`
5.  Run the development server: `python manage.py runserver`

Usage
-----

1.  Navigate to <http://localhost:8000/> in your web browser to view the website
2.  Use the navigation bar to access different sections of the website
3.  To access the admin panel, navigate to <http://localhost:8000/admin/> and log in with your superuser account

Deployment
----------

To deploy the website to a production environment, follow these steps:

1.  Set the `DEBUG` setting to `False` in `settings.py`
2.  Configure your web server to serve the Django application
3.  Set up a production email backend, such as SMTP or SendGrid, and update the `EMAIL_BACKEND` and `EMAIL_*` settings in `settings.py`
4.  Collect the static files: `python manage.py collectstatic`
5.  Set up a process manager, such as systemd or Supervisor, to run the Django application as a daemon

Credits
-------

-   The code for the contact form was adapted from the Django documentation
-   The project descriptions and technologies used were based on my personal projects