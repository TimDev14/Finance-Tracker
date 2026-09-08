FROM python:3.14

WORKDIR /app

COPY server/requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY server/ .

CMD ["python3", "run.py"]