import cv2
import numpy as np
from djitellopy import tello
from time import sleep

drone = tello.Tello()
drone.connect()
print(drone.get_battery())
drone.streamon()
drone.takeoff()
drone.send_rc_control(0, 0, 25, 0)
sleep(1.5)

w, h = 360, 240
fbRange = [6200, 6800]

pid = [0.4, 0.4, 0]
perror = 0


def findAkhil(frame):
    faceCascade = cv2.CascadeClassifier("Resources/haarcascade_frontalface_default.xml")
    framegray = cv2.cvtColor(frame, cv2.COLOR_RGB2GRAY)
    faces = faceCascade.detectMultiScale(framegray, 1.2, 8)
    myFacelistC = []
    myFaceListArea = []

    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 0, 255), 2)
        cx = x + w // 2

        cy = y + h // 2
        area = w * h
        #cv2.circle(frame, (cx, cy), 5, (0, 255, 0), cv2.FILLED)
        myFacelistC.append([cx, cy])
        myFaceListArea.append(area)
    if len(myFaceListArea) != 0:
        i = myFaceListArea.index(max(myFaceListArea))
        return frame, [myFacelistC[i], myFaceListArea[i]]
    else:
        return frame, [[0, 0], 0]


def TrackFace(info, w, pid, perror):
    fb = 0
    area = info[1]
    x, y = info[0]
    error = x - w // 2
    speed = pid[0] * error + pid[1] * (error - perror)
    speed = int(np.clip(speed, -100, 100))

    if area > fbRange[0] and area < fbRange[1]:
        fb = 0
    if area > fbRange[1]:
        fb = -20
    elif area < fbRange[0] and area != 0:
        fb = 20

    if x == 0:
        speed = 0
        error = 0

    drone.send_rc_control(0, fb, 0, speed)
    return error


# Set up DroidCam video capture
cap = cv2.VideoCapture(0)  # Use 0 as the index for the first camera (typically the default webcam)

# Define the codec and create VideoWriter object
fourcc = cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter('output.avi', fourcc, 20.0, (w, h))
out1 = cv2.VideoWriter('output1.mp4', fourcc, 20.0, (w, h))

while True:
    frame = drone.get_frame_read().frame
    frame = cv2.resize(frame, (w, h))  # Read a frame from the camera
    frame = cv2.cvtColor(frame, cv2.COLOR_RGB2BGR)
    frame, info = findAkhil(frame)
    perror = TrackFace(info, w, pid, perror)

    # Write the frame into the file 'output.avi'
    out.write(frame)

    cv2.imshow("Live Feed", frame)  # Display the frame

    # Check for 'q' key press to exit
    if cv2.waitKey(1) & 0xFF == ord('q'):
        drone.land()
        break

# Release everything if job is finished
cap.release()
out.release()
cv2.destroyAllWindows()
