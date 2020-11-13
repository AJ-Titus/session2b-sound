import csv
import os
import numpy as np
from pydub import AudioSegment, silence
from pydub.playback import play
from matplotlib.pyplot import plot, show

AugioSegment_converter = "C:\ProgramData\chocolatey\bin\ffmpeg.exe"

# We have three conditions: High Frequency (HF), Low Frequency (LF), and Non-Words (NW).
# All words for each condition are stored in one .wav file.
# Your task is to:
#       split the words on the silence
#       make sure they all have the same loudness
#       save them in a folder corresponding to their condition (folder names: HF, LF, NW)

path_to_repository = "C:\\Users\\Gebruiker\\OneDrive\\CLS PhD\\MPI\\Python_workshop\\Session_2b_audio_processing\\session2b-sound"  # add your own path here!

# This piece of code is here to help you.
# It reads a text file with information about the stimuli you are going to split (names & condition),
# and returns a dictionary named 'stimuli' with condition as key, and the word itself as value.
# Use this dictionary to name the files you have to save.
stimuli_info = open(os.path.join(path_to_repository, "lexdec_stimuli.txt"))
stimuli_reader = csv.reader(stimuli_info, delimiter=',')
headers = next(stimuli_reader, None)

# Create the dictionary
stimuli = {}
for stimulus in stimuli_reader:
    if stimulus[2] not in stimuli.keys():
        stimuli[stimulus[2]] = list()
    stimuli[stimulus[2]].append(stimulus[3])

# Put them in alphabetical order
for condition, words in stimuli.items():
    sort = sorted(words)
    stimuli[condition] = sort

# change the non-word condition name
#stimuli["NW"] = stimuli.pop("none")
# Now you have the stimulus names. Let's take a look at the dictionary:
# print(stimuli)
stimuli_words = np.array(stimuli)
#print(stimuli_words)
#I wanted to seperated all the of the words into seperate variables to then be able to assigne the words to the correct .wav file
Hf_words = np.array(stimuli["HF"])
#print(len(Hf_words))
#50 total Hf words

Lf_words = np.array(stimuli["LF"])
#print(len(Lf_words))
#50 total Lf words

#Nw_words = np.array(stimuli["NW"])
#print(len(Nw_words))
#100 total Nw words

# YOUR CODE HERE.
sound_folder = "C:\\Users\\Gebruiker\\OneDrive\\CLS PhD\\MPI\\Python_workshop\\Session_2b_audio_processing\\session2b-sound\\raw"
#print(os.listdir(sound_folder))

#open specific file
#I just wanted to look at each sound file individually, to get an idea about them
Lf_sound = AudioSegment.from_wav(os.path.join(sound_folder, "Lf_recording.wav"))
#print(Lf_sound.dBFS)
#-16.374883080516014
#play(Lf_sound)

Nw_sound = AudioSegment.from_wav(os.path.join(sound_folder, "NW_recording.wav"))
#print(Nw_sound.dBFS)
#-17.169795044337373

Hf_sound = AudioSegment.from_wav(os.path.join(sound_folder, "HF_recording.wav"))
#print(Hf_sound.dBFS)
#-18.170628180228533

#We want to create a new folder where we can manipulate the sound files, without changing the original files. 
Lf_sound_folder = "C:\\Users\\Gebruiker\\OneDrive\\CLS PhD\\MPI\\Python_workshop\\Session_2b_audio_processing\\session2b-sound\\Lf_Sound_Folder"
Nw_sound_folder = "C:\\Users\\Gebruiker\\OneDrive\\CLS PhD\\MPI\\Python_workshop\\Session_2b_audio_processing\\session2b-sound\\Nw_Sound_Folder"
Hf_sound_folder = "C:\\Users\\Gebruiker\\OneDrive\\CLS PhD\\MPI\\Python_workshop\\Session_2b_audio_processing\\session2b-sound\\Hf_Sound_Folder"

#we want to make sure that a file does not already exist in the folder
#so we check each file individually for this
# for sound in sound_folder:
#     if not os.path.isdir(Lf_sound_folder):
#         os.mkdir(Lf_sound_folder)
#     if not os.path.isdir(Nw_sound_folder):
#         os.mkdir(Nw_sound_folder)
#     if not os.path.isdir(Hf_sound_folder):
#         os.mkdir(Hf_sound_folder)    
# #then, we want to check what is inside the folders
# print(os.listdir(Lf_sound_folder))
# print(os.listdir(Nw_sound_folder))
# print(os.listdir(Hf_sound_folder))
#currently, there is nothing there because we haven't exported any of the files there. 
def match_target_amplitude(sound, target_dBFS):
    if sound.dBFS < - 18.0:
        decrease_in_dBFS = target_dBFS - sound.dBFS
        return sound.apply_gain(decrease_in_dBFS)
    else:
        if sound.dBFS > -18.0:
            increase_in_dBFS = target_dBFS + sound.dBFS
            return sound.apply_gain(increase_in_dBFS)

normalized_Hf_sound = match_target_amplitude(Hf_sound, -18.0)
#play(normalized_Hf_sound)


#store sound files in new folder
Hf_chunks = silence.split_on_silence(Hf_sound, min_silence_len=100, silence_thresh=-100, keep_silence=100)
for sound in Hf_chunks:
    Hf_sound_file = sound + Hf_words[:] + '_' + '.wav'
    print(Hf_sound_file)

# for i, chunk in enumerate(Hf_chunks):
#     chunk_name = "Hf_words{}.wav".format(i)
# #   print ("exporting", chunk_name)
#     chunk.export(chunk_name, format="wav") # save sound files in "wav" format
#     #chunk.export(os.path.join(Hf_sound_folder, chunk_name))  # save sound files into the corresponding
#     play(Hf_words[47])

#Hf_chunks.export()
# target_volume = -18
# for sound in Hf_chunks:
#     if sound.dBFS < Hf_chunks.dBFS:

# for chunk in enumerate(Hf_chunks): #adopted from: https://stackoverflow.com/questions/36799902/how-to-splice-an-audio-file-wav-format-into-1-sec-splices-in-python
#     chunk_name =  Hf_words[:] + ".wav"
#     chunk.export(chunk_name, format="wav") # save sound files in "wav" format
#     chunk.export(os.path.join(Hf_sound_folder, chunk_name))  # save sound files into the corresponding
#     print(os.listdir(Hf_sound_folder))
                   
#sound.export(new_filename, format =  "mp3")

#Now, I want to normalize the sounds within the file to the same level
#play(Hf_chunks)


# play(Hf_normalized_sound)
#play(Hf_chunks[47])
#print(len(Hf_chunks))

#Now, I want to normalize the sounds within the file to the same level
Lf_chunks = silence.split_on_silence(Lf_sound, min_silence_len=100, silence_thresh=-100, keep_silence=100)
normalized_Lf_sound = match_target_amplitude(Hf_sound, -16.0)
#print(len(Lf_chunks))

Nw_chunks = silence.split_on_silence(Nw_sound, min_silence_len=100, silence_thresh=-100, keep_silence=100)
normalized_Hf_sound = match_target_amplitude(Hf_sound, -17.0)
#Now, I want to normalize the sounds within the file to the same level
#play(Nw_chunks[78])
#print(len(Nw_chunks))

# Hf_sound.export(os.path.join(Hf_sound_folder, Hf_chunks))

# Some hints:
# 1. Where are the stimuli?
# 2. How loud do you want your stimuli to be? Store it in a variable
# 3. Where do you want to save your files? Make separate folders for the conditions.
# 4. Do you normalize the volume for the whole sequence or for separate words? Why (not)? Try it if you like :)
# 5. You can check whether your splitting worked by playing the sound, or by printing the length of the resulting list
# 6. Use the index of the word [in the list of words you get after splitting]
# to get the right text from the dictionary.
# 7. Recall you can plot your results to see what you have done.
# Good luck!



###from Zhenya
# #HF_chunks.export(os.path.join(sound_folder, HF_chunks), format = "wav" )

#  for i, chunk in enumerate(HF_chunks):                   #adopted from: https://stackoverflow.com/questions/36799902/how-to-splice-an-audio-file-wav-format-into-1-sec-splices-in-python
#      chunk_name = "HF_{0}.wav".format(i)
#      print ("exporting", chunk_name)
#      chunk.export(chunk_name, format="wav") # save sound files in "wav" format
#      chunk.export(os.path.join(folder_HF, chunk_name))  # save sound files into the corresponding

# ################# practice from zhenya

# for chunk in enumerate(HF_chunks): 
#     for w in stimuli["HF"]:
#         chunk_name = "HF_" +   w                           
#         #chunk_name = "HF_" + w + ".wav".format(i)
#         print ("exporting", chunk_name)
