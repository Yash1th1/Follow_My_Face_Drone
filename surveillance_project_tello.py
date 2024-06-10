
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
recording = False
video_writer = None
start_time = None

def start_recording():
    global recording, video_writer, start_time
    recording = True
    start_time = time.time()
    video_writer = cv2.VideoWriter(f'Resources/Videos/{start_time}.avi', cv2.VideoWriter_fourcc(*'XVID'), 30, (960, 720))

def pause_recording():
    global recording
    recording = False

def stop_recording():
    global recording, video_writer
    recording = False
    if video_writer:
        video_writer.release()

def get_keyboard_input():
    lr, fb, ud, yw = 0, 0, 0, 0
    speed = 30
    if kb.getkey("LEFT"): lr = -speed
    elif kb.getkey("RIGHT"): lr = speed

    if kb.getkey("UP"): fb = speed
    elif kb.getkey("DOWN"): fb = -speed

    if kb.getkey("w"): ud = speed
    elif kb.getkey("s"): ud = -speed

    if kb.getkey("a"): yw = speed
    elif kb.getkey("d"): yw = -speed

    if kb.getkey("q"): drone.land();time.sleep(3)

    if kb.getkey("SPACE"): drone.takeoff()
    if kb.getkey("z"):
        if recording:
            pause_recording()
        else:
            start_recording()
        time.sleep(0.3)

    if kb.getkey("x"):
        stop_recording()
        time.sleep(0.3)

    return [lr, fb, ud, yw]

while True:
    vals = get_keyboard_input()
    drone.send_rc_control(vals[0], vals[1], vals[2], vals[3])

    img = drone.get_frame_read().frame
    img = cv2.cvtColor(img, cv2.COLOR_RGB2BGR)  # Convert from RGB to BGR
    img = cv2.resize(img, (960, 720))

    if recording:
        if video_writer:
            video_writer.write(img)

    cv2.imshow("Image", img)
    cv2.waitKey(1)
