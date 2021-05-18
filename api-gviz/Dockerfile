FROM python:3.8.9-alpine3.13

RUN mkdir /usr/src/app/
COPY . /usr/src/app/

WORKDIR /usr/src/app/
EXPOSE 5000

# Install graphviz
RUN apk add graphviz
# Check dot is accessible
RUN dot -V

RUN pip install --upgrade pip
RUN pip install -r requirements.txt
RUN pip install -U flask-cors

CMD ["python", "app.py"]