from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep
import pyautogui
import keyboard

def do() :
    pyautogui.moveTo(960, 950)
    pyautogui.click()
    sleep(1)

    pyautogui.moveTo(960, 850)
    pyautogui.click()

    sleep(1)

    pyautogui.moveTo(1100, 950)
    pyautogui.click()

    sleep(1)

    pyautogui.moveTo(950, 620)
    pyautogui.click()

    sleep(1)

    pyautogui.moveTo(1150, 930)
    pyautogui.click()
    sleep(2)

i = 1
while i < 10000:
    do()
    i+=1
    if keyboard.is_pressed('q'):  # if key 'q' is pressed
        print('You Pressed A Key!')
        break
