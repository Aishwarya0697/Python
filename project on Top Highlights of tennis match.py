from moviepy import *
import pyloudnorm as pyln
import soundfile as sf
from moviepy.editor import VideoFileClip, concatenate_videoclips
list_loudness=[]
list_mp4=[]
l=[]
l1=[]
while True:
    try:
        csv_path = input("Enter the path for CSV file: ")
        break
    except OSError as error:
        print("File is not found")
        print(error)
    except ParserError as error:
        print("File with wrong Extension")
        print(error)
while True:
     vedio_path = input("enter vedio file path:")
     if vedio_path.endswith(".mp4"):
         break
     else:
         print("enter file extension is not valid")
while True:
     folder_store_vedio = input("enter in which folder you want to store this break vedio files:")
     break
while True:
     folder_store_audio = input("enter in which folder you want to store this break audio files:")
     break
    
while True:
    try:
        service=int(input("how many top moment do you want"))
        break
    except ValueError as error:
        print("input must be in integer format")
        print(error)    
    
while True:
    final_save_path = input("Enter path of Folder to save video:")
    break
while True:
    video_name = input("Enter name you want for your video: ")
    break

from csv import reader
def vedio_audio_loudness():
    with open(csv_path) as f:
        csv_reader=reader(f)
        for i, row in enumerate(csv_reader):
        
            myvideo = VideoFileClip(vedio_path).subclip(row[0], row[1])
                
            myvideo.write_videofile(folder_store_vedio + "\\" + str(i) + ".mp4")
                    
            myvideo.audio.write_audiofile(folder_store_audio + "\\" + str(i) + ".wav")
                    
            data, rate = sf.read(folder_store_audio + "\\" + str(i) + ".wav")
                
            meter = pyln.Meter(rate)
                
            loudness = meter.integrated_loudness(data)
                
            list_loudness.append(loudness)
                
            list_mp4.append(str(i) + ".mp4")
            print (list_loudness)
            print (list_mp4)
vedio_audio_loudness()
    
def sorting_loudness(x,y):
#sorting of all list_mp4,list_loudness in decending order
    l3 = list(zip(x,y))
    d = (sorted(l3, key=lambda i: i[1], reverse=True))
    k1, k2 = list(zip(*d))
    a=k1[0:]
    for i in a:
        l.append(i)
    return l
sorting_loudness(list_mp4,list_loudness)

def top_highlights():
    b=l[0:service]
    for i in b:
        l1.append(i)
    return l1
print(top_highlights())

            
def concatenate_vedio():
    l=[]
    for i in l1:
        l.append(VideoFileClip(folder_store_vedio+"\\"+i))
        final_clip = concatenate_videoclips(l)
        vedio_clip=final_clip.write_videofile(final_save_path + "\\" + video_name + ".mp4" )
        return vedio_clip
print(concatenate_vedio())
