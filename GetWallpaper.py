import requests
from bs4 import BeautifulSoup
import os
import ctypes


def get_wall():
    main_url = "https://wallpapersite.com"

    url = main_url + "/random-wallpapers/"
    page_random = requests.get(url)
    content = BeautifulSoup(page_random.text, "html.parser")

    i = 0
    for link in content.find_all('a'):
        i += 1
        if i == 40:
            next_page = link.get('href')
            break

    url2 = main_url + next_page
    print("-------------------------------------------")
    print(url2)
    page_rand_found = requests.get(url2)
    content_rand_found = BeautifulSoup(page_rand_found.text, "html.parser")
    j = 0
    for links in content_rand_found.find_all('a'):
        j += 1

        wallpaper_links = links.get('href')
        if "1920x1080" in wallpaper_links:
            wallpaper_page = wallpaper_links
            if ".jpg" not in wallpaper_page:
                get_wall()
            break

    image_url = main_url + wallpaper_page
    print("-------------------------------------------")
    print(image_url)
    r = requests.get(image_url, allow_redirects=True)
    open('image.jpg', 'wb').write(r.content)
    return


def set_wall():
    path = os.path.abspath("image.jpg")
    ctypes.windll.user32.SystemParametersInfoW(20, 0, path, 0)
    print("Wallpaper Changed.")
    return
