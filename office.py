import numpy as np
import cv2
from PIL import Image
width,height=800,800
img=np.zeros((height,width,3),dtype=np.uint8)
img[:]=(35,29,43)
img[int(height*0.85):height, 0:width]=(35,55,43)
#cv2.imwrite("myimage.png",img)
Image.fromarray(img).save("sys-image.png")
