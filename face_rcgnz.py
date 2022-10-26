import cv2
import json
import streamlit
f=open(r'C:\Users\user\Desktop\python programes\attendance-project\database.json')
data=json.load(f)
def face_rec(camera):
    recognizer=cv2.face.LBPHFaceRecognizer_create()
    recognizer.read(r'C:\Users\user\Desktop\python programes\attendance-project\my_model_1.xml')
    face_detector=cv2.CascadeClassifier(r'C:\Users\user\Desktop\python programes\attendance-project\face_model_1.xml')
    while True:
        success,frame=camera.read()
        # print(success,frame)
        if success:
            gray_video=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
            faces=face_detector.detectMultiScale(gray_video,minNeighbors=10,minSize=[100,100])
            # print(faces)
            for x,y,w,h in faces:
                cv2.rectangle(frame,(x,y),(x+w,y+h),(0,255,0),2)
                output=gray_video[y:y+h,x:x+w]
                id,loss=recognizer.predict(output)
                # print(data[id],loss)
                #print (type(id))
                if str(id) in data and loss<70:
                    cv2.putText(frame,data[str(id)],(x,y),cv2.FONT_HERSHEY_DUPLEX,1,(255,0,0),2)
                if loss>70:
                    cv2.putText(frame,'Unknown',(x,y),cv2.FONT_HERSHEY_DUPLEX,1,(255,0,0),2)
                frame=cv2.cvtColor(frame,cv2.COLOR_BGR2RGB)
        return(frame)
        