# importing libraries 
import os 
import cv2  
from PIL import Image 
import numpy as np 

# reading the language file
f = open("commands.flip","r")
imageNames = []
coord = np.zeros((1000,2))

Lines = f.readlines()
i = 1
for line in Lines:
    args = line.split(' ')
    if(len(args) != 3 and len(args) != 5):
        print("Error in line ",i,". Format is {start frame} {end frame} {x_index} {y_index} {filename}\n")
        exit(0)
    else:
        # i += 1
        sf = int(args[0])
        ef = int(args[1])
        x = 0
        y = 0
        image = ""
        if(len(args) == 5):
            x = int(args[2])
            y = int(args[3])
            image = args[4]
        else:
            image = args[2]
        image = image.strip()
        
        if(not os.path.exists(image)):
            print("Error in line",i,". ",image," does not exist.\n")
            exit(0)
        
        numberOfFrames = ef-sf
        for i in range(0,numberOfFrames):
            imageNames.append(image)
        
        i += 1
print(imageNames)

