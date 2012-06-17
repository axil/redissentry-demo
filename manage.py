#!/usr/bin/env python
from django.core.management import execute_manager
import imp
try:
    imp.find_module('settings') # Assumed to be in the same directory.
except ImportError:
    import sys
    sys.stderr.write("Error: Can't find the file 'settings.py' in the directory containing %r. It appears you've customized things.\nYou'll have to run django-admin.py, passing it your settings module.\n" % __file__)
    sys.exit(1)

import settings

from sys import argv
if len(argv)>1:
    from os import environ
    if argv[1]=='runserver':
        environ['DJANGO_RUNSERVER'] = ''
    elif argv[1]=='runfcgi':
        environ['DJANGO_RUNFCGI'] = ''
    elif argv[1]=='sqlevolve':
        try:
            import deseb                        ##
        except:
            pass

if __name__ == "__main__":
    execute_manager(settings)
