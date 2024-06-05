FROM  huecker.io/library/python:3.12

RUN pip install oemer
RUN pip install flask

# Create Flask app root dir
RUN mkdir /usr/src/oemer_rest_api

# Create oemer-related dirs
RUN mkdir -p /usr/resourse/output
RUN mkdir /usr/resourse/input

WORKDIR /usr/src/oemer_rest_api

# Copy Flask-related source files
COPY ./app ./app
COPY ./main.py .

# Copy image for oemer (temporary hardcoded)
COPY ./image.jpeg /usr/resourse/input

ENV FLASK_APP main.py

CMD ["flask", "run", "--host=0.0.0.0"]
