import cv2
import write_attendance
import time

print(cv2.__file__)

start = time.time()
period = 8
face_cas = cv2.CascadeClassifier(
    'C:/Users/HP/AppData/Local/Programs/Python/Python39/Lib/site-packages/cv2/data/haarcascade_frontalface_default.xml')
capture = cv2.VideoCapture(0,cv2.CAP_DSHOW)
recognizer = cv2.face.LBPHFaceRecognizer_create();
recognizer.read("G:/Computing With Python/Course_Project/E3_CWP_Attendance System/trainer.yaml");

flag = 0;
id = 0;
dict = {
    'item1': 1
}
font = cv2.FONT_HERSHEY_SIMPLEX
while True:
    ret, img = capture.read();
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY);
    faces = face_cas.detectMultiScale(gray, scaleFactor=1.2, minNeighbors=6, minSize=(100, 100), flags=cv2.CASCADE_SCALE_IMAGE);
    for (x, y, w, h) in faces:
        cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2);
        id,conf = recognizer.predict(gray[y:y+h,x:x+w])
        if (conf < 60):
            if (id == 11):
                id = 'Atharva Dudhgaonkar'
                if ((str(id)) not in dict):
                    write_attendance.Mark_Attendance("Atharva Dudhgaonkar")
                    dict[str(id)] = str(id)
                    print("Hey Atharva Dudhgaonkar")

            elif (id == 12):
                id = 'Shital Dukale'
                if ((str(id)) not in dict):
                    write_attendance.Mark_Attendance('Shital Dukale')
                    dict[str(id)] = str(id)
                    print("Hey Shital Dukale")

            elif (id == 13):
                id = 'Gaurav Durge'
                if ((str(id)) not in dict):
                    write_attendance.Mark_Attendance('Gaurav Durge')
                    dict[str(id)] = str(id)
                    print("Hey Gaurav Durge")
                    
            
            elif (id == 14):
                id = 'Krushna Durole'
                if ((str(id)) not in dict):
                    write_attendance.Mark_Attendance('Krushna Durole')
                    dict[str(id)] = str(id)
                    print("Hey Krushna Durole")
            
            elif (id == 15):
                id = 'Atharva Dusane'
                if ((str(id)) not in dict):
                    write_attendance.Mark_Attendance('Atharva Dusane')
                    dict[str(id)] = str(id)
                    print("Hey Atharva Dusane")
            
            elif (id == 16):
                id = 'Dyuti'
                if ((str(id)) not in dict):
                    write_attendance.Mark_Attendance('Dyuti Bobby')
                    dict[str(id)] = str(id)
                    print("Hey Dyuti Bobby")
            
        else:
            flag = flag + 1
            break

        cv2.putText(img, str(id) + " " + str(conf), (x, y - 10), font, 1 , (0,0, 255), 1)
    cv2.imshow('frame', img);
    cv2.setWindowProperty('frame', cv2.WND_PROP_TOPMOST, 1)
    if flag == 40:
        print("Unknown face!!Can't recognise!!")
        break;
    if time.time() > start + period:
        break;
    if cv2.waitKey(100) & 0xFF == ord('q'):
        break;

capture.release();
cv2.destroyAllWindows();
