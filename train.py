import os 
import cv2
import numpy
def training():
    recognizer = cv2.face.LBPHFaceRecognizer_create()
    images=os.listdir(r'C:\Users\user\Desktop\python programes\attendance-project\datasetwebapp')
    id_list=[]
    face_list=[]
    for image in images:
        # print(image)
        my_image=cv2.imread(r'C:\Users\user\Desktop\python programes\attendance-project\datasetwebapp/'+image,0)
        a=image.split('.')
        # print(a)
        # print(a[1])
        id_list.append(int(a[1]))
        face_list.append(my_image)
        cv2.imshow('display',my_image)
        cv2.waitKey(10)
    # print(id_list)
    recognizer.train(face_list,numpy.array(id_list))
    # print('training')
    recognizer.write(r'C:\Users\user\Desktop\python programes\attendance-project\my_model_1.xml')