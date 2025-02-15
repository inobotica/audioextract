import os

from flask import render_template, request, send_file
from werkzeug.utils import secure_filename

from core import app
from core.audio import extract_audio

UPLOAD_FOLDER = "/tmp/"
ALLOWED_EXTENSIONS = ["mp4"]


def allowed_file(filename):
    return "." in filename and filename.rsplit(".", 1)[1] in ALLOWED_EXTENSIONS


@app.route("/", methods=["GET", "POST"])
def index():

    if request.method == "POST":
        file = request.files["file"]

        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(UPLOAD_FOLDER, filename))
            return {"status": "ok", "filename": file.filename}, 200

        else:
            return {"status": "error"}, 400
    else:
        return render_template("index2.html")


@app.route("/uploads/<filename>", methods=["GET"])
def uploads(filename):
    print("Extracting audio from", filename)
    audio_filename = extract_audio(os.path.join(UPLOAD_FOLDER, filename))
    return send_file(audio_filename, as_attachment=True)
