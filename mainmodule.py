import streamlit
import cv2
import data_set
import train
import face_rcgnz
image_placeholder=streamlit.empty()
camera=cv2.VideoCapture(0)
streamlit.title('Welcome')
register_button=streamlit.button('Register')
textbox=streamlit.text_input('please enter your name here:') 
start_button=streamlit.button('START')
stop_button=streamlit.button('STOP')
if register_button:
    data_set.create_dataset(textbox)
    train.training()
    streamlit.text('You have successfully registered')
if start_button:
    while True:
        image=face_rcgnz.face_rec(camera)
        image_placeholder.image(image,width=500)
        if stop_button:
            camera.release()
            break
