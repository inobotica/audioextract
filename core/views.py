from flask import render_template, request, Response, url_for, redirect
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

        if file and allowed_file(file.filename):
            #filename = secure_filename(file.filename)
            filename = file.filename
            file.save(os.path.join(UPLOAD_FOLDER, filename))
            extract_audio(os.path.join(UPLOAD_FOLDER, filename))
            #return redirect(url_for('/', filename=filename))

    ## main return
    #return render_template("index.html",
    #    user = user)
    greeting="Hello there, Ace"
    return render_template('index.html', greet=greeting)