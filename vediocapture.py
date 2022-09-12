import cv2
#vedio capture project
print("zeenat waseem")
cap=cv2.VideoCapture("pexels-sunsetoned-5968893.mp4")
while(1):
    success,img=cap.read()
    cv2.imshow("vedio",img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break


