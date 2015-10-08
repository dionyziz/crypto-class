"""
This module loads graders.py from all installed applications.
This way the graders on exercises get autodiscovered.
"""
from django.conf import settings
from importlib import import_module

def autodiscover():
    for app in settings.INSTALLED_APPS:
        try:
            print 'trying', app
            import_module('%s.graders' % (app,))
            print 'imported graders from', app
            import_module('%s.generators' % (app,))
            print 'imported generators from', app
        except ImportError, e:
            print 'error', e
            continue

graders = {}

def register_grader(tag, grader_function):
    graders[tag] = grader_function

def get_grader(tag):
    return graders[tag]

generators = {}

def register_generator(tag, generator_class):
    generators[tag] = generator_class

def get_generator(tag):
    return generators[tag]

# needs to be last line in the file
autodiscover()
