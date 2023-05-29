import PySimpleGUI as sg
import os
import subprocess

# print(os.path.dirname(os.path.realpath(__file__)))
print(os.getcwd())
# os.chdir(os.path.dirname(os.path.realpath(__file__)))
print(os.listdir())
folder = sg.popup_get_folder('Select base folder to scan for videos', no_window=True)

if 'MediaInfo.exe' not in os.listdir():
    print('Please install mediainfo')
    exit()
else:
    print('Found mediainfo')

#Function that converts a number of seconds to hours, minutes and seconds
def seconds_to_hours(milliseconds):
    seconds = milliseconds // 1000
    hours = seconds // 3600
    seconds = seconds % 3600
    minutes = seconds // 60
    seconds = seconds % 60
    return hours, minutes, seconds

def seconds_to_minutes(miliseconds):
    seconds = miliseconds // 1000
    minutes = seconds // 60
    seconds = seconds % 60
    return minutes, seconds

#  scan folder and subfolders for videos
def recursive_search(folder, result_func):
    formats = ('mp4', 'mkv', 'flv', 'avi', 'webm', 'ogg', 'mov')
    videos = []
    directories = []
    length = 0

    with os.scandir(folder) as entries:
        print('Directories: ',  directories)
        print('Videos: ', videos)
        for entry in entries:
            if entry.is_dir():
                directories.append(entry.name)
                print('Directory found: ', entry.name)
                length += recursive_search(entry, result_func)
            else:
                if entry.name.endswith(tuple(formats)):
                    print('Video found: ', entry.name)
                    videos.append(entry.name)
                    length += result_func(entry.name)

    print('Finished. Found: ', videos)
    return length
    
def video_duration(file):
    command = 'mediainfo --Output=Video;%Duration% "' + file + '"'
    # print(command)
    # length = os.system(command=command)
    length = subprocess.getoutput(command)
    print(length)
    float(length)
    return length

    return videos

    # for root, dirs, files in os.walk(folder):
    #     for file in files:
    #         if file.endswith(tuple(formats)):
    #             print(file + ' found')
    #             print(os.path.realpath(root))
    #             videos.append(os.path.join(os._path.realpath(root), file))




    for root, dirs, files in os.walk(folder):
        for file in files:
            if file.endswith('.mp4'):
                print(os.path.join(root, file))
                videos.append(os.path.join(root, file))
        for dir in dirs:
            recursive_scan(os.path.join(root, dir))

formats = ('mp4', 'mkv', 'flv', 'avi', 'webm', 'ogg', 'mov')
videos = []

length = recursive_search(folder, video_duration)
print(seconds_to_hours(length))

# for fold in os.scandir(folder):
#     if fold.is_dir() == False: continue
#     print('Folder: ', fold)
#     duration = print(recursive_search(fold, video_duration))
#     if (duration): print(seconds_to_hours(duration))
#     else: print('no videos found')
    

# with os.scandir() as entries:
#     for entry in entries:
#         print(entry)
#         print(entry.name)
