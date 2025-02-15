# Import moviepy
import moviepy.editor

def extract_audio(filename):
    #Load the Video
    video = moviepy.editor.VideoFileClip(filename)

    #Extract the Audio
    audio = video.audio

    #Export the Audio
    new_filename = filename[:filename.find(".")] + ".mp4"

    audio.write_audiofile(new_filename)
    return new_filename