FROM ubuntu
RUN sed -i "s/archive.ubuntu.com/cn.archive.ubuntu.com/g" /etc/apt/sources.list
RUN apt-get update -y
RUN apt-get install -y python-pip python-dev build-essential
COPY . /opt
WORKDIR /opt
RUN mkdir logs
RUN pip install -r requirements.txt
RUN python manage.py migrate
EXPOSE 8000
CMD ["run", "python", "manage.py", "runserver", "0.0.0.0:8000"]
