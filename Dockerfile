FROM python

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt
RUN pip install gunicorn cryptography

COPY app app
COPY tracker.py config.py boot.sh ./
RUN chmod a+x boot.sh

ENV FLASK_APP tracker.py


EXPOSE 5000
ENTRYPOINT ["./boot.sh"]