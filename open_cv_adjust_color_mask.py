import cv2
import numpy as np

def nothing(x):
    pass

cap = cv2.VideoCapture(0)
cv2.namedWindow("Trackbars")

cv2.createTrackbar("L - H", "Trackbars", 0, 180, nothing)
cv2.createTrackbar("L - L", "Trackbars", 0, 255, nothing)
cv2.createTrackbar("L - S", "Trackbars", 0, 255, nothing)
cv2.createTrackbar("U - H", "Trackbars", 0, 180, nothing)
cv2.createTrackbar("U - L", "Trackbars", 0, 255, nothing)
cv2.createTrackbar("U - S", "Trackbars", 0, 255, nothing)


while True:
    _, frame = cap.read()
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HLS)

  
    
    l_H = cv2.getTrackbarPos("L - H", "Trackbars")
    l_L = cv2.getTrackbarPos("L - L", "Trackbars")
    l_S = cv2.getTrackbarPos("L - S", "Trackbars")
    u_H = cv2.getTrackbarPos("U - H", "Trackbars")
    u_L = cv2.getTrackbarPos("U - L", "Trackbars")
    u_S = cv2.getTrackbarPos("U - S", "Trackbars")
    
    lower_blue = np.array([l_H, l_L, l_S])
    upper_blue = np.array([u_H, u_L, u_S])

    mask = cv2.inRange(hsv,lower_blue, upper_blue)
    
    cv2.imshow("frame", frame)
    cv2.imshow("mask", mask)
    key = cv2.waitKey(27)
    if key ==27:
        break


