from djitellopy import tello
from time import sleep
import keyboard as kb
kb.init()
drone = tello.Tello()
drone.connect()
print(drone.get_battery())

print(kb.getkey("s"))
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

    if kb.getkey("SPACE"): drone.takeoff()

    return[lr, fb, ud, yw]

while True:
  vals = getkeyboardInput()
  drone.send_rc_control(vals[0], vals[1], vals[2], vals[3])
  sleep(0.05)