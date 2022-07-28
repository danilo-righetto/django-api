# SUMMARY

- [PROJECT INTRODUCTION](#project-introduction)
- [MAIN PROJECT TECHNOLOGIES](#main-project-technologies)
- [MAIN LIBRARIES](#main-libraries)
- [ORGANIZATION OF THE PROJECT DIRECTORY STRUCTURE](#organization-of-the-project-directory-structure)
- [SETUP LOCAL](#setup-local)
- [HOW TO RUN LOCAL TEST](#how-to-run-local-test)
- [DEPLOY](#deploy)
- [APPLICATION ENVIRONMENTS LINKS](#application-environments-links)
- [ENVIRONMENT VARIABLES](#environment-variables)
- [BUSINESS RULES AND REQUIREMENTS](#business-rules-and-requirements)
- [CACHE RULES](#cache-rules)
- [TROUBLESHOOTING](#troubleshooting)
- [CHANGELOG](#changelog)
- [USEFUL REFERENCES AND LINKS](#useful-references-and-links)


# PROJECT INTRODUCTION

The "django-api" project aims to document the learning in developing API's using Django.


## WHAT IS THE FINAL GOAL OF THE PRODUCT?

The project aims to demonstrate the mastery of using Django to create APIs, in addition to other resources.
   
## WHO ARE THE END USERS?

The end users of this project are the developers (students) of the communities: Django and Python.


# MAIN PROJECT TECHNOLOGIES

* [Django 3.2](https://docs.djangoproject.com/en/3.2/releases/3.2/)

* [Postgres 13.2](https://www.postgresql.org/docs/13/release-13-2.html)


# MAIN LIBRARIES

- [django-cors-headers 3.7.0](https://pypi.org/project/django-cors-headers/3.7.0/)

- [django-environ 0.4.5](https://pypi.org/project/django-environ/0.4.5/)

- [djangorestframework 3.12.4](https://pypi.org/project/djangorestframework/3.12.4/)

- [drf-yasg 1.20.0](https://pypi.org/project/drf-yasg/1.20.0/)

- [pylint 2.8.3](https://pypi.org/project/pylint/2.8.3/)

- [coverage 5.5](https://pypi.org/project/coverage/5.5/)

- [botocore 1.20.84](https://pypi.org/project/botocore/1.20.84/)


# ORGANIZATION OF THE PROJECT DIRECTORY STRUCTURE

```
django-api
|----- developing tree
```



<details>
  <summary>apps</summary>

`contains all Django apps.`

Each app can contain:
- api: module that exposes the models API
- migrations: all migrations in the module
- fixtures: standard data that must be entered in all installations
- tests: all app tests


  <details>
    <summary>apps > base</summary>

    `The base APP contains all the code that must be generic between apps`

  </details>
  <details>
    <summary>apps > galleries</summary>

    `The galleries APP implements the entire context aimed at managing photo galleries.`

  </details>
  <details>
    <summary>apps > heroes</summary>

    `The heroes APP implements the entire context facing the hero management of the laborit website.`

  </details>
  <details>
    <summary>apps > leads</summary>

    `The leads APP implements the entire context aimed at managing leads`

  </details>
  <details>
    <summary>apps > newsletter</summary>

    `The newsletter APP implements the entire context aimed at managing newsletter subscriptions`

  </details>
  <details>
    <summary>apps > segment</summary>

    `The segments APP implements the entire context aimed at the management of Laborit's operating segments`

  </details>
  <details>
    <summary>apps > stories</summary>

    `The stories APP implements the entire context aimed at managing stories related to Laborit`

  </details>
  <details>
    <summary>apps > users</summary>

    `The users APP rewrites the base user of the django system bringing product features.`

  </details>
</details>

<details>
  <summary>laborit_inc</summary>

  `Django Project`

</details>

# SETUP LOCAL

**First of all, make sure you are at the root of the project.**

First create and edit the `.env` file with the following command:

```sh
  $ cp .env.example .env
```

Start the containers by running the command:

```sh
  $ docker-compose up -d
```

Run all migrations:

```sh
  $ docker exec -t django-server python3.7 manage.py migrate 
```

Load all default data into base:

```sh
  $ docker exec -t django-server python3.7 manage.py loaddata apps/**/fixtures/**.json 
```

Access `localhost:8000/swagger` or `localhost:8000/admin`


# HOW TO RUN LOCAL TEST

We use [pytest](https://docs.pytest.org/en/6.2.x/contents.html) to perform unit and application integration tests.

You can run the test suite running:

```sh
  $ docker exec -t django-server python3.7 manage.py test
```

## CODE COVERAGE

Code coverage is generated with the following command:

```sh
  $ docker exec -t django-server coverage run manage.py test
```

Now run the following command to export in HTML:

```sh
  $ docker exec -t django-server coverage html
```

You can view the artifacts at: `htmlcov`

# DEPLOY

N/A

## PIPES

> Example:

It is very important to consider that we use two tools to support the project's code quality.

The first is pylint, which will validate all PEP8 rules that are geared towards Python code-style standards.

Run the following command to validate your branch before confirming:

```sh
  $ docker exec -t django-server pylint --load-plugins pylint_django --django-settings-module=laborit_inc.settings ./*
```

The second is pytest that has already been submitted.


# APPLICATION ENVIRONMENTS LINKS

N/A

# ENVIRONMENT VARIABLES

- DJANGO_DEBUG: Define se o Django vai rodar no modo debug
- DJANGO_SECRET_KEY: Define o salt que será utilizado em dados sensiveis
- DJANGO_DEFAULT_LANGUAGE: Define o idioma em que o Django vai rodar
- DJANGO_TIME_ZONE: Define qual timezone o Django deve usar
- DJANGO_USE_I18N: Define se o Django deve utilziar traduções
- DJANGO_USE_L10N: Define se o Django deve utilziar localizações
- DJANGO_USE_TZ: Define
- DJANGO_LOG_LEVEL: Define o level do log que o Django deve emitir 
- REST_PAGE_SIZE: Define a quantidade padrão de itens nas listagens dos recursos da API
- CLIENT_URL: Define o endereço http do client do Site Laborit
- DEV_CLIENT_LOCAL_DOMAIN: Define o endereço dos devs para liberar no cors
- API_DOMAIN: Define o dominio da API para liberar no Django
- ADMIN_DOMAIN: Define o dominio do admin para liberar no Django
- LOCAL_DOMAIN: Define o dominio do localhost para liberar no Django

# BUSINESS RULES AND REQUIREMENTS

N\A

# CACHE RULES

N\A

# TROUBLESHOOTING

Workaround solutions

N\A

# CHANGELOG

The Changelog with the change events is available in the `CHANGELOG.md` file at the root of the project.

# USEFUL REFERENCES AND LINKS

- [Sentry Doc](https://docs.sentry.io/platforms/dotnet/aspnetcore/)

- [Test Pattern AAA](https://medium.com/@pjbgf/title-testing-code-ocd-and-the-aaa-pattern-df453975ab80)

- [Semantic Versioning](https://semver.org/)

- [Keep a CHANGELOG](https://keepachangelog.com/en/1.0.0/)

- [Django Permissions](https://www.django-rest-framework.org/api-guide/permissions/)
  
- [Django database API](https://docs.djangoproject.com/en/3.2/topics/db/queries/)
  
- [Django faker](https://faker.readthedocs.io/en/master/fakerclass.html)
  
- [Django doc](https://docs.djangoproject.com/en/3.2/)
  
- [Django Rest Framework](https://www.django-rest-framework.org/)
  
- [Django cors](https://pypi.org/project/django-cors-headers/)