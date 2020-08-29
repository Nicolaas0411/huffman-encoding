FROM python:3.8

WORKDIR /code
COPY requirements.txt .
COPY config.yml .
RUN pip install -r requirements.txt
COPY src/ .
EXPOSE 5672

CMD [ "nameko", "run", "--config", "config.yml", "main" ]