from tkinter import *
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
import cv2
import os
import numpy as np



class Face_recognition:
    def __init__(self,root):
        self.root=root
        self.root.geometry('1530x790+0+0')
        self.root.title("Face Recognition System")

        title_lb1=Label(self.root,text='FACE RECOGNITION',font=('times new roman',35,'bold'),bg='gray',fg='green')
        title_lb1.place(x=0,y=0,width=1530,height=45)

          #left image
        img_left=Image.open(r'C:\Users\Divya\Desktop\Face_rec\images\tr1.png')
        img_left=img_left.resize((650,700),Image.LANCZOS)
        self.photoimg_left=ImageTk.PhotoImage(img_left)

        f_lbl=Label(self.root,image=self.photoimg_left)
        f_lbl.place(x=0,y=55,width=650,height=700)

        #right image
        img_right=Image.open(r'C:\Users\Divya\Desktop\Face_rec\images\fa1.jpg')
        img_right=img_right.resize((950,700),Image.LANCZOS)
        self.photoimg_right=ImageTk.PhotoImage(img_right)

        f_lbl=Label(self.root,image=self.photoimg_right)
        f_lbl.place(x=650,y=55,width=950,height=700)

        face_btn=Button(f_lbl,text="FACE RECOGNITION",command=self.face_recog,cursor="hand2",font=('times new roman',12,'bold'),bg="red",fg="white")
        face_btn.place(x=350,y=460,width=200,height=40)

#+++++++++++++++++++++++face recognition+++++++++++++
    def face_recog(self):
        def draw_boundary(img,classifier,scaleFactor,minNeighbors,color,text,clf):
            gray_image=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
            features=classifier.detectMultiScale(gray_image,scaleFactor,minNeighbors)

            coords=[]

            for (x,y,w,h) in features:
                cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),3)
                id,predict=clf.predict(gray_image[y:y+h,x:x+w])
                confidence=int((100*(1-predict/300)))

                conn=mysql.connector.connect(host="localhost",username="root",password="2003@Divya",database="face_rec")
                my_cursor=conn.cursor()

                my_cursor.execute("select Name from student where student_id="+str(id))
                n=my_cursor.fetchone()
                n="+".join(n)

                my_cursor.execute("select rollno from student where student_id="+str(id))
                r=my_cursor.fetchone()
                r="+".join(r)

                my_cursor.execute("select dep from student where student_id="+str(id))
                d=my_cursor.fetchone()
                d="+".join(d)

                if confidence>77:
                    cv2.putText(img,f"Roll:{r}",(x,y-55),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)
                    cv2.putText(img,f"Name:{n}",(x,y-30),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)
                    cv2.putText(img,f"Department:{d}",(x,y-5),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)
                else:
                    cv2.rectangle(img,(x,y),(x+w,y+h),(0,0,255),3)
                    cv2.putText(img,"Unknown face",(x,y-5),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)

                coords=[x,y,w,h]
            
            return coords
        
        def recognize(img,clf,faceCascade):
            coords=draw_boundary(img,faceCascade,1.1,10,(255,25,255),"face",clf)
            return img
        faceCascade=cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
        clf=cv2.face.LBPHFaceRecognizer_create()  
        clf.read("classifier.xml")

        video_cap=cv2.VideoCapture(0)

        while True: 
            ret,img=video_cap.read()
            img=recognize(img,clf,faceCascade)
            cv2.imshow("welcome to face recognition",img)

            if cv2.waitKey(1)==13:
                break
        video_cap.release()
        cv2.destroyAllWindows()

if __name__=="__main__":
    root=Tk()
    obj=Face_recognition(root)
    root.mainloop()