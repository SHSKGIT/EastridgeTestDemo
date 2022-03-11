Please use source blob for better format view.

# EastridgeTestDemo
This is a Python3.9 Django4.0 project running in Docker containers (Nginx + Django + MySQL8.0)

Django project root folder: EastridgeTestDemo/webapp/
Django configuration files: EastridgeTestDemo/webapp/webapp/
Django settings file: EastridgeTestDemo/webapp/webapp/settings/prod.py
DJANGO_SETTINGS_MODULE in manage.py, wsgi.py, asgi.py should reference to prod.py:
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'webapp.settings.prod')

Please create settings/.env file and set your own sensitive info for using prod.py. 
(.env file is ignored by .gitignore file.)

MySQL is used. Please make sure your MySQL server location (IP and port) and access control.
You need to define sensitive info in .env for attributes in prod.py, such DATABASES, SECRET_KEY.

If you use venv, please install in the path of EastridgeTestDemo/webapp/
Install venv: python -m venv venv 
Navigate to venv/bin/ and activate it: source activate
(venv is not necessary when using Docker containers.)

Please use requirements/base.txt to install necessary Python libraries: pip install -r base.txt 
To generate all libraies the project is using: pip freeze > <file_name>

In this Django project, there is only one app called Logistics.
The root webapp/url.py includes Logistics/urls.py
There are 2 models at models/invoice.py: Invoice, InvoiceItem
There are 2 forms at forms/invoice.py: InvoiceForm, InvoiceItemForm
All Class-Based Views are defined in views/invoice.py
All html templates are defined in templates/Logistics/
migrations files are to keep models tracked. It's not doing anything to database until execute migrate.
For example:
python manage.py makemigrations Logistics
python manage.py migrate Logistics
(For 1st time to migrate, don't type app name, just migrate everything including Django built-in apps, so that all tables will be created in db. However, some built-in apps are not necessary.)

Naviagte to where manage.py is located.
python manage.py runserver
(You can also specify a port: python manage.py runserver 0:8080)
Go to a web browser and type url: localhost/logistics/home
(If using port 8080, type url: localhost:8080/logistics/home)
Before typing url, please check if the port is being used or not:
On Mac: netstat -an | grep LISTEN
On Linux: netstat -tulpn | grep LISTEN
If the port is being used, either change another port, or kill the current port (pid).

# Using Docker Containers
You will use docker-compose to build images.

Create docker-compose.yml file in EastridgeTestDemo/
There are 3 services, you can define alias such: db, web, nginx.
Put sensitive info into EastridgeTestDemo/webapp/webapp/settings/.env
.env file should look like this:
DATABASE_NAME=...
DATABASE_USER=... # this user will be created in mysql config
DATABASE_PASS=...
DATABASE_HOST=db   # the alias you defined in docker-compose.yml
DATABASE_PORT=3306  # default 3306, could be others
SECRET_KEY=...
MYSQL_DATABASE=...  # it must be the same as DATABASE_NAME
MYSQL_ROOT_PASSWORD=...
MYSQL_PASSWORD=... # it must be the same as DATABASE_PASS

Nginx and MySQL docker container configurations are in EastridgeTestDemo/compose/
Nothing remarkable in EastridgeTestDemo/compose/nginx/
In EastridgeTestDemo/compose/mysql, when creating a user, the way to create is quite different in MySQL8.0 compared to previous versions. It took me a bit time to figure it out...

EastridgeTestDemo/webapp/Dockerfile is to build web image.
uwsgi.ini is to initialize uwsgi server.
start.sh is to recap all commands for launching app.

Now, navigate to where docker-compose.yml is located, and execute:
docker-compose build
Images of Nginx and webapp are generated. MySQL image will be generated in the next step.
docker-compose up
check images: docker images -a
check containers: docker ps -a
The last but not the least, Nginx will route to uwsgi server, so you need to turn uwsgi server on:
docker exec -it <mysql_container_name> /bin/bash start.sh
OR 
get into container: docker exec -it <mysql_container_name> /bin/bash
and execute start.sh: source start.sh

Now refresh the web page and see everything working well.

\*^*/

Youtube screen records:
Without Docker: 
https://youtu.be/qNfgAGF_-j0
With Docker: 
https://youtu.be/Mb_YFAAxy4s
Fixed date picker widget in docker:
https://youtu.be/093C-ZYON5s