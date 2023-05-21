import os
import re
import shutil

def search_and_create_files(root_dir, search_word):
    file_extension = '.txt'
    found_files = False
    output_folder = os.path.join(root_dir, 'FisiereNoi')  # Numele folderului pentru fișierele noi

    # Creează folderul de ieșire dacă nu există deja
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    for dirpath, dirnames, filenames in os.walk(root_dir):
        for filename in filenames:
            if filename.endswith(file_extension):
                file_path = os.path.join(dirpath, filename)
                try:
                    with open(file_path, 'r', encoding='utf-8') as file:
                        try:
                            content = file.read()
                        except UnicodeDecodeError:
                            print(f'Error decoding file: {file_path}')
                            continue

                        if re.search(search_word, content):
                            new_filename = f'new_file_{filename}'
                            new_file_path = os.path.join(output_folder, new_filename)
                            try:
                                shutil.copy2(file_path, new_file_path)
                                print(f'{filename} has been copied as {new_filename}.')
                                found_files = True
                            except PermissionError:
                                print(f'Permission denied: Unable to create {new_filename}.')
                                continue
                except PermissionError:
                    print(f'Permission denied: Unable to open {file_path}.')
                    continue

    if not found_files:
        print(f'No files found matching the search criteria.')

root_directory = 'C:\\'  # Directorul în care se va căuta
search_word = input('Enter the search word: ')
search_and_create_files(root_directory, search_word)