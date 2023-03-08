import cv2
import pupil_apriltags as pat
import numpy as np

#rasio panjang : lebar = 16:9
tinggi= 720
lebar= 1280
cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, tinggi)
cap.set(cv2.CAP_PROP_FRAME_WIDTH, lebar)
cap.set(cv2.CAP_PROP_FPS, 30)
cap.set(cv2.CAP_PROP_FOURCC, cv2.VideoWriter_fourcc(*'MJPG'))

det = pat.Detector()

def toInt(li:list):
    return [int(_) for _ in li]
red = (0,0,255)

while True:
    kosong, frame = cap.read()
    frame =cv2.resize(frame, (int(lebar/2), int(tinggi/2))) # size frame

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    res = det.detect(gray, True, [1,1,1,1], 1)

    for i in range(len(res)):
        cv2.circle(frame, (int(res[i].center[0]), int(res[i].center[1])), 5, (0,255,0), -1)

    for i in res:
        pts = [tuple(toInt(_)) for _ in i.corners]
        cv2.polylines(frame, np.array([pts]), True, (0,0,255), 2)

    cv2.imshow("web1", frame)
    cv2.moveWindow("web1", 0 , 0)
    if cv2.waitKey(1) &  0xff == ord('q'):
        break

cap.release()
