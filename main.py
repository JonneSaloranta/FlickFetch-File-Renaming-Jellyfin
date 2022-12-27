
import os
import re


folder_path = ''
try:
    if os.path.exists('path.txt'):
        with open('path.txt', 'r') as file:
            folder_path = file.read()
        use_previous_path = input(f'Use previous path: {folder_path} (y/n): ')

        if use_previous_path == 'y' or use_previous_path == 'Y' or use_previous_path == '':
            pass
        else:
            folder_path = input('Enter the folder path: ')
            if folder_path == '':
                folder_path = os.getcwd()
            with open('path.txt', 'w') as file:
                file.write(folder_path)
    else:

        folder_path = input('Enter the folder path: ')
        if folder_path == '':
            folder_path = os.getcwd()
        with open('path.txt', 'w') as file:
            file.write(folder_path)
except:
    print('Error: Invalid path')

print(f'Folder path: {folder_path}')

# example file name Sirkuspelle Hermanni - 2021-09-07 - Kausi 01 - Jakso 01 - Pyykkipäivä


regex = r'(?P<show_name>.*) - (?P<date>.*) - (?P<season>.*) - (?P<episode>.*) - (?P<title>.*)'


template_name = r'\g<show_name> \g<season>\g<episode> - \g<title>'

print('Regex: ', regex)
print('Template name: ', template_name)

files = os.listdir(folder_path)

# all video formats

video_formats = ['.mp4', '.mkv', '.avi', '.mov', '.wmv', '.flv', '.mpg', '.mpeg', '.m4v', '.webm', '.vob', '.ogv', '.ogg',
                 '.drc', '.gif', '.gifv', '.mng', '.qt', '.mts', '.m2ts', '.ts', '.mxf', '.roq', '.nsv', '.flv', '.f4v', '.f4p', '.f4a', '.f4b']


for file in files:
    if os.path.splitext(file)[1] not in video_formats:
        pass
    else:

        file_name = os.path.splitext(file)[0]
        file_extension = os.path.splitext(file)[1]
        file_path = os.path.join(folder_path, file)

        if not re.match(regex, file_name):
            print(f'Skipped {file}')
            continue

        new_file_name = re.sub(regex, template_name, file_name)

        new_file_name = new_file_name.replace('Kausi ', 'S')
        new_file_name = new_file_name.replace('Jakso ', 'E')

        new_file_path = os.path.join(folder_path, new_file_name + file_extension)

        try:
            os.rename(file_path, new_file_path)
            print(f'Renamed {file} to {new_file_name + file_extension}')
        except:
            print('Error: File already exists')
