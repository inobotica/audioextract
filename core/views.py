from flask import render_template, request, Response, url_for, redirect, send_from_directory, send_file
from core import app
from core.audio import extract_audio
#from werkzeug import secure_filename
import os

## uploading specs ##
UPLOAD_FOLDER = '/tmp/'
ALLOWED_EXTENSIONS = set(['mp4'])

def allowed_file(filename):
    return '.' in filename and \
    filename.rsplit('.', 1)[1] in ALLOWED_EXTENSIONS

@app.route('/', methods = ['GET', 'POST'])
def index():

    if request.method == 'POST': 
        
        file = request.files['file']
        print("filename", file.filename, allowed_file(file.filename))
        print("button:", request.form.get("torrent_id", None))

        if file and allowed_file(file.filename):
            #filename = secure_filename(file.filename)
            filename = file.filename
            file.save(os.path.join(UPLOAD_FOLDER, filename))           
            return {"status": "ok", "filename": file.filename}, 200

        else:
            return {"status": "error"}, 400
    else:
        return render_template('index2.html')

@app.route('/uploads/<filename>', methods = ['GET'])
def uploads(filename):
    audio_filename = extract_audio(os.path.join(UPLOAD_FOLDER, filename))
    return send_file(audio_filename, as_attachment=True)