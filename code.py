# importing libraries 
import os 
import cv2  
from PIL import Image 
import numpy as np 
import imutils
import sys
import imageio

def generateGif(imageNames, video_name, fpsUser):
    images = []
    for imageName in imageNames:
        images.append(imageio.imread(imageName))
    imageio.mimsave(video_name, images, fps = fpsUser)

def resizeImages(mw, mh, imageNamesUnique):
    for im in imageNamesUnique:
        image = cv2.imread(im)
        newImage = imutils.resize(image , width=mw, height=mh)
        cv2.imwrite(im, newImage)

def generateVideo(imageNames,fpsUser,loop,video_name):
    frame = cv2.imread(imageNames[0])
    height, width, layers = frame.shape  
    video = cv2.VideoWriter(video_name, 0, fpsUser, (width, height))

    for _ in range(loop):
        for image in imageNames:  
            video.write(cv2.imread(image)) 
    cv2.destroyAllWindows()  
    video.release()


gifFlag = False
# reading the language file
# checking if it is a .flip file
filename = sys.argv[1]
if(not ".flip" in filename):
    print("Error: File must be of .flip format")
    exit()
# checking if output path is .avi or .gif
outputvid = sys.argv[2]
if(not "avi" in outputvid and not "gif" in outputvid):
    print("Error: Output file must be of .gif or .avi format")
    exit()
if(".gif" in outputvid):
    gifFlag = True

if(not os.path.exists(filename)):
    print("Error:",filename,"does not exist")
    exit(0)
f = open(filename,"r")

imageNames = []
imageNamesUnique = []
coord = np.zeros((1000,2))
fpsUser = 15
loop = 3
Lines = f.readlines()
i = 1
# animation = 0
for line in Lines:
    if("fps" in line):
        args_fps = line.split('=')
        # print(args_fps)
        x = args_fps.index("fps")
        # print(x)
        fpsUser = int(args_fps[x+1].strip())
        # print(fpsUser)
        continue
    
    if("loop" in line):
        args_loop = line.split('=')
        x = args_loop.index("loop")
        loop = int(args_loop[x+1].strip())
        continue
    
    args = line.split(' ')
    if(len(args) != 3 and len(args) != 5):
        print("Error in line "+str(i)+". Format is {start frame} {end frame} {x_index} {y_index} {filename}")
        print("or {start frame} {end frame} {filename}")
        exit(0)
    else:
        # i += 1
        sf = int(args[0])
        ef = int(args[1])
        if(not isinstance(sf, int) or not isinstance(ef, int)):
            print("Error in line "+str(i)+". Format is {start frame} {end frame} {x_index} {y_index} {filename}")
            print("or {start frame} {end frame} {x_index} {y_index} {filename}")
            exit(0)
        x = 0
        y = 0
        image = ""
        if(len(args) == 5):
            # animation = 1
            x = int(args[2])
            y = int(args[3])
            image = args[4]
        else:
            image = args[2]
        image = image.strip()
        
        if(not os.path.exists(image)):
            print("Error in line"+str(i)+". "+image+" does not exist.")
            exit(0)
        
        numberOfFrames = ef-sf
        imageNamesUnique.append(image)
        for i in range(0,numberOfFrames):
            imageNames.append(image)
        
        i += 1
# print(imageNames)

# Constructing the image list for the gif

# Making all images the same size
mean_height = 0
mean_width = 0
num_of_images = len(imageNamesUnique)

for impath in imageNamesUnique: 
    im = Image.open(impath) 
    width, height = im.size 
    mean_width += width 
    mean_height += height

mean_width = int(mean_width / num_of_images) 
mean_height = int(mean_height / num_of_images)

# Resize images to make the video seamless
resizeImages(mean_width, mean_height, imageNamesUnique)

# Generate video
if(gifFlag):
    generateGif(imageNames, outputvid, fpsUser)
else:
    generateVideo(imageNames, fpsUser, loop,outputvid)
    