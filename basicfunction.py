import cv2
img=cv2.imread("OIP.jpg")
#gray scale image
gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
cv2.imwrite("grayscale.png",gray)
cv2.imshow("gray",gray)
cv2.waitKey(0)
