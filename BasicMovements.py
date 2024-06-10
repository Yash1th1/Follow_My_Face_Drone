from djitellopy import tello
from time import sleep

drone = tello.Tello()
drone.connect()
print("Battery:", drone.get_battery())
drone.takeoff()
drone.send_rc_control(0,60,60,0)
    # drone.move_right(20)
sleep(2)
drone.send_rc_control(0, 0, 0, 60)
sleep(2)
drone.send_rc_control(0, 0, 0, -60)
sleep(2)
drone.send_rc_control(0, -60,0,0)
sleep(2)    # drone.move_back(20)
drone.send_rc_control(0, 0, 0,0)
drone.land()

