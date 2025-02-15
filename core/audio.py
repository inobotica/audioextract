# Import moviepy
import os

import moviepy.editor


def extract_audio(filename: str) -> str:
    # Load the Video
    video = moviepy.editor.VideoFileClip(filename)
    audiopath, audioname = os.path.split(filename)
    audioname = audioname.split(".")[0] + ".mp3"
    audiofilepath = os.path.join(audiopath, audioname)
    print("audio filepath:", audiofilepath)
    # Extract the Audio
    audio = video.audio

    # Export the Audio
    audio.write_audiofile(audiofilepath)

    return audiofilepath
