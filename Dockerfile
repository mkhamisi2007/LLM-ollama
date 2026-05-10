FROM ubuntu:latest

ENV SECRET_KEY=mysupersecretkey123
ENV DB_PASSWORD=admin1234

RUN apt-get update && apt-get install -y python3

COPY . /app
WORKDIR /app

CMD ["python3", "app.py"]