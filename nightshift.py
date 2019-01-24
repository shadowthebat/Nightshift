import pyautogui
# Script that toggles nightshift mode on my mac

pyautogui.PAUSE = .5 # waits x second(s) inbetween clicks
pyautogui.FAILSAFE = True # breaks script uppon moving pointer to upperleft screen

# click top right corner
pyautogui.click(x=1409, y=10, clicks=1, button='left')
# scroll down on possition
pyautogui.scroll(110, x=1395, y=102)
# click possition
pyautogui.click(x=1395, y=102, clicks=1, button='left')
# exit
pyautogui.click(x=1409, y=10, clicks=1, button='left')
