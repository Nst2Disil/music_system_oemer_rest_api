FROM  huecker.io/library/python:3.12

RUN pip install oemer
RUN pip install flask

# Create Flask app root dir
RUN mkdir /usr/src/oemer_rest_api

# Create oemer-related dirs
RUN mkdir -p /usr/resourse/output
RUN mkdir /usr/resourse/input
RUN mkdir /usr/resourse/mock_output/

COPY ./mock_image.musicxml ./image.musicxml

WORKDIR /usr/src/oemer_rest_api

# Copy Flask-related source files
COPY ./app ./app
COPY ./main.py .

ENV FLASK_APP main.py
ENV OEMER_MOCK_RESULT True

CMD ["flask", "run", "--host=0.0.0.0"]
