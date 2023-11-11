FROM python:3.12-slim

RUN apt-get update && \
    apt-get install -y build-essential && \
    rm -rf /var/lib/apt/lists/*

WORKDIR /app
COPY . /app
RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 5000

COPY uwsgi.ini /app/uwsgi.ini
CMD ["uwsgi", "--ini", "uwsgi.ini"]
