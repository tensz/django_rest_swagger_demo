FROM ubuntu

RUN sed -i "s/archive.ubuntu.com/cn.archive.ubuntu.com/g" /etc/apt/sources.list
RUN apt-get update -y
RUN apt-get install -y python-pip python-dev build-essential nginx

COPY . /opt
WORKDIR /opt

RUN mkdir -p logs/nginx
RUN mkdir -p logs/uwsgi

RUN cat ngixn.conf >> /etc/nginx/nginx.conf
RUN pip install -r requirements.txt

RUN python manage.py migrate
RUN python manage.py collectstatic

EXPOSE 8000
CMD ["uwsgi", "-x", "uwsgi.xml"]
