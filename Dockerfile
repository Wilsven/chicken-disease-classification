FROM python:3.10.12-slim-bullseye

# RUN apt update -y && apt install awscli -y
RUN apt-get update -y && apt-get install -y gcc
WORKDIR /app

COPY . /app
RUN pip install --upgrade pip
RUN pip install --upgrade setuptools
RUN pip install -r requirements.txt

CMD ["python3", "app.py"]