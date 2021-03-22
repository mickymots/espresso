FROM python:3
ENV PYTHONUNBUFFERED=1
# RUN apt update && apt install gunicorn3 -y
WORKDIR /code
COPY requirements.txt /code/
RUN pip install -r requirements.txt
COPY . /code/