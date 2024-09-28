import os
from os import system, name
from send2trash import send2trash
from time import sleep
from random import choice

goodbyes = ["I hope your day is filled with joy", "Have a good day", "May your day be filled with happiness", "Wishing you a day full of laughter", "Enjoy your day ahead", "Have an enjoyable day", "May your day be as bright as your smile", "Have a cheerful day", "May your day be filled with good thoughts", "Have a delightful day", "May your day be filled with love and light", "Have a pleasant day", "May your day be as wonderful as you are", "Have a joyful day", "May your day be full of blessings", "Have a fantastic day", "May your day be filled with positivity", "Have a peaceful day", "May your day be as lovely as you", "Have a relaxing day", "May your day be full of beautiful moments", "Have a great day ahead", "May your day be filled with success", "Have a prosperous day", "May your day be as inspiring as you are", "Have a day full of wonder", "May your day be filled with creativity", "Have a day full of great ideas", "May your day be filled with personal growth", "Have a day full of achievements", "May your day be filled with exploration", "Have a day full of new experiences", "May your day be filled with dreams come true", "Have a day full of great conversations", "May your day be filled with great memories", "Have a day full of wonderful surprises", "May your day be filled with strength and courage", "Have a day full of exciting discoveries", "May your day be filled with things you love", "Have a day full of meaningful moments", "May your day be filled with joyous moments", "Have a day full of learning", "May your day be filled with fun and laughter", "Have a day full of peace and love", "May your day be filled with all the things that make you happy", "Have a day full of hard-earned successes", "May your day be filled with lots of love", "Have a day full of warm moments", "May your day be filled with all your favorite things", "Have a day full of pleasant surprises", "May The Force be with you"]
def search_and_delete_files(directory, search_query):
    files_found = 0
    files_searched = 0
    files_deleted = 0
    files = []
    for root, dirs, filenames in os.walk(directory):
        print('Searching', root)
        for filename in filenames:
            files_searched += 1
            if search_query in filename and not root.lower().startswith('c:/windows'):
                full_path = os.path.join(root, filename)
                files.append(full_path)
                files_found += 1
    system('cls' if name == 'nt' else 'clear')
    if files_found == 0:
        print(f"No files were found with your search query. Files searched: {files_searched}.")
        return None
    show = str(input(f"Found {files_found} files (searched {files_searched} files).\nType 'show' to show or press enter to continue.\n")).lower()
    system('cls' if name == 'nt' else 'clear')
    if show == 'show':
        show_number = input("How many files would you like to show?\nInput 'all' to show all.\n").lower()
        system('cls' if name == 'nt' else 'clear')
        files_shown = 0
        if show_number == 'all':
            show_number = files_found
        else:
            show_number = int(show_number)
        for file in files:
            print(file)
            files_shown += 1
            if files_shown == show_number:
                break
    confirm = str(input("\nWould you like to delete these files? (y/n)\n")).lower()
    system('cls' if name == 'nt' else 'clear')
    if confirm == 'y':
        for file in files:
            try:
                send2trash(file)
                print(f'Deleted: {file}')
                files_deleted += 1
            except OSError as e:
                print(f"Could not delete: {file}")
        system('cls' if name == 'nt' else 'clear')
        if files_deleted == 0:
            print("No files with the search query you entered were able to be deleted.")
        else:
            print(f"Complete. {files_deleted} out of {files_found} found files were deleted.")
            print(f"\n{choice(goodbyes)} :)")
        return files_deleted
    else:
        print(f"{choice(goodbyes)} :)")
        return 0
search_query = str(input("Please enter the search query you would like to use.\n"))
system('cls' if name == 'nt' else 'clear')
directory = str(input("Please enter the directory you would like to search.\nInput '.' to search this directory.\nInput 'system' to search the entire computer.\n"))
system('cls' if name == 'nt' else 'clear')
if directory.lower() =='system':
    directory = 'C:\\'
search_and_delete_files(directory, search_query)
sleep(60)