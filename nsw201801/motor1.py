#motor test
from gpiozero import Motor
import time

right = Motor(23, 24)
right.forward()
time.sleep(1)
right.stop()
time.sleep(1)
right.backward()
time.sleep(1)
right.stop()

left = Motor(20,21)
left.forward()
time.sleep(1)
left.stop()
time.sleep(1)
left.backward()
time.sleep(1)
left.stop()
