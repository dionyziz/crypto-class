FROM django:python2-onbuild

RUN apt-get -qy update && apt-get install -y gettext && rm -rf /var/lib/apt

CMD /bin/sh -c "python manage.py migrate && python manage.py runserver 0.0.0.0:8000"
