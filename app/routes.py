import subprocess

from app import app

OUTPUT_PATH     = "/usr/resourse/output"
INPUT_IMAGE_PTH = "/usr/resourse/input/image.jpeg"

@app.route('/v1/oemer/recognize', methods=['POST'])
def recognize():
    command = f"oemer -o {OUTPUT_PATH} {INPUT_IMAGE_PTH}"
    subprocess.run(command, shell=True)
    return {}