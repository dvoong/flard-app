FROM python:3

WORKDIR /app
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt
COPY . /app
CMD ["gunicorn", "app:app", "-b", "0.0.0.0:5000"]
