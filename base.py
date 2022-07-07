import numpy as np
import cv2

width,height=800,800
img=np.zeros((height,width))
location=0
shade=0
for i in range(50):
    img[0:height,location:location+width//50] =shade
    location += width//50
    shade+=255//50
cv2.imwrite("myimage.png",img)
