# Hands-on Flask-01-02 : Creating First Flask Application - Hello World and basic usage of Jinja Templates

Purpose of the this hands-on training is to give the students quick introductory knowledge of how to create a Flask web application on local.

## Learning Outcomes

At the end of the this hands-on training, students will be able to;

- understand client-server software architecture.

- get familiar with Python Flask framework.

- install Python and Flask framework on local

- build a simple web application with Python Flask framework.

- use git repo to manage the application versioning.

- run the web application on AWS EC2 instance using the GitHub repo as codebase (will be shown by instructor).

## Outline

- Part 1 - Getting to know the Python Flask framework

- Part 2 - Write a Simple Hello World Web Application on GitHub Repo

- Part 3 - Write a Simple Hello World Web Application with Jinja template on GitHub Repo

- Part 4 - Install Python and Flask framework on Amazon Linux 2 EC2 Instance

## Part 1 - Getting to know the Python Flask framework

![Flask](./flask.png)

Flask is a web application development framework written in Python. It is a micro-framework that provides only the essential components which makes it easier to begin with when compared to full-stack frameworks like Django which has boilerplate code and dependencies.
And yet, Flask provides libraries, tools, and modules to develop web applications with additional features like authentication, database ORM, etc.

Followings are some of features of Flask Framework;

- It provides a development server and a debugger.

- It uses Jinja2 as templating engine.

- It is compliant with WSGI 1.0.

- It provides integrated support for unit testing.

- Many extensions are available to enhance its functionalities.


## Part 2 - Write a Simple Hello World Web Application on GitHub Repo

- Create folder named `flask-01-02-hello-world-app-Jinja-Template` within your repo under `python/hands-on` folder and go under it.

- Create folder named `flask-01-hello-world-app`

- Create python file named `hello-world-app.py`

- Import Flask module.

- Create an object named `app` from imported Flask module.

- Create a function `hello` which returns a string `Hello World`.

- Assign a URL route the `hello` function with decorator `@app.route('/')`.

- Create a function `second` which returns a string `This is the second page` and assign a URL route the `second` function with decorator `@app.route('/second')`. 

- Create a function `third` which returns a string `This is the subpage of third page` and assign a URL route the `third` function with decorator `@app.route('/third/subthird')`. 

- Create a dynamic url which takes id number dynamically and return with a massage which show id of page.

- run the application in debug mode

- Connect the Hello World application from the web browser with `localhost:5000` or `127.0.0.1:5000`

- to reach application from anywhere on port 80, change debug mode

- Save the complete code as `hello-world-app.py` file under `hands-on/flask-01-02-hello-world-app-Jinja-Template/flask-01-hello-world-app` folder.

- Add and commit all changes on local repo

- Push `hello-world-app.py` to your remote repo


## Part 3 - Write a Simple Hello World Web Application with Jinja template on GitHub Repo

- Create folder named `flask-02-Jinja_Template` within your repo under `python/hands-on` and go under it

- Create python file named `jinja.py`

- Import Flask and render_template modules.

- Create an object named `app` from imported Flask module.

- Create an `index.html` file under templates folder.

- Create a function named `head` which sends number `number1` and `number2` variables to the `index.html`. Use these variables into the `index.html` file. Assign a URL route the `head` function with decorator `@app.route('/')`.

- Create an `body.html` file under templates folder.

- Create a function named `number` which sends number `num1` and `num2` and sum of them to the `index.html`. Use these variables into the `body.html` file. Assign a URL route the `number` function with decorator `@app.route('/sum')`.

- run the application in debug mode

- Connect the Hello World application from the web browser with `localhost:5000` or `127.0.0.1:5000`

- Save the complete code as `jinja.py` file under `flask-02-Jinja_Template` folder.

- Add and commit all changes on local repo

- Push all files to your remote repo on GitHub.

## Part 4 - Run the Hello World App on EC2 Instance

- Launch an Amazon EC2 instance using the Amazon Linux 2 AMI with security group allowing SSH (Port 22) and HTTP (Port 80) connections.

- Connect to your instance with SSH.

- Update the installed packages and package cache on your instance.

- install git and wget

- Download the web application file from GitHub repo.

- Run the web application

- Connect the Hello World application from the web browser

- Connect the Hello World application from the terminal with `curl` command.
