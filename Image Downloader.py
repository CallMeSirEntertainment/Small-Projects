import os
import requests
from bs4 import BeautifulSoup
from random import choice

confirm = "null"
first_time_crawling = True
default_directory = os.getcwd()
yes_list = ["Yes", "Yea", "Yep", "Sure", "Def", "Yep", "Aye", "Yup", "Yas", "Yeah", "Yah", "True", "Right", "Okay", "Bet", "Exact", "Positive", "Uh-huh", "Affirm", "Indeed", "Alright", "Agreed", "Of course", "Certainly"]
no_list = ["No", "Nah", "Nope", "Neg", "Never", "Nay", "Not", "Hardly", "Scarcely", "Barely", "Not likely", "Not quite", "Not really", "Not exactly", "Far from it", "Not at all", "Not by any means", "Not a bit", "Not a chance", "Not for me", "No way", "No siree", "No thank you", "No dice", "No go"]

def download_images(url, directory):
    files_downloaded = 0
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.text, 'html.parser')
    img_tags = soup.find_all('img')
    if not img_tags:
        print("\nThere were no images detected on the site you entered.\nThis is usually because the site does not allow crawling or has download protection installed.")
        return
    first_time = True
    for img in img_tags:
        img_url = img.get('src')
        if 'http' not in img_url:
            img_url = url + img_url
        if first_time:
            print(f"\nDownloading {img_url}")
            first_time = False
        else:
            print(f"Downloading {img_url}")
        try:
            filename = img_url.split("?")[0].split("/")[-1]
            response = requests.get(img_url, stream=True, headers=headers)
            with open(os.path.join(directory, filename), 'wb') as out_file:
                out_file.write(response.content)
            files_downloaded += 1
        except requests.exceptions.RequestException as e:
            print(f"An error occurred while downloading {img_url}: {str(e)}")
    print(f"\nAll files downloaded. File count: {files_downloaded}")

while True:
    yes = choice(yes_list)
    yes_lower = yes.lower()
    no = choice(no_list)
    no_lower = no.lower()
    if first_time_crawling:
        url = str(input("Please enter the URL of the website you would like to crawl for images.\n"))
        directory = str(input("\nPlease enter the directory where you would like to save the images, or 'default' for no specified directory.\n")).lower()
        if directory == 'default':
            directory = default_directory
        first_time_crawling = False
    else:
        confirm = str(input(f"\nWould you like to continue crawling? ({yes}/{no})\n")).lower()
        if confirm == no_lower:
            exit()
        elif confirm == yes_lower:
            url = str(input("\nPlease enter the URL of the website you would like to crawl for images.\n"))
            directory = str(input("\nPlease enter the directory where you would like to save the images, or 'default' for no specified directory.\n")).lower()
            if directory == 'default':
                directory = default_directory
        else:
            print(f"\nInvalid input. Please enter '{yes}' for yes or '{no}' for no.")
            continue
    download_images(url, directory)