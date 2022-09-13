import cv2
import imutils
img=cv2.imread("grayscale.png")
#gaussian blur-soothening

gaussian=cv2.GaussianBlur(img,(21,21),0)
cv2.imwrite("gaussainimage.jpg",gaussian)
cv2.waitKey(0)
