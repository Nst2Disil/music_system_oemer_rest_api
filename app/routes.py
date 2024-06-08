import subprocess
import os
from flask import request

from app import app

OUTPUT_PATH = "/usr/resourse/output"
INPUT_PATH = "/usr/resourse/input"

@app.route('/v1/oemer/recognize', methods=['POST'])
def recognize():
    file = request.files.get('file')
    if file:
        try:
            filename = "image.jpg"
            file_path = os.path.join(INPUT_PATH, filename)
            file.save(file_path) 
            
            command = f"oemer -o {OUTPUT_PATH} {file_path}"
            subprocess.run(command, shell=True) 
            return {}
        except Exception as e:
            return {"error": str(e)}, 500  # Internal Server Error
    else:
        return {"error": "No file provided"}, 400  # Bad Request
