import numpy as np
import cv2

width,height=800,800
img=np.zeros((height,width,3),dtype=np.uint8)
location=0
shade=0
n_shades=255
for i in range(n_shades):
    img[0:height,location:location+width//n_shades,1:2] =shade #open cv uses BRG format not RGB format
    location += width//n_shades
    shade+=255//n_shades
cv2.imwrite("myimage.png",img)
