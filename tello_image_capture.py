from djitellopy import tello
import time
import keyboard as kb
import cv2
kb.init()
drone = tello.Tello()
drone.connect()
print(drone.get_battery())
drone.streamon()
global img
def getkeyboardInput():
    lr, fb, ud, yw = 0, 0, 0, 0
    speed = 50
    if kb.getkey("LEFT"): lr = -speed
    elif kb.getkey("RIGHT"): lr = speed

    if kb.getkey("UP"): fb = speed
    elif kb.getkey("DOWN"): fb = -speed

    if kb.getkey("w"): ud = speed
    elif kb.getkey("s"): ud = -speed

    if kb.getkey("a"): yw = speed
    elif kb.getkey("d"): yw = -speed

    if kb.getkey("q"): drone.land()
    time.sleep(3)

    if kb.getkey("SPACE"): drone.takeoff()
    if kb.getkey('z'):
        cv2.imwrite(f'Resources/Images/{time.time()}.jpg',img)
        time.sleep(0.3)
    return[lr, fb, ud, yw]

while True:
  vals = getkeyboardInput()
  drone.send_rc_control(vals[0], vals[1], vals[2], vals[3])

  img = drone.get_frame_read().frame
  img = cv2.cvtColor(img, cv2.COLOR_RGB2BGR)  # Convert from RGB to BGR
  img = cv2.resize(img, (360, 240))
  cv2.imshow("Image", img)
  cv2.waitKey(1)