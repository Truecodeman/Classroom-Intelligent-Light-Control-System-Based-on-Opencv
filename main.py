import cv2
import os
import time
video = cv2.VideoCapture(0)
face_dector = cv2.CascadeClassifier(r"D:\Python\Lib\site-packages\cv2\data\haarcascade_frontalface_default.xml")
passby = 0
while True:
    ret, img = video.read()
    faces = face_dector.detectMultiScale(img)
    if len(faces) > 0:
        for x, y, w, h in faces:
            cv2.rectangle(img, pt1=(x, y), pt2=(x + w, y + h), color=(0, 255, 255), thickness=2)
            os.system('adb shell am start com.devuni.flashlight/.activity.SplashActivityGDT')
        passby = 0
    else:
        if passby < 5:
            cv2.putText(img, 'Turn off the lights in', (20, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)
            cv2.putText(img,  str(int(round((5-passby), 0))), (360, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)
            cv2.putText(img, 'seconds', (390, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)
            time.sleep(.100)
            passby += 0.1
        elif passby >= 5:
            cv2.putText(img, 'No Body and Lights Off', (100, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)
            os.system('adb shell am force-stop com.devuni.flashlight')
            break
    cv2.imshow('Lights', img)
    K = cv2.waitKey(1)
cv2.destroyAllWindows()
video.release() 
