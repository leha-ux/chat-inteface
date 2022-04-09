FROM python:3.8

#Copy files
COPY . /search_server/

# Set working directory
WORKDIR /search_server/

RUN pip install -r requirements.txt

CMD python search_server.py serve --host 0.0.0.0:8080
