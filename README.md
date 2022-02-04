# Django Junraider

Example Django project from Zinglecode's YouTube Django Ep.1 (Thai language)

## YouTube video

- YouTube link coming soon

## Install Python 3 and pipenv

1. Download Python 3 installation file from https://www.python.org/

2. Install pipenv as global package by this command.

```
pip install pipenv
```

Note: macOS with pre-installed Python 2, use pip3 instead of pip.
Note: to use pipenv on Windows, Some additional steps maybe required. Please read here ...link...

## Install MySQL and MySQLWorkbench

Please install MySQL + MySQL Workbench. And then create your database for using with this Django project.

- macOS -> YouTube
- Windows -> Facebook

## Install and Run project by VSCode

1. Download this project

2. Open folder project in VSCode

3. Open project_jrd/.env.sample file, rename to .env, and change configuration

4. Open VSCode Terminal

5. Install packages by below command

```
pipenv install
```

6. Activate pipenv environment by below command

```
pipenv shell
```

7. Run migrations

```
python manage.py migrate
```

8. Run project

```
python manage.py runserver
```

