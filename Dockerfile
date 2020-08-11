<<<<<<< HEAD
FROM python



ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
ENV DEBUG 0


COPY ./requirements.txt /requirements.txt
RUN pip install -r requirements.txt




RUN adduser -D user
USER user

=======
FROM python:3

# Set environment variables
ENV PYTHONUNBUFFERED 1

COPY requirements.txt /

# Install dependencies.
RUN pip install -r /requirements.txt

# Set work directory.
RUN mkdir /code
WORKDIR /code

# Copy project code.
COPY . /code/
>>>>>>> e681caa99e8087f402dd05fe663984f2fde7c479
