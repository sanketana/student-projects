import face_recognition 
import cv2 
import numpy as np
import csv
from datetime import datetime

video_capture = cv2.VideoCapture(0)

arush_image = face_recognition.load_image_file("ArushPic.png")
arush_face_encoding = face_recognition.face_encodings(arush_image)[0]

vihaan_image = face_recognition.load_image_file("VihaanPic.png")
vihaan_face_encoding = face_recognition.face_encodings(vihaan_image)[0]


# Create lists of known face encodings and their names
known_face_encodings = [
    arush_face_encoding,
    vihaan_face_encoding,
]
known_face_names = [
    "arush",
    "vihaan",
]

students=known_face_names.copy()

# Initialize some variables
face_locations = []
face_encodings = []
face_names = []
process_this_frame = True

while True:
    ret, frame = video_capture.read()
    small_frame = cv2.resize(frame, (0, 0), fx=0.25, fy=0.25)
    now = datetime.now()
    rgb_small_frame = cv2.cvtColor(small_frame,cv2.COLOR_BGR2RGB)

   
    if process_this_frame:
      
        face_locations = face_recognition.face_locations(rgb_small_frame)
        face_encodings = face_recognition.face_encodings(rgb_small_frame, face_locations)
        face_names = []
        
        for face_encoding in face_encodings:
            
            matches = face_recognition.compare_faces(known_face_encodings, face_encoding)
            name = "Unknown"
            face_distances = face_recognition.face_distance(known_face_encodings, face_encoding)
            best_match_index = np.argmin(face_distances)
            
            if matches[best_match_index]:
                name = known_face_names[best_match_index]
                face_names.append(name)
                if name in known_face_names:
                     if name in students:
                          students.remove(name)
                          current_time = now.strftime('%I:%M:%S:%p %A')


                          with open('Attendance.csv', mode='a') as f:
                            writer = csv.writer(f, delimiter=',')                   
                            writer.writerow([name,current_time])
                         
                          
    process_this_frame = not process_this_frame

   
   
    for (top, right, bottom, left), name in zip(face_locations, face_names):
        top *= 4
        right *= 4
        bottom *= 4
        left *= 4
        cv2.rectangle(frame, (left, top), (right, bottom), (0, 0, 255), 2)
        cv2.rectangle(frame, (left, bottom - 35), (right, bottom), (0, 0, 255), cv2.FILLED)
        font = cv2.FONT_HERSHEY_DUPLEX
        cv2.putText(frame, name, (left + 6, bottom - 6), font, 1.0, (255, 255, 255), 1)

    cv2.imshow('Video', frame)
    

    # Hit 'q' on the keyboard to quit!
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release handle to the webcam
video_capture.release()
cv2.destroyAllWindows()

#f.close()
