FROM python:3.8

ENV PYTHONUNBUFFERED=1

WORKDIR /aluxion

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY . /aluxion

CMD ["python3","manage.py","runserver","0.0.0.0:8000"]