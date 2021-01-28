FROM python:3.7.2

RUN pip install pipenv

COPY . /flask-app

WORKDIR /flask-app

RUN pip install gunicorn[gevent]

RUN pip install -r requirements.txt

EXPOSE 5000

CMD gunicorn --worker-class gevent --workers 8 --bind 0.0.0.0:5000 wsgi:app --max-requests 10000 --timeout 5 --keep-alive 5 --log-level info