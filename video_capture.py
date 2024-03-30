import cv2
import pickle
import cvzone
import numpy as np

width, height = 130, 55

cap = cv2.VideoCapture('car_parking_vidio.mp4')

poslist = []

try:
    with open('CarParkPos', 'rb') as f:
        poslist = pickle.load(f)
except:
    poslist = []
    
def checkParkingSpace(imgPro):
    spaceCounter = 0

    for pos in poslist:
        x, y = pos

        imgCrop = imgPro[y:y + height, x:x + width]
        count = cv2.countNonZero(imgCrop)


        if count < 900:
            color = (0, 255, 0)
            thickness = 5
            spaceCounter += 1
        else:
            color = (0, 0, 255)
            thickness = 3

        cv2.rectangle(img, pos, (pos[0] + width, pos[1] + height), color, thickness)
        cvzone.putTextRect(img, str(count), (x, y + height - 3), scale=1, thickness=2, offset=0, colorR=color)

    cvzone.putTextRect(img, f'We have : {spaceCounter} parking available & {len(poslist)} parked cars.', (100, 50), scale=2, thickness=5, offset=30, colorR=(128, 128, 128), font = cv2.FONT_HERSHEY_SIMPLEX)
while True:
    
    if cap.get(cv2.CAP_PROP_POS_FRAMES) == cap.get(cv2.CAP_PROP_FRAME_COUNT):
        cap.set(cv2.CAP_PROP_POS_FRAMES, 0)
    success, img = cap.read()
    for pos in poslist:
        cv2.rectangle(img, pos, (pos[0] + width, pos[1] + height), (255, 0, 255), 3)
    cv2.rectangle(img, (150, 250), (280, 815), (255, 255, 255), 3)
    cv2.rectangle(img, (570, 250), (870, 570), (255, 255, 255), 3)
    cv2.rectangle(img, (1035, 190), (1300, 500), (255, 255, 255), 3)
    cv2.rectangle(img, (1040, 1250), (1320, 1540), (255, 255, 255), 3)
    cv2.rectangle(img, (1920, 210), (2180, 480), (255, 255, 255), 3)
    cv2.rectangle(img, (150, 2075), (440, 1260), (255, 255, 255), 3)
    cv2.rectangle(img, (2800, 1080), (3070, 1320), (255, 255, 255), 3)

    
    imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    imgBlur = cv2.GaussianBlur(imgGray, (3, 3), 1)
    imgThreshold = cv2.adaptiveThreshold(imgBlur, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY_INV, 25, 16)
    imgMedian = cv2.medianBlur(imgThreshold, 5)
    kernel = np.ones((3, 3), np.uint8)
    imgDilate = cv2.dilate(imgMedian, kernel, iterations=1)

    checkParkingSpace(imgDilate)
    
    cv2.namedWindow("Image", cv2.WINDOW_NORMAL)
    cv2.resizeWindow("Image", 1200, 800)  
    cv2.moveWindow("Image", 0, 0)
    cv2.imshow("Image", img)
    cv2.setWindowProperty("Image", cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_FULLSCREEN)
    cv2.waitKey(1)

