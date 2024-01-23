from flask import Flask

app = Flask(__name__,
            template_folder='/projects/audioextract/templates/',
            static_folder='/projects/audioextract/static/')
from core import views