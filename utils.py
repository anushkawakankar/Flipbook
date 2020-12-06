import os 
import cv2  
from PIL import Image 
import numpy as np 
import imutils
import sys
import imageio

def generate_gif(FPS, LOOP, FRAMES, outfile):
    images = []
    for FRAME in FRAMES:
        images.append(imageio.imread(FRAME))
    imageio.mimsave(outfile, images, fps = FPS)

def generate_video(FPS, LOOP, FRAMES, outfile):
    frame = cv2.imread(FRAMES[0])
    height, width, layers = frame.shape  
    video = cv2.VideoWriter(outfile, 0, FPS, (width, height))

    for _ in range(LOOP):
        for image in FRAMES:  
            video.write(cv2.imread(image)) 
    cv2.destroyAllWindows()  
    video.release()
