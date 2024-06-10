import math

from djitellopy import tello
from time import sleep
import keyboard as kb
import numpy as np
import cv2
import math

fspeed = 117/10#forward speedbn(15cm/s)
aspeed = 360/10# angular speed(50d/s)
interval = 0.5

dInterval = fspeed*interval
aInterval = aspeed*interval

x, y = 500, 500
a = 0
yaw = 0
kb.init()
drone = tello.Tello()
drone.connect()
print(drone.get_battery())
points = [(0, 0), (0, 0)]
print(kb.getkey("s"))
def getkeyboardInput():
    lr, fb, ud, yw = 0, 0, 0, 0
    speed = 15
    aspeed = 50
    global x, y, yaw, a
    d = 0
    if kb.getkey("LEFT"):
        lr = -speed
        d = dInterval
        a = -180

    elif kb.getkey("RIGHT"):
        lr = speed
        d = -dInterval
        a = 180

    if kb.getkey("UP"):
        fb = speed
        d = dInterval
        a = 270

    elif kb.getkey("DOWN"):
        fb = -speed
        d = -dInterval
        a = -90

    if kb.getkey("w"):
        ud = speed
    elif kb.getkey("s"):
        ud = -speed

    if kb.getkey("a"):
        yw = -aspeed
        yaw -= aInterval

    elif kb.getkey("d"):
        yw = aspeed
        yaw += aInterval

    if kb.getkey("q"): drone.land()

    if kb.getkey("SPACE"): drone.takeoff()
    sleep(0.5)
    a += yaw
    x += int(d*math.cos(math.radians(a)))
    y += int(d * math.sin(math.radians(a)))
    return[lr, fb, ud, yw, x, y]
def drawpoints(img, points):
    for point in points:
        cv2.circle(img, point, 5, (0, 0, 255), cv2.FILLED)
    cv2.circle(img, points[-1], 8, (0, 255, 0), cv2.FILLED)
    cv2.putText(img, f'({(points[-1][0]-500)/100},{(points[-1][1]-500)/100})m',
    (points[-1][0]+10,points[-1][1]+30),cv2.FONT_HERSHEY_PLAIN,1,(255,0,255),1)


while True:
  vals = getkeyboardInput()
  drone.send_rc_contro l(vals[0], vals[1], vals[2], vals[3])
  img = np.zeros((1000, 1000, 3), np.uint8)
  if (points[-1][0]!= vals[4] or points[-1][1]!= vals[5]):
      points.append((vals[4], vals[5]))
  drawpoints(img, points)
  cv2.imshow("output", img)
  cv2.waitKey(1)