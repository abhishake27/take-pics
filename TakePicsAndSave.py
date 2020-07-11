import cv2
import os

camera=cv2.VideoCapture(0)
i=0
start = False
#for i in range(50):
while True :
    ret, img = camera.read()
    if not ret :
       print("failed")
       break
    cv2.rectangle(img,(50,80),(300,300),(255,255,255),2)
    
    if not start:
       cv2.putText(img,"Press 's' to start collecting images"
                   ,(0,50),cv2.FONT_HERSHEY_SIMPLEX,1,(100,0,200),2) 
    
       
    if start :
       roi = img[80:300,50:300]
       cv2.putText(img,"collecting image:"+str(i),(0,50)
                   ,cv2.FONT_HERSHEY_SIMPLEX,2,(100,0,200),3)
       
       path = 'F:/pyjup'  #my destination
       cv2.imwrite(os.path.join(path , str(i)+'.jpg'), roi)
       i=i+1
       
    cv2.imshow("cam",img)  
    
#     cv2.imwrite(str(i)+'.png',img)
    k = cv2.waitKey(100)
    if  k == ord('s'):
       start = True
    elif k == ord('p'):
        start = False
        
    elif k == ord('q'):
       break

    
camera.release()
cv2.destroyAllWindows()