# DRF_PG
Django REST Framework, Postgres

1. Create a new virtual environment
    python -m venv envName

2. Create new django project
    django-admin startproject projectName .
    use "." to create project in current dir.

3. Create a decent folder structure
    --Project
        -- ProjectName
            -- settings
                -- base.py
                -- dev.py
            -- urls.py
            -- asgi.py
            -- wsgi.py
        -- Apps
            -- AppName1
                -- models.py
                -- serializers.py
                -- views.py
                -- urls.py
            -- AppName2
                -- models.py
                -- serializers.py
                -- views.py
                -- urls.py
            -- utils.py
        -- manage.py
        -- requirement.txt
        -- .gitignore
        -- .dockerignore
        -- Dockerfile
        -- Jenkinsfile
        -- .env

4. Start project
    python manage.py runserver

5. Create Applications in app folder
    cd apps
    python manage.py startapp AppName3

6. add new app to the INSTALLED_APPS list in the project settings.py file
    INSTALLED_APPS = [
        #...
        apps.AppName3
    ]

7. Inside AppName3 folder create 2 new files as serializers.py and url.py
    The serializers.py file is used to define serializers for your Django models. Serializers allow to convert Django models into JSON or other content types. They are use to validate the data.
    The urls.py file is used to define the URL patterns for your Django app. It specifies how URLs should be mapped to views or other URL patterns within the app.

8 Connect PostgresSQL to Project
    DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'databaseName',
        'USER': 'databaseUser',
        'PASSWORD': 'databasePassword',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}