import pyautogui
# Script that toggles nightshift mode on my mac
pyautogui.PAUSE = 1
pyautogui.FAILSAFE = True

# click the apple
pyautogui.click(x=29, y=15, clicks=1, button='left')
# System Preferences
pyautogui.click(x=74, y=64, clicks=1, button='left')
# Displays
pyautogui.click(x=427, y=304, clicks=1, button='left')
# Night Shift
pyautogui.click(x=775, y=179, clicks=1, button='left')
# Toggle 'turn on until tmr'
pyautogui.click(x=641, y=340, clicks=1, button='left')
# System Preferences menu
pyautogui.click(x=97, y=0, clicks=1, button='left')
# Quit
pyautogui.click(x=133, y=167, clicks=1, button='left')
