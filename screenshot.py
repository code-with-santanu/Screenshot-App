import time 
import pyautogui


def screenshot():
    fileName = int(round(time.time()* 1000))
    fileName = '{}.png'.format(fileName)
    # time.sleep(3)
    img = pyautogui.screenshot('./images/{}'.format(fileName))
    img.show()


# if __name__ == "__main__":
#     screenshot()