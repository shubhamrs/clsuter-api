FROM python:3.8-slim


COPY . /app
COPY requirements.txt ./
WORKDIR /app
RUN pip install --no-cache-dir -r requirements.txt
EXPOSE 5000 
# ENTRYPOINT [ "python" ] 
CMD [ "python app.py" ] 
