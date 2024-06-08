import subprocess
import os
from flask import request

from app import app

global oemer_process
oemer_process = None

OUTPUT_PATH = "/usr/resourse/output"
INPUT_PATH = "/usr/resourse/input"
IMG_NAME = "image.jpg"

@app.route('/v1/oemer/recognize', methods=['POST'])
def recognize():
    global oemer_process
    # если процесс ещё не запускался или уже завершился
    if oemer_process is None or oemer_process.poll() is not None:
        file = request.files.get('file')
        if file:
            try:
                img_path = os.path.join(INPUT_PATH, IMG_NAME)
                file.save(img_path) 
                oemer_process = run_oemer(img_path)
                return {}
            except Exception as e:
                return {"error": str(e)}, 500  # Internal Server Error
        else:
            return {"error": "No file provided"}, 400  # Bad Request
    else:
        return {"info": "Sorry, the request cannot be processed. Try later."}, 202  # Accepted 


def run_oemer(img_path):
    global oemer_process
    command = f"oemer -o {OUTPUT_PATH} {img_path}"
    oemer_process = subprocess.Popen(command, shell=True)
    stdout, stderr = oemer_process.communicate()
    return oemer_process