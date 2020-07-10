import cv2
import os

camera=cv2.VideoCapture(0)
i=0
for i in range(50):
    ret, img = camera.read()
    if not ret :
       print("failed")
       break
   
    cv2.putText(img, str(i),(0,50),cv2.FONT_HERSHEY_SIMPLEX,2,(100,0,200),5)
                
    cv2.imshow("cam",img)
    path = 'F:/pyjup'  #destination
    
    cv2.imwrite(os.path.join(path , str(i)+'.jpg'), img)
#     cv2.imwrite(str(i)+'.png',img)
    i=i+1
    cv2.waitKey(100)
#    if cv2.waitKey(100) & 0xFF == ord('q'):
 #      break

    
camera.release()
cv2.destroyAllWindows()