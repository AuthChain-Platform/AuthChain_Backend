import cv2
from pyzbar.pyzbar import decode 
import time

cam = cv2.VideoCapture(0)
cam.set(5, 640)
cam.set(6, 480)

camera = True
while camera:
    success, frame = cam.read()
    if not success:
        print("Failed to capture frame")
        break
    
    for i in decode(frame):
        print(i.type)  
        print(i.data.decode('utf-8')) 
        time.sleep(6)

    cv2.imshow("OurQr-Code-Scanner", frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):  
        # So if any of us the AuthChain team wants to break this code, we use 'q' to exit
        break

cam.release()
cv2.destroyAllWindows()





# import cv2
# from pyzbar.pyzbar import decode 
# import time


# cam = cv2.VideoCapture(0)
# cam.set(5, 640)
# cam.set(6, 480)
# camera = True
# while camera == True:
#   success, frame = cam.read(0)
#   for i in decode(frame):
#     print(i.Type)
#     print(code.data.decode('utf-8'))
#     time.sleep(6)

#     cv2.imshow("OurQr-Code-Scanner", frame)
#     cv2.waitKey(3)