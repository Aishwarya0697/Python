from moviepy import *
import pyloudnorm as pyln
import soundfile as sf
from moviepy.editor import VideoFileClip, concatenate_videoclips
import os

list_loudness=[]
list_mp4=[]
l=[]
l1=[]

def csv_file_open():
    '''
    This function take csv file from user
    
    '''
    while True:
        csv_path = input("Enter the path for CSV file: ")
        if csv_path == "":
            print("Empty input is not valid")
        try:
            if not (os.path.exists(csv_path) and csv_path.endswith(".csv")):
                raise FileNotFoundError
        except (OSError,FileNotFoundError) as error:
            print("File is not found")
            print(error)
        else:
            return csv_path
            break
def vedio_file_open():
    '''
    This functions takes input vedio file form user
    
    '''
    while True:
        vedio_path = input("enter vedio file path:")
        if vedio_path == "":
            print("Empty input is not valid")
        try:
            if not (os.path.exists(csv_path) and csv_path.endswith(".csv")):
                raise FileNotFoundError
        except (OSError,FileNotFoundError) as error:
            print("File is not found")
            print("enter file extension is not valid")
            print(error)
        else:
            return vedio_path
            break
def no_of_highlights():
    '''
    This functions takes number of top highlights  from user
    
    '''
    
    while True:
        service=int(input("how many top moment do you want"))
        if service == "":
            print("empty input is not valid")
        elif service == "0":
            print("zero service not acepted")
        else:
            try:
                service = int(service)
                return service
                break
            except ValueError as error:
                print("input must be in integer format")
                print(error)
            
            
def final_path_save():
    '''
    This functions takes final vedio path from user
    
    '''
    
    while True:
        final_save_path = input("Enter path of Folder to save video:")
        if final_save_path == "":
            print("empty input is not valid")
        elif os.path.isdir(final_save_path):
            return final_save_path
            break
        else:
            print("Directory is not found")
def vedio_name():
    '''
    This function takes final vedio name from user
    
    '''
    
    while True:
        video_name = input("Enter name you want for your video: ")
        if video_name == "":
            print("empty input is not valid")
        else:
            return video_name
            break
def stored_vedio():
    '''
    This functions takes break vedio folder path from user
    
    '''
    
    while True:
        break_vedios=input("enter in which folder you want to store this break vedio files:")
        if break_vedios == "":
            print("empty is not valid")
        else:
            return break_vedios
            break
def stored_audio():
    '''
    This functions takes break audio folder path from user
    
    '''
    
    while True:
        break_audios=input("enter in which folder you want to store this break audio files:")
        if break_audios == "":
            print("empty is not valid")
        else:
            return break_audios
            break
        
from csv import reader
def vedio_audio_loudness(csv_path,vedio_path,break_vedios,break_audios):
    with open(csv_path) as f:
        csv_reader=reader(f)
        for i, row in enumerate(csv_reader):
        
            myvideo = VideoFileClip(vedio_path).subclip(row[0], row[1])
                
            myvideo.write_videofile(break_vedios + "\\" + str(i) + ".mp4")
                    
            myvideo.audio.write_audiofile(break_audios + "\\" + str(i) + ".wav")
                    
            data, rate = sf.read(break_audios + "\\" + str(i) + ".wav")
                
            meter = pyln.Meter(rate)
                
            loudness = meter.integrated_loudness(data)
                
            list_loudness.append(loudness)
                
            list_mp4.append(str(i) + ".mp4")    
        
def sorting_loudness():
#sorting of all list_mp4,list_loudness in decending order
    l3 = list(zip(list_mp4,list_loudness))
    d = (sorted(l3,key=lambda i: i[1], reverse=True))
    k1, k2 = list(zip(*d))
    a=k1[0:]
    for i in a:
        l.append(i)
        
def top_highlights(service):
    b=l[0:service]
    for i in b:
        l1.append(i)
      
def concatenate_vedio(final_save_path,video_name,break_vedios):
    l=[]
    for i in l1:
        l.append(VideoFileClip(break_vedios+"\\"+i))
        final_clip = concatenate_videoclips(l)
        vedio_clip=final_clip.write_videofile(final_save_path + "\\" + video_name + ".mp4" )
        return vedio_clip
    
print("**Thanks For Using Application**")
        
if __name__ == "__main__":
    
    print("Welcome\n")
    
    # Runs function to take and open CSV/Excel file
    csv_path=csv_file_open()
    # Runs function to take and open video file
    vedio_path=vedio_file_open()
    # Take number of highlights from user
    service= no_of_highlights()
    # Runs function to ask user for path to save final video
    final_save_path=final_path_save()
    # Enter name for final highlights video
    video_name= vedio_name()
    #Enter folder path to store break vedio
    break_vedios=stored_vedio()
    #Enter folder path to store break audio
    break_audios=stored_audio()
    #Breaking of videos and calculating loudnessand converting them into audios
    vedio_audio_loudness(csv_path,vedio_path,break_vedios,break_audios)
    #soeting of loudness
    sorting_loudness()
    #Top highlights
    top_highlights(service)
    #concatenote top highlights
    vedio_clip=concatenate_vedio(final_save_path,video_name,break_vedios)
    
    

