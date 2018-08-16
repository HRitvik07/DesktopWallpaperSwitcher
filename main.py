import keyboard
import socket
import time
import ctypes

from GetWallpaper import get_wall, set_wall


def is_connected():
    while True:
        try:
            socket.create_connection(('wallpapersite.com', 80))
            return True
        except Exception as e:
            print(e)
            print("waiting for internet connection")
            time.sleep(300)


if __name__ == "__main__":
    if is_connected():
        flag = 2
        while flag == 2:
            print("running.")
            if keyboard.is_pressed('ctrl+shift+alt+c'):
                get_wall()
                set_wall()
            if keyboard.is_pressed('ctrl+shift+alt+esc'):
                flag = ctypes.windll.user32.MessageBoxW(0, "Want to Turn Off Wallpaper Changer?", "Wallpaper Changer", 1)
            time.sleep(0.25)
