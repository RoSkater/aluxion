FROM python:3.10

ENV PYTHONUNBUFFERED=1

WORKDIR /aluxion

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY . /aluxion

EXPOSE 8000

CMD ["python3","manage.py","runserver"]