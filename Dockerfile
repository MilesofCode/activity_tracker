FROM python

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt
RUN pip install gunicorn

COPY app app
COPY tracker.py config.py boot.sh ./
RUN chmod a+x boot.sh

ENV FLASK_APP tracker.py
RUN flask translate compile

EXPOSE 5000