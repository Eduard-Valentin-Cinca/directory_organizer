import os
import shutil


def menu():
    path = input('Insert the path or write quit to exit the program -> ')
    while not path_validation(path):
        if path == 'quit' or 'Quit' or 'QUIT':
            exit()
        path = input('Insert the path or write quit to exit the program -> ')
    print('Valid path!')
    return path


def path_validation(path: str) -> bool:
    return os.path.isdir(path)


def create_directories(path: str):
    for directory in DIRECTORY_TYPES:
        if not os.path.isdir(path + '\\' + directory):
            os.mkdir(path + '\\' + directory)


def list_all_files(path: str) -> list:
    files = [file for file in os.listdir(path) if os.path.isfile(path + '\\' + file)]
    return files


def get_file_extension(file: str) -> str:
    indexes = [i for i, character in enumerate(file) if character == '.']
    if indexes:
        file_extension = file[indexes[-1]::]
        return file_extension
    else:
        return 'no extension found'


def map_extension_to_folder(path: str) -> dict:
    extension_mapping = {path + '\\' + directory: FILE_EXTENSION_TYPE[i] for i, directory in enumerate(DIRECTORY_TYPES)}
    return extension_mapping


if __name__ == '__main__':
    DIRECTORY_TYPES = ['PDF_files', 'Text_files', 'Word_files', 'Excel_files', 'Presentation_files',
                       'Executable_files', 'Picture_files', 'Photoshop_files', 'Video_files', 'Music_files',
                       'Archived_files', 'Torrent_files', 'Python_files']
    FILE_EXTENSION_TYPE = [['.pdf', '.PDF'], ['.psd', '.PSD'], '.txt', ['.doc', '.docx'], ['.ppt', '.pptx'],
                           ['.xls', '.xlsx', '.csv'], '.exe', ['.jpg', '.jpeg', '.png', '.JPG'],
                           ['.avi', '.mov', '.mp4', '.MOV', '.mkv', ], ['.mp3', '.wav'],
                           ['.zip', '.7z'], '.torrent', '.py']

path = menu()
mapping = map_extension_to_folder(path)
print(mapping)
create_directories(path)
files = list_all_files(path)
for file in files:
    file_extension = get_file_extension(file)
    for key, value in mapping.items():
        if file_extension in value:
            try:
                shutil.move(path + '\\' + file, key)
            except:
                print(file + ' cannot be moved!')
