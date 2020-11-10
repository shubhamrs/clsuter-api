FROM python:3.8-slim

WORKDIR /usr/src/app

COPY requirements.txt ./
RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt
RUN pip install kubernetes

COPY app1.py .

EXPOSE 5000

CMD [ "python", "./app1.py" ]
