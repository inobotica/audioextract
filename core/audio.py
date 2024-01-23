# Import moviepy
import moviepy.editor

def extract_audio(filename):
    #Load the Video
    video = moviepy.editor.VideoFileClip(filename)

    #Extract the Audio
    audio = video.audio

    #Export the Audio
    audio.write_audiofile("/tmp/A.mp3")