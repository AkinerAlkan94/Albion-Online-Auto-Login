import time
import numpy
import pyautogui
import cv2


while True:
    myScreenshot = pyautogui.screenshot()
    print('ScreenShot Taken')
    # convert image to numpy array
    large_image = cv2.cvtColor(numpy.array(myScreenshot), cv2.COLOR_RGB2BGR)

    method = cv2.TM_SQDIFF_NORMED

    # Read the images from the file
    loginButton = cv2.imread('D:\Repositories\Personal\AlbionAutoLogger\Resources\LoginButton.png')
    result = cv2.matchTemplate(loginButton, large_image, method)
    mn, _, mnLoc, _ = cv2.minMaxLoc(result)

    if mn < 0.00001:
        print('Found Login Button')
        MPx, MPy = mnLoc
        pyautogui.click(MPx, MPy)

    enterWorldButton = cv2.imread('D:\Repositories\Personal\AlbionAutoLogger\Resources\EnterWorld.png')
    result = cv2.matchTemplate(enterWorldButton, large_image, method)
    mn, _, mnLoc, _ = cv2.minMaxLoc(result)

    if mn < 0.00001:
        print('Found Enter World Button')
        MPx, MPy = mnLoc
        pyautogui.click(MPx, MPy)

    okayButton = cv2.imread('D:\Repositories\Personal\AlbionAutoLogger\Resources\OkayButton.png')
    result = cv2.matchTemplate(okayButton, large_image, method)
    mn, _, mnLoc, _ = cv2.minMaxLoc(result)

    if mn < 0.00001:
        print('Found Okay Button')
        MPx, MPy = mnLoc
        pyautogui.click(MPx, MPy)


    okayButton2 = cv2.imread('D:\Repositories\Personal\AlbionAutoLogger\Resources\OkayButton2.png')
    result = cv2.matchTemplate(okayButton2, large_image, method)
    mn, _, mnLoc, _ = cv2.minMaxLoc(result)

    if mn < 0.00001:
        print('Found Okay2 Button')
        MPx, MPy = mnLoc
        pyautogui.click(MPx, MPy)

    time.sleep(10)
