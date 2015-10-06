FROM django:python2-onbuild

CMD /bin/sh -c "python manage.py migrate && python manage.py runserver 0.0.0.0:8000"
