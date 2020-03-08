# For only code refer to this file, for both code and output refer to word document

#Task 1

import cv2
from google.colab.patches import cv2_imshow
img_grey = cv2.imread('lo.png', cv2.IMREAD_GRAYSCALE)

# define a threshold, 128 is the middle of black and white in grey scale
thresh = 128

# assign blue channel to zeros
img_binary = cv2.threshold(img_grey, thresh, 255, cv2.THRESH_BINARY)[1]

#save image
cv2.imwrite('loz.png',img_binary) 
cv2_imshow(img_binary)
width, height = img_binary.shape
left = width
right = 0
top = height
bottom = 0
for x in range(height ):
  for y in range(width):
    color = img_binary[y, x]
    if color == 0:
      if x >right:
        right = x
      if x < left:
        left = x
      if y > bottom:
        bottom = y
      if y < top:
        top = y 
print(left, right, top, bottom)
crop = img_binary[top:bottom, left:right]
cv2_imshow(crop)

#Task 2
height, width = crop.shape
cx = 0
cy = 0
n = 0
for x in range(height-1):
  for y in range(width-1):
    if crop[x, y] == 0:
      cx += x
      cy += y
      n += 1
cx /= n
cy /= n
print(cx, cy)
cv2.rectangle(crop_img,(0,0),(cx,cy),(0,255,0),1)
cv2.rectangle(crop_img,(cx,0),(crop_img.shape[1],0),(0,255,0),1)
cv2.rectangle(crop_img,(0,cy),(0,crop_img.shape[0]),(0,255,0),1)
cv2.rectangle(crop_img,(cx,cy),(crop_img.shape[1],crop_img.shape[0]),(0,255,0),1)
cv2_imshow(crop_img)

#Task3
prev = crop_img[0,0] 
n = 0
for  x  in  range(1,crop_img.shape[1],1):
    for y  in  range(1,crop_img.shape[0],1): 
      curr = crop_img[y, x]
      if(curr == 255  and  prev == 0):
         n =  n  +  1
      prev = curr
