import subprocess
import os
from flask import request, send_file, jsonify

from app import app

global oemer_process
oemer_process = None

OUTPUT_PATH = "/usr/resourse/output"
INPUT_PATH = "/usr/resourse/input"
IMG_NAME = "image.jpg"
MUSICXML_NAME = "image.musicxml"

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

                # удаление предыдущих результатов распознавания
                file_list = os.listdir(OUTPUT_PATH)
                for file_name in file_list:
                    file_path = os.path.join(OUTPUT_PATH, file_name)
                    os.remove(file_path)

                oemer_process = run_oemer(img_path)
                
                musicxml_path = os.path.join(OUTPUT_PATH, MUSICXML_NAME)
                if os.path.exists(musicxml_path):
                    return send_file(musicxml_path) 
            except Exception as e:
                return {"error": str(e)}, 500  # Internal Server Error
        else:
            return {"error": "No file provided"}, 400  # Bad Request
    else:
        return {"info": "Sorry, the request cannot be processed. Try later."}, 202  # Accepted 


@app.route('/v1/oemer/status', methods=['GET'])
def check_status():
    try:
        global oemer_process
        if oemer_process is None or oemer_process.poll() is not None:
            return jsonify({"free": True})
        else:
            return jsonify({"free": False})
    except Exception as e:
        return {"error": str(e)}, 500  # Internal Server Error


def run_oemer(img_path):
    global oemer_process
    command = f"oemer -o {OUTPUT_PATH} {img_path}"
    oemer_process = subprocess.Popen(command, shell=True)
    stdout, stderr = oemer_process.communicate()
    return oemer_process