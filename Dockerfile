FROM python



ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
ENV DEBUG 0


COPY ./requirements.txt /requirements.txt
RUN pip install -r requirements.txt




RUN adduser -D user
USER user

