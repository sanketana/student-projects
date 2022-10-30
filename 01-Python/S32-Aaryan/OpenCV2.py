import face_recognition as fr
import cv2
import numpy as np
import csv
from datetime import datetime
import os

video_capture = cv2.VideoCapture(0)
aaryan_image = fr.load_image_file("D:\\Aaryan\\OneDrive\\Aaryan's stuff for non school stuff\\Python\\PythonDev\\Aaryan pic.jpg")
mom_image = fr.load_image_file("mom_image.jpeg")


# Load a second sample picture and learn how to recognize it.
aaryan_image_encoding = fr.face_encodings(aaryan_image)[0] #[0] fetches the first parameter
mom_image_encoding = fr.face_encodings(mom_image)[0] 
# Create arrays of known face encodings and their names

known_face_encodings = [aaryan_image_encoding, mom_image_encoding]

known_face_names = [
    "Aaryan",
    "Mom"
]

students=known_face_names.copy()

# Initialize some variables
face_locations = []
face_encodings = []
face_names = []
process_this_frame = True

while True:
    # Grab a single frame of video
    ret, frame = video_capture.read()

    # Resize frame of video to 1/4 size for faster face recognition processing
    small_frame = cv2.resize(frame, (0, 0), fx=0.25, fy=0.25)
    now = datetime.now()
    time = now.strftime('%I:%M:%S:%p')
    date = now.strftime('%d-%B-%Y')
    day = now.strftime('%A')
    #with open(date+'.csv', 'w+') as f: 
    #f=open(date+'.csv','w+',newline='')
    #myfile=csv.writer(f)
    #with open('d:\\employee_file.csv', mode='w') as f:
     #writer = csv.writer(f, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
     #writer.writerow(['fsmanoj','seth'])
    rgb_small_frame = cv2.cvtColor(small_frame,cv2.COLOR_BGR2RGB)

   
    if process_this_frame:
      
        face_locations = fr.face_locations(rgb_small_frame)
        face_encodings = fr.face_encodings(rgb_small_frame, face_locations)

        face_names = []
        for face_encoding in face_encodings:
            
            matches = fr.compare_faces(known_face_encodings, face_encoding)
            name = "Idk who u r"

           
            face_distances = fr.face_distance(known_face_encodings, face_encoding)
            best_match_index = np.argmin(face_distances)
            if matches[best_match_index]:
                name = known_face_names[best_match_index]
                face_names.append(name)
                if name in known_face_names:
                     if name in students:
                          students.remove(name)
                          print(students)
                          current_time = now.strftime('%I:%M:%S:%p')
                          print(current_time)  
                          print(name)
                          print(day)

                          with open("D:\\Aaryan\\OneDrive\\Aaryan's stuff for non school stuff\\Python\\PythonDev\\CSV\\Attendance Sheet.csv", mode='a') as f:
                            writer = csv.writer(f, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)                   
                            writer.writerow([name,current_time,day])
                          
    process_this_frame = not process_this_frame

   
   
    for (top, right, bottom, left), name in zip(face_locations, face_names):
        
        top *= 4
        right *= 4
        bottom *= 4
        left *= 4

        # Draw a box around the face
        cv2.rectangle(frame, (left, top), (right, bottom), (0, 0, 0), 2)

        # Draw a label with a name below the face
        cv2.rectangle(frame, (left, bottom - 35), (right, bottom), (0, 0, 0), cv2.FILLED)
        font = cv2.FONT_HERSHEY_DUPLEX
        cv2.putText(frame, name, (left + 6, bottom - 6), font, 1.0, (255, 255, 255), 1)

    # Display the resulting image
    cv2.imshow('Video', frame)
    

    # Hit 'q' on the keyboard to quit!
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release handle to the webcam
video_capture.release()
cv2.destroyAllWindows()

#f.close()



