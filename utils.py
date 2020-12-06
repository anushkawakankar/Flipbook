import os 
import cv2  
from PIL import Image 
import numpy as np 
import imutils
import sys
import imageio

def generate_gif(FPS, LOOP, FRAMES, outfile):
    images = [imageio.imread(img) for img in FRAMES*LOOP]
    imageio.mimsave(outfile, images, fps=FPS)