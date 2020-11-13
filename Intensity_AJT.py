import os
from pydub import AudioSegment, silence, effects
from pydub.playback import play

#this is to make sure pydub knows exactly where to go
AugioSegment_converter = "C:\ProgramData\chocolatey\bin\ffmpeg.exe"

#Need to specify where the sound files are
sound_folder = "C:\\Users\\Gebruiker\\OneDrive\\CLS PhD\\MPI\\Python_workshop\\Session_2b_audio_processing\\session2b-sound\\raw"
#print(os.listdir(sound_folder))

#open a file
filename = "HF_recording.wav"
sound = AudioSegment.from_wav(os.path.join(sound_folder, filename))

#to change the volume by number of decibels
#louder = sound + 6
#softer = sound - 6
#the above is okay, but troublesome because it may concontanate sounds or strings

#the better way would be
louder = sound.apply_gain(6)
#softer = sound.apply_gain(-6)

#what if we want to change a sound based on a comparison of a given value
#first check out how loud the sound is
print(sound.dBFS)

target_volume = -6
change = target_volume - louder.dBFS

#dBFS gives the average of the whole file
#can use max_dBFS to get max volume
#remove all the silences first and then apply the averages of dBFS
print(change)

