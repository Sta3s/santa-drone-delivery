from djitellopy import Tello
import time

# Uzdevums: Iziet trasi ar koda palidzību
# Noteikumi:
# - secīgi jaiziet cauri visiem vārtiem
# - jaapmeklē visas platformas
# - jaātgriezas atpakaļ
# - caur vārtiem drīkst līdot tikai taisni (ar kāmeru priekšā)
# Dokumentācija un piemēri
# https://github.com/damiafuentes/DJITelloPy/tree/master
# https://github.com/damiafuentes/DJITelloPy/blob/master/examples/simple.py

tello = Tello()

tello.connect()
tello.takeoff()
tello.rotate_counter_clockwise(190)
tello.move_up(50)
tello.set_speed(40)
tello.move_forward(200)
tello.rotate_clockwise(90)
tello.move_forward(400)
tello.rotate_clockwise(180)
tello.move_forward(400)
tello.rotate_clockwise(180)
tello.move_forward(300)
tello.rotate_clockwise(3)
tello.move_forward(190)
tello.land()
time.sleep(3)


# tello.move_left(100)
# tello.move_right(100)
# tello.move_forward(100)
# tello.move_back(100)

# tello.land()
# tello.takeoff()

# tello.rotate_clockwise(360)
# tello.rotate_counter_clockwise(360)

# tello.land()
