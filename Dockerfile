FROM python:3.14

WORKDIR /app

COPY server/app.py .

CMD ["python3", "app.py"]