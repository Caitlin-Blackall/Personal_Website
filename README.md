# Personal Website

*IN PROGRESS - August 2023*

## Project Overview
To create a personal website to display my projects and also 
write blog posts about learning to code. I thought it would be nice 
to have a way to display my coding projects while also demonstrating 
my coding skills.

## Local Dev Set-Up
### Pre-Requisites:
+ [pip](https://pypi.org/project/pip/)
+ [venv](https://docs.python.org/3/library/venv.html)
+ [Git](https://git-scm.com/)

### Installations:
+ ```pip install Django```

### Database Set-Up:
The database is managed with SQLite via Django. The database and models have already 
been created using the following commands:
```python
python manage.py makemigrations
```
```python
python manage.py migrate
```

> __Note__: Migrations files can be found in `app/migrations`.

Models are subsequently managed using [Django Admin](https://docs.djangoproject.com/en/4.2/ref/contrib/admin/).

### Running the App
This project is currently run locally only. As such, in order to access the 
app, a local copy must be made first.

1. Enter the directory where the clone will be made.


2. ```git clone [enter SSH key here]```

Once a clone has been made, the app can be activated.

1. ```source venv/bin/activate```


2. ```python manage.py runserver```


The app will then be accessible on the local development server.

To close the app when finished, use ```^C``` followed by ```deactivate```.


## Development Process
I used Django to create the website, creating different apps for 
each of the webpages. Within each app, I used `views.py` and `urls.py`
to ensure web requests are received and the appropriate response / 
web page is returned. The url paths were also added to the
main `urls.py` section in the following format:
```python
URL PATTERNS: ['app/', include('app.urls')),]
```

I used Bootstrap to assist with the template design elements of the website, 
creating a `base.html` file containing the navigation bar. The file 
was then extended upon for each of the different web pages. I also 
used ```{{ value | linebreaksbr }}``` to ensure text was 
displayed in paragraphs for the blog detail, project detail
and 'About Me' sections. I also used ```{{ value | urlize }}``` 
to allow hyperlinking between sections of the website.

Media elements are saved in a `static` directory which allows them 
to be uploaded through [Django Admin](https://docs.djangoproject.com/en/4.2/ref/contrib/admin/)
and accessed on the relevant web page.

I used to built-in Object Relational Mapper (ORM) of Django with SQLite
to create models and manage these within a relational database. Within 
each app, `models.py` was used to store the models required and data was 
subsequently entered and managed using [Django Admin](https://docs.djangoproject.com/en/4.2/ref/contrib/admin/).

One of my sections also includes a lambda function through AWS.
Although this is not necessary for my website, it was another 
way for me to demonstrate skills that I have developed.

## Learning
### New Skills

**1. Learning Django**

It was nice to learn Django after having some experience with 
building FlaskApps. It seemed to be slightly more flexible in 
the way it works and I liked separating each model into 
different files. I found this much easier to keep track of all 
my code and track where I was up to.

**2. Using Bootstrap**

I have never used Bootstrap before but it was very easy to 
use and similar enough to CSS. It was a more flexible design 
process which was handy and I could make page layouts quickly 
and easily.

**3. Creating a lambda function using AWS**

I created a very basic function to get used to using 
cloud services.

## Future Work
The ultimate aim is to deploy this app in the cloud. I used 
AWS to create a basic lambda function and am currently expanding 
on those skills to be able to deploy this website soon.

## Conclusion
