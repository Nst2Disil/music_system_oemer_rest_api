docker run \
  --rm \
  -e FLASK_APP='main.py' \
  -e FLASK_PROJECT='oemer_rest_api' \
  -e FLASK_APP_DIR='' \
  -p 8080:3000 \
  -v ./:/shared/httpd/oemer_rest_api \
  devilbox/python-flask:3.8-dev
