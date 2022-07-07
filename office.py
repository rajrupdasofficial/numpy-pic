import numpy as np
import cv2
from PIL import Image
width,height=600,800
img=np.zeros((height,width,3),dtype=np.uint8)
img[:]=(35,29,43)
img[int(height*0.85):height, 0:width]=(35,55,43)
#building
img[int(height*0.1):int(height*0.9), int(width*0.2):int(width*0.8)]=(94,101,107)
# draw windows
for row in range(6):
    for column in range(5):
        if np.random.randint(0,8)==5:
            window_color=(240,230,140)
        else:
            window_color=(28,23,35)
        img[int(height*0.1+100*row+20):int(height*0.1+100*row+60+20),int(width*0.2+75*column+15):int(width*0.2+75*column+30+15)]=window_color


#cv2.imwrite("myimage.png",img)
Image.fromarray(img).save("sys-image.png")
