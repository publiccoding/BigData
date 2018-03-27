from boto3 import Session
from botocore.exceptions import BotoCoreError, ClientError
from contextlib import closing
import os
import sys
import subprocess
from tempfile import gettempdir 
import random 
import time 




session  = Session(profile_name="adminuser")
polly = session.client("polly")


def text_to_speech(text):
    try:
        response = polly.synthesize_speech(Text=text, OutputFormat="mp3", VoiceId="Justin")
    except(BotoCoreError, ClientError) as error:
        print(error)
        sys.exit(-1)


    if "AudioStream" in response:
        
        with closing(response["AudioStream"]) as stream:
            output = os.path.join(gettempdir(), "speech.mp3")

            try:
                with open(output, "wb") as file:
                    file.write(stream.read())
            except IOError as error:
                print(error)
                sys.exit(-1)
    else:
        print("Could not stream audio")
    if sys.platform == "win32":
        os.startfile(output)
        
    else:
        opener = "open" if sys.platform == "darwin" else "xdg-open"
        subprocess.call([opener,output])

sample_text = input("Enter your text input")
text_to_speech(sample_text)

# with open('entities.data','r') as file:
#       for text in file:
#         text_to_speech(text)
#         time.sleep(1)
#print(data_dict)


# def text_to_speech(text):
#     try:
#         response = polly.synthesize_speech(Text=text, OutputFormat="mp3", VoiceId="Justin")
#     except(BotoCoreError, ClientError) as error:
#         print(error)
#         sys.exit(-1)


#     if "AudioStream" in response:
        
#         with closing(response["AudioStream"]) as stream:
#             output = os.path.join(gettempdir(), "speech.mp3")

#             try:
#                 with open(output, "wb") as file:
#                     file.write(stream.read())
#             except IOError as error:
#                 print(error)
#                 sys.exit(-1)
#     else:
#         print("Could not stream audio")
#     if sys.platform == "win32":
#         os.startfile(output)
        
#     else:
#         opener = "open" if sys.platform == "darwin" else "xdg-open"
#         subprocess.call([opener,output])


# with open('entities.data','r') as file:
#       for text in file:
#         text_to_speech(text)
#         time.sleep(1)
# #print(data_dict)
