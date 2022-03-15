import pyautogui
import time
while True:
    button7location = pyautogui.locateOnScreen('sure.jpg', confidence=0.8)
    if button7location:
        button7point=pyautogui.center(button7location)
        pyautogui.click(button7location)
    #time.sleep(5)
    #pyautogui.scroll(3)
    pyautogui.PAUSE=150
