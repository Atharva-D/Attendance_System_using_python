import cv2
import os 

def file_name_path(path):
    dir = os.path.dirname(path)
    if not os.path.exists(dir):
        os.makedirs(dir)

face_id = input('Enter your Roll.No:')

video = cv2.VideoCapture(0, cv2.CAP_DSHOW)


face_classifier =cv2.CascadeClassifier('C:/Users/HP/AppData/Local/Programs/Python/Python39/Lib/site-packages/cv2/data/haarcascade_frontalface_default.xml')

count = 0


while (True):

    
    _, image_frame = video.read()
    """
    _ is just a variable like any other, however there are a few (contradictory) conventions for a variable called _. 
    The one you see here is when you need to assign a result to a value that is not subsequently used: 
    the retrieve method is returning two values and the programmer is only interested in the second one.
    """

    gray = cv2.cvtColor(image_frame, cv2.COLOR_BGR2GRAY)

    
    faces = face_classifier.detectMultiScale(gray, 1.3, 5)

    
    for (x, y, w, h) in faces:
        
        cv2.rectangle(image_frame, (x, y), (x + w, y + h), (255, 0, 0), 2)
        count += 1
        cv2.imwrite("G:/Computing With Python/Course_Project/E3_CWP_Attendance System/dataset/" + str(face_id) + '.' + str(count) + ".jpg", gray[y:y + h, x:x + w])
        cv2.imshow('frame', image_frame)
        cv2.setWindowProperty('frame', cv2.WND_PROP_TOPMOST, 1)
        
    
    if cv2.waitKey(100) & 0xFF == ord('q'):
        break
   
    if count >= 50:
        print("Dataset created Successfully!")
        break


video.release()

cv2.destroyAllWindows()

