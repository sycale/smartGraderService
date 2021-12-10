FROM python:latest

WORKDIR /app

COPY ./pygrader/ .
COPY ./submissions ./submissions

RUN pip3 install -r requirements.txt

RUN ls -l /app

RUN chmod +x start.sh


CMD ./start.sh
