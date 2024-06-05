FROM  huecker.io/library/python:3.12

RUN pip install flask
RUN mkdir /usr/src/oemer_rest_api

WORKDIR /usr/src/oemer_rest_api

COPY ./app ./app
COPY ./main.py .

ENV FLASK_APP main.py

CMD ["flask", "run", "--host=0.0.0.0"]
