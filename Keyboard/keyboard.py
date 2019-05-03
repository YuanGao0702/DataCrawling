import pyautogui
from pynput import keyboard
from pynput.keyboard import Key, Controller
SSNs = ['2UA9150Z5C',
'2UA9150Z5D',
'2UA9150Z5F',
'2UA9150Z5G',
'2UA9150Z5J',
'2UA9150Z5K',
'2UA9150Z5L',
'2UA9150Z5M',
'2UA9150Z5R',
'2UA9150Z5S',
'2UA9150Z5T',
'2UA9150Z5V',
'2UA9150Z5W' ]

TPO = ['0003148945',
'3503986794']

def on_press(key):
    try:
        print('alphanumeric key {0} pressed'.format(
            key.char))
    except AttributeError:
        print('special key {0} pressed'.format(
            key))

def on_release(key):
    print('{0} released'.format(
        key))

    if key == keyboard.Key.f1:
        for x in SSNs:
            pyautogui.typewrite(x)
            pyautogui.press('enter')
    if key == keyboard.Key.f2:
        for x in TPO:
            pyautogui.typewrite(x)
            pyautogui.press('enter')
    if key == keyboard.Key.esc:
        # Stop listener
        return False

# Collect events until released
with keyboard.Listener(
        on_press=on_press,
        on_release=on_release) as listener:
    listener.join()


listener = keyboard.Listener(
    on_press=on_press,
    on_release=on_release)

listener.start()
