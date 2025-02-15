from flask import Flask

from core import views

app = Flask(
    __name__,
    template_folder="/projects/audioextract/templates/",
    static_folder="/projects/audioextract/static/",
)
