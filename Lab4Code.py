# For only code refer to this file, for both code and output refer to word document

#Task 
import numpy as np
import cv2
from google.colab.patches import cv2_imshow

#transition fuction
def transition(x1,x2,y1,y2,final):  
  prev = final[y1,x1]
  n = 0
  for x in range(x1, x2-1):
    for y in range(y1, y2-1):
      curr = final[y,x]
      if curr == 255 and prev == 0: 
        n = n + 1
      prev = curr
  return n

#ratio function
def rationFunc(left,  right,  top,  bottom):
  return ((right-left)/(bottom-top)) 

#Centroid function
def centroidFunc(image,  left,  right,  top,  bottom):
  cx = left
  cy = top
  n = 0

  for x in range(left,right-1):
    for y in range(top, bottom-1):
      if cropImage[y,x] == 0:
        cx = cx + x
        cy = cy + y
        n = n + 1
  if n !=0:  
    cx = cx/n
    cy = cy/n
   

  f= open("centroid.txt","a+")
  f.write("%f , %f \n" % (cy , cx))
  f.close()

  cropImage2 = cropImage
  for x in range(left,right-1):
    for i in range(top, bottom-1):
      cropImage2[int(cy),x] = 50  
      cropImage2[i,int(cx)] = 50
   
  cv2_imshow(cropImage2)
  return int(cx), int(cy)

#split function
def split(image,left,right,top,bottom, depth =0): 
  if  depth  <  3:
    cx,  cy  =  centroidFunc(image,  left,  right,  top,  bottom)
    if cx != 0 and cy != 0:
      split(image,  left,  cx,  top,  cy,  depth  +  1)  
      split(image,  cx,  right,  top,  cy,  depth  +  1) 
      split(image,  left,  cx,  cy,  bottom,  depth  +  1) 
      split(image,  cx,  right,  cy,  bottom,  depth  +  1)
  else:  
    t  =  transition(left,  right,  top,  bottom,image) 
    r  =  rationFunc(left,  right,  top,  bottom)
 
   
 
    f1= open("transitions.txt","a+")
    f1.close()

 
    f2= open("aspectRatio.txt","a+")
    f2.close()

img = cv2.imread('signature.jpg',0) 
(thresh, bWImg) = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY)
cv2_imshow(bWImg)
x,y = bWImg.shape 
left = y 
right = 0 
top = x 
bottom = 0

for x in range(0,y-1):
  for y in range(0, x-1):
    color = bWImg[y,x]
    if color==0:
      if x > right:
        right = x
      if x < left:
        left = x
      if y > bottom:
        bottom = y
      if y < top:
        top = y

cropImage = bWImg[top:bottom, left:right]

cv2_imshow(cropImage)
cropImage2 = cropImage
for x in range(0,right-left-1): 
  for y in range(0, bottom-top-1):
    cropImage2[0,x] = 50
    cropImage2[y,0] = 50
    cropImage2[bottom-top-1,x] = 50
    cropImage2[y,right-left-1] = 50

split(cropImage,0,right-left,0,bottom-top)
