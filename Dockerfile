FROM python:3.9.12

WORKDIR /home/

RUN git clone https://github.com/OXcarXierra/django_tutorial.git

WORKDIR /home/pinterest_clone/

RUN pip install -r requirements.txt

RUN echo "SECRET_KEY=!ln)^%b7rbuss)t$1qx9o#z&4af@jt^iw82+xjw5ac5-(8(^jc" > .env

RUN python manage.py migrate

EXPOSE 8000

CMD ["python","manage.py","runserver","0.0.0.0:8000"]