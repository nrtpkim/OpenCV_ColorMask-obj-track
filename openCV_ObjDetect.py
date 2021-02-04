import cv2
import numpy as np

def nothing(x):
    pass


def contours_img(mask):
    contours, _ = cv2.findContours(mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    return contours


def filter_contours_img(contours, img_draw, color_bbox, onTracking):
    count = 0
    for c in contours:
        rect = cv2.boundingRect(c)
        x,y,w,h = rect
        area = w * h
        if area > 6000:
            count = count + 1 # นับ object ที่มีพื้นที่มากกว่า 1000 pixel
            cv2.rectangle(img_draw, (x, y), (x+w, y+h), color_bbox, 5)

            if tracker.init(frame, (x, y, w, h)):
                onTracking = True
            
            print(area)
    return img_draw, count, onTracking


cap = cv2.VideoCapture(0)
tracker = cv2.TrackerMedianFlow_create()
onTracking = False


while True:
    _, frame = cap.read()
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HLS)



    lower_blue = np.array([120, 80, 89])
    upper_blue = np.array([215, 197, 182])

    mask = cv2.inRange(hsv,lower_blue, upper_blue)


    # result = cv2.bitwise_and(frame, frame, mask=mask)
    if not onTracking:
        contours = contours_img(mask)
        color_bbox = (0, 0, 255)
        img_draw, count_yellow, onTracking = filter_contours_img(contours, frame, color_bbox, onTracking)
      

    else:
        ok, bbox = tracker.update(frame)
        if ok:
            p1 = int(bbox[0]), int(bbox[1])
            p2 = int(bbox[0] + bbox[2]), int(bbox[1] + bbox[3])
            cv2.rectangle(frame, p1, p2, (0,255,0), 2)
        else:
            onTracking = False
            tracker = cv2.TrackerMedianFlow_create()
    # print(count_yellow)


    cv2.imshow("frame", frame)
    cv2.imshow("mask", mask)
    key = cv2.waitKey(1)
    if key ==27:
        break

   


cap.release

    
    # cv2.imshow("result", result)