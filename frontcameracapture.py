import cv2
#web camera live vedio capture project
print("zeenat waseem")
cap=cv2.VideoCapture(0)# 0 for 1 camera if u have another device use 1
cap.set(3,640)#width set
cap.set(4,640)#height set
cap.set(10,100)
while(1):
    success,img=cap.read()
    cv2.imshow("vedio",img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break