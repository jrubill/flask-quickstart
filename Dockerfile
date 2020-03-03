FROM python:3.7-alpine

RUN adduser -D quickstart

WORKDIR /home/quickstart

COPY requirements.txt requirements.txt
RUN python -m venv venv
RUN venv/bin/pip install -r requirements.txt
RUN venv/bin/pip install gunicorn


COPY website website 
COPY run.py boot.sh ./

RUN chmod +x boot.sh


RUN chown -R quickstart:quickstart ./
USER quickstart 

EXPOSE 5000
ENTRYPOINT ["./boot.sh"]
