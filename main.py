from tkinter import *
from tkinter import ttk
from PIL import Image,ImageTk
from student import Student
import os
from train import Train
from Face_recognition import Face_recognition

class Face_Recognition_System:
    def __init__(self,root):
        self.root=root
        self.root.geometry('1530x790+0+0')
        self.root.title("Face Recognition System")

        img=Image.open(r'C:\Users\Divya\Desktop\Face_rec\images\im1.jpg')
        img=img.resize((500,130),Image.LANCZOS)
        self.photoimg1=ImageTk.PhotoImage(img)
        f_lb1=Label(self.root,image=self.photoimg1)
        f_lb1.place(x=0,y=0,width=500,height=130)

        img1=Image.open(r'C:\Users\Divya\Desktop\Face_rec\images\im2.jpg')
        img1=img1.resize((500,130),Image.LANCZOS)
        self.photoimg2=ImageTk.PhotoImage(img1)
        f_lb1=Label(self.root,image=self.photoimg2)
        f_lb1.place(x=500,y=0,width=500,height=130)

        img2=Image.open(r'C:\Users\Divya\Desktop\Face_rec\images\im3.jpg')
        img2=img.resize((500,130),Image.LANCZOS)
        self.photoimg3=ImageTk.PhotoImage(img2)
        f_lb1=Label(self.root,image=self.photoimg3)
        f_lb1.place(x=1000,y=0,width=500,height=130)

        img3=Image.open(r'C:\Users\Divya\Desktop\Face_rec\images\bg_im.png')
        img3=img3.resize((1530,710),Image.LANCZOS)
        self.photoimg4=ImageTk.PhotoImage(img3)

        bg_img=Label(self.root,image=self.photoimg4)
        bg_img.place(x=0,y=130,width=1530,height=710)

        title_lb1=Label(bg_img,text='FACE RECOGNITION ATTENDENCE SYSTEM SOFTWARE',font=('times new roman',35,'bold'),bg='white',fg='blue')
        title_lb1.place(x=0,y=0,width=1530,height=45)

        #student Button
        img4=Image.open(r'C:\Users\Divya\Desktop\Face_rec\images\im4.webp')
        img4=img4.resize((220,220),Image.LANCZOS)
        self.photoimg5=ImageTk.PhotoImage(img4)
        b1=Button(bg_img,image=self.photoimg5,command=self.stud_details,cursor='hand2')
        b1.place(x=200,y=100,width=220,height=220)

        b2=Button(bg_img,text='Student Details',command=self.stud_details,cursor='hand2',font=('times new roman',15,'bold'),bg='darkblue',fg='white')
        b2.place(x=200,y=300,width=220,height=40)

        #Detect Face button
        img5=Image.open(r'C:\Users\Divya\Desktop\Face_rec\images\im5.png')
        img5=img5.resize((220,220),Image.LANCZOS)
        self.photoimg6=ImageTk.PhotoImage(img5)
        b1=Button(bg_img,command=self.face_data,image=self.photoimg6,cursor='hand2')
        b1.place(x=500,y=100,width=220,height=220)

        b2=Button(bg_img,text='Face Detector',command=self.face_data,cursor='hand2',font=('times new roman',15,'bold'),bg='darkblue',fg='white')
        b2.place(x=500,y=300,width=220,height=40)

        #attendence
        img6=Image.open(r'C:\Users\Divya\Desktop\Face_rec\images\im6.jpg')
        img6=img6.resize((220,220),Image.LANCZOS)
        self.photoimg7=ImageTk.PhotoImage(img6)
        b1=Button(bg_img,image=self.photoimg7,cursor='hand2')
        b1.place(x=800,y=100,width=220,height=220)

        b2=Button(bg_img,text='Attendence',cursor='hand2',font=('times new roman',15,'bold'),bg='darkblue',fg='white')
        b2.place(x=800,y=300,width=220,height=40)

        #HelpDesk
        img7=Image.open(r'C:\Users\Divya\Desktop\Face_rec\images\im7.jpg')
        img7=img7.resize((220,220),Image.LANCZOS)
        self.photoimg8=ImageTk.PhotoImage(img7)
        b1=Button(bg_img,image=self.photoimg8,cursor='hand2')
        b1.place(x=1100,y=100,width=220,height=220)

        b2=Button(bg_img,text='Chatbot',cursor='hand2',font=('times new roman',15,'bold'),bg='darkblue',fg='white')
        b2.place(x=1100,y=300,width=220,height=40)

        #Train Face Button
        img8=Image.open(r'C:\Users\Divya\Desktop\Face_rec\images\im8.jpg')
        img8=img8.resize((220,220),Image.LANCZOS)
        self.photoimg9=ImageTk.PhotoImage(img8)
        b1=Button(bg_img,command=self.train_data,image=self.photoimg9,cursor='hand2')
        b1.place(x=200,y=400,width=220,height=220)

        b2=Button(bg_img,command=self.train_data,text='Train Model',cursor='hand2',font=('times new roman',15,'bold'),bg='darkblue',fg='white')
        b2.place(x=200,y=600,width=220,height=40)

        #Photos face
        img9=Image.open(r'C:\Users\Divya\Desktop\Face_rec\images\im11.jpg')
        img9=img9.resize((220,220),Image.LANCZOS)
        self.photoimg10=ImageTk.PhotoImage(img9)
        b1=Button(bg_img,command=self.open_img,image=self.photoimg10,cursor='hand2')
        b1.place(x=500,y=400,width=220,height=220)

        b2=Button(bg_img,text='Photos',cursor='hand2',command=self.open_img,font=('times new roman',15,'bold'),bg='darkblue',fg='white')
        b2.place(x=500,y=600,width=220,height=40)

        #developer
        img10=Image.open(r'C:\Users\Divya\Desktop\Face_rec\images\im9.jpg')
        img10=img10.resize((220,220),Image.LANCZOS)
        self.photoimg11=ImageTk.PhotoImage(img10)
        b1=Button(bg_img,image=self.photoimg11,cursor='hand2')
        b1.place(x=800,y=400,width=220,height=220)

        b2=Button(bg_img,text='Developer',cursor='hand2',font=('times new roman',15,'bold'),bg='darkblue',fg='white')
        b2.place(x=800,y=600,width=220,height=40)

        #Exit
        img11=Image.open(r'C:\Users\Divya\Desktop\Face_rec\images\im10.jpg')
        img11=img11.resize((220,220),Image.LANCZOS)
        self.photoimg12=ImageTk.PhotoImage(img11)
        b1=Button(bg_img,image=self.photoimg12,cursor='hand2')
        b1.place(x=1100,y=400,width=220,height=220)

        b2=Button(bg_img,text='Exit',cursor='hand2',font=('times new roman',15,'bold'),bg='darkblue',fg='white')
        b2.place(x=1100,y=600,width=220,height=40)

    def open_img(self):
        os.startfile('data')
        #functions buttons
    def stud_details(self):
        self.new_window=Toplevel(self.root)
        self.app=Student(self.new_window)

    def train_data(self):
        self.new_window=Toplevel(self.root)
        self.app=Train(self.new_window)

    def face_data(self):
        self.new_window=Toplevel(self.root)
        self.app=Face_recognition(self.new_window)
        
        
if __name__=="__main__":
    root=Tk()
    obj=Face_Recognition_System(root)
    root.mainloop()
