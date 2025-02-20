# Brain-Farts
## Web application to input brainfarts into a database
#### Coded by Evert Rot

### Project purpose

The purpose of this app is to be able to make a digital note of an idea wherever I am.

Brain-farts can contain any or all of these formats:
- Text
- Image
- Audio
- Link

### UX

The UX has been designed with as less text as possible, by creating a intuitive icon based interface.

### Deployment instructions:

##### Create a new repository
- Clone the repository to a new local folder:
    - ``` git clone https://github.com/Evert-R/brain-farts ```

##### Environment variables
- In the root folder create a new file named: ```env.py```
- Generate a secret key here: [Django secret key generator](https://miniwebtool.com/django-secret-key-generator/)
- Put the following code in the file:
          
      import os

      os.environ["SECRET_KEY"] = "<Django secret key>"
      os.environ['DEVELOPMENT'] = "1"

      os.environ["POSTGRESQL_NAME"] = "<database name>"
      os.environ["POSTGRESQL_USER"] = "<database user>"
      os.environ["POSTGRESQL_PASS"] = "<database password>"

- Add this file to the ```.gitignore``` file

The app will first look for this file to load the environment variables. If this file is not found it assumes that the environment variables are already present, as will be the case when we run the project on an external server. This hidden file is there to ensure our credentials are not exposed on github.

##### Virtual environment for python

  These commands may differ slightly depending on wich operating system en IDE you are using. I used VScode on windows

- To create a virtual environment enter from the terminal in you IDE: 
    - ```python -m .venv venv```
- Now activate the virtual environment
    - ```.venv\Scripts\activate```
- Install the requirements
    - ```pip -r requirements.txt```
- Migrate the database
  - ```python manage.py migrate```
- Create superuser
  - ```python manage.py createsuperuser```
    - You will be prompted for your username, password and email
- Start the app
    - ```python manage.py runserver```
- Create user groups
  - Go to ```http://127.0.0.1:8000/admin/```
  - Login with the account you just created
  - Go to ```Users```
  - Click on your account
  - Add your account to the admin group

## Technologies Used
- [VSCode](https://code.visualstudio.com)
  - Code Editor
- [Git bash](https://gitforwindows.org)
  - Version control from windows
- [Python 3.11.2](https://www.python.org)
  - Program language
- [Django 4.0](https://www.djangoproject.com)
  - Web framework
- [Bootstrap 4.4.1](https://getbootstrap.com/)
  - Grid layout, navigation bar & card columns
- [Jquery 3.6.0](https://jquery.com/)
  - DOM manipulation
- [Font awesome 6.1.1](https://fontawesome.com/)
  - Icon library
- [Crispy forms](https://django-crispy-forms.readthedocs.io/)
  - Custom form rendering in Django
- [psycopg2](https://pypi.org/project/psycopg2)
  - Connnect to progresql database
- [Gunicorn](https://gunicorn.org)
  - Run django app on Heroku server 
- [Django secret key generator](https://miniwebtool.com/django-secret-key-generator/)
  - Generate secret key 
