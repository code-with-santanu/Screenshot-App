import time
import pyautogui
from PIL import Image


class Agent():

    def __init__(self) -> None:

        self.filename = self.generateFilename()
        self.filePath = None

    def generateFilename(self) -> str:
        fileName = int(round(time.time() * 1000))
        fileName = '{}.png'.format(fileName)
        print("Filename successfully generated")

        return fileName

    # Method to take the screenshot
    def screenshot(self, dirPath) -> None:

        try:
            pyautogui.screenshot('{}\{}'.format(dirPath, self.filename))
            self.filePath = '{}\{}'.format(dirPath, self.filename)

            # Display screenshot
            self.displayImage()
        except Exception as e:
            print("Got Error: ", e)

    # Method to display the captured screeenshot
    def displayImage(self) -> None:
        img = Image.open(self.filePath)
        img.show()
        print("File is shown..")


# Define top level module
if __name__ == "__main__":
    myAgent = Agent()

    myAgent.screenshot(".")
    time.sleep(3)
