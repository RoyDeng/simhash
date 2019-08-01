FROM python:3.6.3
RUN mkdir /app
WORKDIR /app
ADD pip.txt /app/
RUN pip install -r pip.txt
ADD . /app/
WORKDIR /app/
ENV PYTHONPATH /app/utils
RUN python manage.py collectstatic --noinput