import cv2
import imutils
img=cv2.imread("OIP.jpg")
resize=imutils.resize(img,width=120)
resize=imutils.resize(img,height=150)# resize an image
cv2.imwrite("resizedimage.jpg",resize)#save an image
cv2.waitKey(0)
