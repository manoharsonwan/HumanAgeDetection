import urllib.request
import random


def downloader(image_url):
    file_name = random.randrange(1,10000)
    file_dir = "/home/qwickbit/Documents/Palm_API/url_downloader/"
    full_file_name = file_dir + str(file_name) + '.jpg'
    urllib.request.urlretrieve(image_url,full_file_name)
    print(full_file_name)

downloader("https://thumbs.dreamstime.com/z/female-hand-palm-isolated-780255.jpg")