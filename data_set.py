import json
import cv2
def create_dataset(textbox):
    # print(textbox)
    count=0
    f=open(r'C:\Users\user\Desktop\python programes\attendance-project\database.json')
    data=json.load(f)
    f.close()
    wr=open(r'C:\Users\user\Desktop\python programes\attendance-project\database.json','w')
    data[len(data)+1]=textbox
    json.dump(data, wr)
    wr.close()
    camera=cv2.VideoCapture(0)
    face_detector=cv2.CascadeClassifier(r'C:\Users\user\Desktop\python programes\attendance-project\face_model_1.xml')
    while count<30:
        count=count+1
        success,frame=camera.read()
        if success:
            gray_video=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
            faces=face_detector.detectMultiScale(gray_video,minNeighbors=10,minSize=[100,100])
            # print(faces)
            # print(count)
            for x,y,w,h in faces:
                cv2.rectangle(frame,(x,y),(x+w,y+h),(0,255,0),2)
                my_image=frame[y:y+h,x:x+w]
                cv2.imwrite(r'C:\Users\user\Desktop\python programes\attendance-project\datasetwebapp\user'+'.'+str(len(data))+'.'+str(count)+'.'+'jpg',my_image)
        cv2.waitKey(500)
       
