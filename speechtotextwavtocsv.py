# Import library
import speech_recognition as sr
# from playsound import playsound
import os
import readline
from csvsort import csvsort

def rlinput(prompt, prefill=''):
    readline.set_startup_hook(lambda: readline.insert_text(prefill))
    try:
        return input(prompt)
    finally:
        readline.set_startup_hook()

# Name the output csv file as you wish
name_of_meta = input("Please input the output file name: ")
name_of_meta = name_of_meta + '.csv'


# Initialize recognizer class (for recognizer he speech)
r = sr.Recognizer()
path_to_wav = "./wav_audio_files"

# Reading Audio file as source
# listening the audio file and store in audio_text variable

for filename in os.listdir(path_to_wav):
    # There are other files like ".DS_Store" being created in the directory.
    # So, writing a condition to skip the file.
    if filename == ".DS_Store":
        continue
    file_in_wav = os.path.join(path_to_wav, filename)

    print(file_in_wav)
    with sr.AudioFile(file_in_wav) as source:

        audio_text = r.listen(source)

        # recognize() method will throw an error if the API is unreachable.
        # Hence using the exception handling
        try:
            # Using googles speech recognition
            text = r.recognize_google(audio_text, language="te-IN")
            # print('Converting audio transcripts into text...')
            # print(text)

            # while True:
            #     playsound(path_to_wav)
            #     # print("Please check if the audio matches the description")
            #     repeat = input("Play audio to check the transcript matches?(y/n)")
            #     if repeat != "y":
            #         break
            
            # edit_transcript = input("Edit transcript?(y/n)")
            
            # if edit_transcript == "y":
            #     text = rlinput(prompt="Edit Text: ", prefill=text)
            with open(name_of_meta, 'a') as the_file:
                the_file.write(filename.split(".")[0] + "|" + text + "|\n")
        except:
            print('Sorry.. run again...')

csvsort(name_of_meta, [0], output_filename=name_of_meta, has_header=False, delimiter='|')
