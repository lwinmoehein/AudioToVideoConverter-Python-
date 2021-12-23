import os
from moviepy.editor import *

# assign directory
audios = 'audios'
images = 'images'
converted = 'converted'
 
# iterate over files in
# that directory
for filename in os.listdir(audios):
    audio = os.path.join(audios, filename) 
    image = os.path.join(images, filename.split('.')[0]+'.png')
    # checking if it is a file
    if os.path.isfile(audio):
        print("Converting : ",audio)
        # Import the audio(Insert to location of your audio instead of audioClip.mp3)
        vaudio = AudioFileClip(audio)
        # Import the Image and set its duration same as the audio (Insert the location of your photo instead of photo.jpg)
        clip = ImageClip(image).set_duration(vaudio.duration)
        # Set the audio of the clip
        clip = clip.set_audio(vaudio)
        #set resolution
        resized = clip.resize( (1280,720) )
        # Export the clip
        resized.write_videofile(converted+"/"+image.split("/")[1].split('.')[0]+".mp4", fps=60)
        