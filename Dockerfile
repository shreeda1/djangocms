FROM python

WORKDIR .
COPY .  /app

COPY requirements.txt requirements.txt
RUN python -m pip install -r requirements.txt

