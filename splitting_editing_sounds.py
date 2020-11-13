import os
from pydub import AudioSegment, silence
from pydub.playback import play

#this is to make sure pydub knows exactly where to go
AugioSegment_converter = "C:\ProgramData\chocolatey\bin\ffmpeg.exe"

#Need to specify where the sound files are
sound_folder = "C:\\Users\\Gebruiker\\OneDrive\\CLS PhD\\MPI\\Python_workshop\\Session_2b_audio_processing\\session2b-sound\\raw"
#print(os.listdir(sound_folder))

#open specific file
#I just wanted to look at each sound file individually, to get an idea about them
Lf_file = "Lf_recording.wav"
Lf_sound = AudioSegment.from_wav(os.path.join(sound_folder, Lf_file))

Nw_file = "NW_recording.wav"
Nw_sound = AudioSegment.from_wav(os.path.join(sound_folder, Nw_file))

Hf_file = "HF_recording.wav"
Hf_sound = AudioSegment.from_wav(os.path.join(sound_folder, Hf_file))

#get the duration of the sound
# print(Lf_sound.duration_seconds)
# print(Nw_sound.duration_seconds)
# print(Hf_sound.duration_seconds)

#Now we want to try to split them into words based on their duration
#pydub works in milliseconds
#total_duration = Hf_sound.duration_seconds * 1000
#print(total_duration)

half_Of_Total_Time = (Hf_sound.duration_seconds / 2) * 1000
#print(half_Of_Total_Time)

#we want to work with the first and second half of the 
first_half = Hf_sound[:half_Of_Total_Time]
#print(first_half)
second_half = Hf_sound[half_Of_Total_Time:]
#print(second_half)

#if we want to create silent spaces
silent_time = AudioSegment.silent(duration = 2000)

#if we want to split sound file into words based on silences
#changing the silence length will effect the split of words, depending on if the words are monosyllabic or more
#changing the threshold may cut of words based on the dB level and split words awkwardly
#Also, within the silence function, the two statements in the () act as AND condtionals. 
words = silence.split_on_silence(Hf_sound, min_silence_len = 2000, silence_thresh = - 50)

#print(Hf_sound.dBFS)

if -19 < -18:
    print("true")