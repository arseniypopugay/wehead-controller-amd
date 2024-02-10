import cv2
import time
import os

from wehead_hack_sdk import Wehead

token = os.environ.get("HEADTOKEN", "YOUR_TOKEN_HERE")
wehead = Wehead(token)

wehead.move(pitch=0.5, yaw=0.5)
wehead.say("Hello robotics world!")

@wehead.on_video
def process_frame(img):
    pass

@wehead.on_phrase
def handle_phrase(text):
    if text == "Exit.":
        wehead.say("Goodbye")
        time.sleep(1)
        exit()

while True:
    pass  # Keep the script running
