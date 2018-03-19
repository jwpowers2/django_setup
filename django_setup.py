#!/usr/bin/python

# use argparse to take an app name(s) and create a django skeleton from that

# for linux only with v1
# start in directory where you want your django project
import os

os.system('django-admin startproject {}'.format(projectname))

os.system('cd {}'.format(projectname'))

os.system('mkdir apps')

os.system('cd apps')

os.system('touch __init__.py')

os.system('python ../manage.py startapp {}'.format(appname))

# mod settings.py to include our app as an installed app

settingsfile = '../{}/projectname/settings.py'.format(projectname)

with open(settingsfile, r) as file:
    filedata = file.read()
    filedata = filedata.replace("INSTALLED_APPS = ['django.contrib.admin','django.contrib.auth','django.contrib.contenttypes','django.contrib.sessions','django.contrib.messages','django.contrib.staticfiles',]","INSTALLED_APPS = ['apps.{}','django.contrib.admin','django.contrib.auth','django.contrib.contenttypes','django.contrib.sessions','django.contrib.messages','django.contrib.staticfiles',]".format('appname')

with open(settingsfile, 'w') as file:
    file.write(filedata)


# mod primary urls.py to include our app
# can just delete the generated one and make a new one with our copy
# whack main urls.py and push line by line to it


# create urls.py in the application and give it canned content

# create a canned index view

# build templates and statics in the app

# activate session if that flag is set in the argparse 




