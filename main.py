from os import sys
from os import system as sh
import cv2
import numpy as np
from time import *

stream = cv2.VideoCapture(0)
counter = 0
def stream_checkout(break_point):    
    while True:
        success, frame = stream.read()
        frame = cv2.GaussianBlur(frame, (39, 39), 0)
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        frame = cv2.Canny(frame, 20, 20)
        cv2.imshow("Bruh", frame)
        mean = np.mean(frame)
        print(mean)
        if mean >= break_point:
            sh("notify-send whoareyou?")
            sleep(2)
            break    

        if cv2.waitKey(1) & 0xFF == ord('q'):
            print("Exit button was pressed...")
            break
    

print(sys.argv)
def argf(key, callback):
    if static_val == key:
        callback()

static_val = sys.argv[1]
def arg_breakpoint():
    if sys.argv[2]:
        stream_checkout(int(sys.argv[2]))


argf("--breakpoint", arg_breakpoint)
argf("-b", arg_breakpoint)

