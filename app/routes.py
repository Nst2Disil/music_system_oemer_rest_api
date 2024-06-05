from app import app

@app.route('/v1/oemer/recognize', methods=['POST'])
def index():
    return {}