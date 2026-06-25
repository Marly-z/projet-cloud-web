
FROM python:3.10

WORKDIR /app

COPY . .

RUN pip install -r app/requirements.txt

EXPOSE 5000

CMD ["python", "app/app.py"]
