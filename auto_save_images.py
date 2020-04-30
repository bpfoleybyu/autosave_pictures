#!/usr/bin/python
"""
Save image from clipboard to file
"""
 
fname = "s.png"
import tkinter as tk
import time
from PIL import ImageGrab
t = tk.Tk()
t.overrideredirect(1) #This makes it so the tk window doesnt show up.
t.withdraw()
old_val = ""
fname = input("Save Clip as: ")
while True:
    time.sleep(1)
    try:
        clip_val = t.clipboard_get()
    except:
        clip_val = ImageGrab.grabclipboard()
    if type(clip_val) != type(str):
        #compare the size of images, otherwise it just compares the mem location (always diff)
        if clip_val != old_val:
            try:
                image = ImageGrab.grabclipboard()
            except:
                print("error getting image")
                image = None
            if image is not None:
                if type(old_val) != str:
                    if old_val.size != clip_val.size:
                        image.save((fname+ ".png"))
                        print ("PNG image saved as", fname)
                else:
                    image.save((fname+ ".png"))
                    print ("PNG image saved as", fname)
    old_val = clip_val
    # If you ever need to break the loop copy this to the clip board.
    if clip_val == ":q":
        break
    clip_val = None

 

