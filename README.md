# Brain-Farts
## Web application to input brainfarts into a database
#### Coded by Evert Rot

### Project purpose

The purpose of this app is to be able to make a digital note of an idea wherever I am.

Brain-farts can contain any or all of these content formats:

- Text
- Image
- Audio
- Link

The type of a brain-fart is defined by the active tab the moment you submit it.

So when the audio input tab is opened when you submit, the brain-fart's type will be `audio`

The list of brain-farts on the main page can be filtered by their format and their tags:

- Category
- Subject
- Project

### UX

The UX has been designed with as less text as possible, by creating an intuitive icon based interface.

When creating a new brain-fart its tags can be selected from a dropdown, or via autocomplete while you type. If it's a new tag you can click `Create <tag>` to create and store it in the database instantly.


### Deployment instructions:

#### Create a new repository
- Clone the repository to a new local folder:
    - ``` git clone https://github.com/Evert-R/brain-farts ```

#### Environment variables
- In the root folder create a new file named: ```env.py```

- Generate a secret key here: [Django secret key generator](https://miniwebtool.com/django-secret-key-generator/)

- Put the following code in the file:
          
      import os

      os.environ["SECRET_KEY"] = "<Django secret key>"
      os.environ['DEVELOPMENT'] = "1"

      os.environ["ALLOWED_HOSTS"] = "localhost,<your_domain>"

      os.environ["POSTGRESQL_NAME"] = "<database name>"
      os.environ["POSTGRESQL_USER"] = "<database user>"
      os.environ["POSTGRESQL_PASS"] = "<database password>"

- Add this file to the ```.gitignore``` file

#### Create a virtual environment for python

  These commands may differ slightly depending on which operating system and IDE you are using. I used VScode on debian bookworm.

- To create a virtual environment enter from the terminal in you IDE: 
    - ```python -m .venv env```
- Now activate the virtual environment
    - ```.env\Scripts\activate```
- Install the requirements
    - ```pip -r requirements.txt```
- Migrate the database
  - ```python manage.py migrate```
- Create superuser
  - ```python manage.py createsuperuser```
    - You will be prompted for your username, password and email
- Start the app
    - ```python manage.py runserver localhost:8080```
- Login with your username and password using a browser:
    - ```http://127.0.0.1:8000/admin/```

#### Create a postgresql database

```sudo -u postgres psql```

```CREATE DATABASE <database_name>;```

```CREATE USER <database_user> WITH PASSWORD '<your_password>';```

```ALTER ROLE <database_user> SET client_encoding TO 'utf8';```

```ALTER ROLE <database_user> SET default_transaction_isolation TO 'read committed';```

```ALTER ROLE <database_user> SET timezone TO 'UTC';```

```GRANT ALL PRIVILEGES ON DATABASE <database_name> TO <database_user>;```

```ALTER DATABASE <database_name> OWNER TO <database_user>;```

```\c <database_name>;```

```GRANT USAGE ON SCHEMA public TO <database_user>;```

```GRANT ALL PRIVILEGES ON ALL TABLES IN SCHEMA public TO <database_user>;```

```GRANT ALL PRIVILEGES ON ALL SEQUENCES IN SCHEMA public TO <database_user>;```

```\q```

#### Setup gunicorn

```sudo nano /etc/systemd/system/<project_name>.socket```

```
    [Unit]
    Description=gunicorn socket

    [Socket]
    ListenStream=/run/<project_name>.sock

    [Install]
    WantedBy=sockets.target
```

```sudo nano /etc/systemd/system/<project_name>.service```

```
    [Unit]
    Description=gunicorn daemon
    Requires=<project_name>.socket
    After=network.target

    [Service]
    User=<os_username>
    Group=www-data
    WorkingDirectory=/<path_to_project>/<project_name>
    ExecStart=/<path_to_project>/env/bin/gunicorn \
            --access-logfile - \
            --workers 3 \
            --bind unix:/run/<project_name>.sock \
            core.wsgi:application

    [Install]
    WantedBy=multi-user.target
```

Make sure the `os_username` is added to the `www-data` group.

#### Setup nginx

```sudo nano /etc/nginx/sites-available/<project_name>```

```
    server {
        listen 80;
        server_name <server_name>;

        location = /favicon.ico { access_log off; log_not_found off; }
        location /static/ {
            root /<path_to_project>/<project_name>;
        }

        location /media/ {
            autoindex on;
            alias /<path_to_project>/<project_name>/media;
        }

        location / {
            include proxy_params;
            proxy_pass http://unix:/run/<project_name>.sock;
        }
    }
```

```sudo ln -s /etc/nginx/sites-available/<project_name> /etc/nginx/sites-enabled```

```sudo systemctl daemon-reload```

```sudo systemctl restart <project_name>.socket <project_name>.service```

```sudo systemctl restart nginx```

### Databse management

#### Backup the database

```sudo pg_dump -U <database_user> -h localhost -d <database_name> -f backup.sql```

#### Restore the database

```sudo dropdb -U <database_user> -h localhost <database_name>```

Create the new database as described above.

```psql -U <database_user> -h localhost -d <database_name> -f debian.sql```

## Technologies Used
- [VSCode](https://code.visualstudio.com)
  - Code Editor
- [Python 3.11.2](https://www.python.org)
  - Program language
- [Django 4.2](https://www.djangoproject.com)
  - Web framework
- [django-autocomplete-light 3.11.0](https://django-autocomplete-light.readthedocs.io/en/master)
  - Autocomplete function for the tags.
- [Bootstrap 5.1.3](https://getbootstrap.com/)
  - Grid layout, navigation bar & card columns
- [Jquery 3.6.0](https://jquery.com/)
  - DOM manipulation
- [Font awesome 6.1.1](https://fontawesome.com/)
  - Icon library
- [Crispy forms 1.14.0](https://django-crispy-forms.readthedocs.io/)
  - Custom form rendering in Django
- [psycopg2](https://pypi.org/project/psycopg2)
  - Connnect to progresql database
- [Gunicorn](https://gunicorn.org)
  - Run django app the server
- [Django secret key generator](https://miniwebtool.com/django-secret-key-generator/)
  - Generate secret key 
