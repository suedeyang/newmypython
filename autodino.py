import pyautogui
import time
import keyboard

while True:
    im=pyautogui.screenshot()
    screen=im.getpixel((897,147))
    x1=im.getpixel((1080,728))
    x2=im.getpixel((1180,728))
    x3=im.getpixel((1280,728))
    x4=im.getpixel((1380,728))
    x5=im.getpixel((1030,728))

    if screen[0]==255:
        if x4[0]==83 or x1[0]==83 or x2[0]==83 or x3[0]==83 or x4[0]==83:
            pyautogui.press('space')
            time.sleep(0.0001)


    if keyboard.is_pressed('s'):
        break
    