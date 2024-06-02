from tkinter import *
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
import cv2

class Student:
    def __init__(self,root):
        self.root=root
        self.root.geometry('1530x790+0+0')
        self.root.title("Face Recognition System")

        self.var_dep=StringVar()
        self.var_course=StringVar()
        self.var_year=StringVar()
        self.var_semester=StringVar()
        self.var_stu_id=StringVar()
        self.var_name=StringVar()
        self.var_div=StringVar()
        self.var_roll=StringVar()
        self.var_gender=StringVar()
        self.var_dob=StringVar()
        self.var_email=StringVar()
        self.var_phone=StringVar()
        

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

        title_lb1=Label(bg_img,text='STUDENT MANAGEMENT SYSTEM',font=('times new roman',35,'bold'),bg='white',fg='red')
        title_lb1.place(x=0,y=0,width=1530,height=45)


        main_frame=Frame(bg_img,bd=2,bg='white')
        main_frame.place(x=10,y=55,width=1500,height=600)
        #left label
        left_frame=LabelFrame(main_frame,bd=2,bg='white',relief=RIDGE,text='Student Details',font=('times new roman',12,'bold'))
        left_frame.place(x=10,y=10,width=760,height=580)

        imgl=Image.open(r'C:\Users\Divya\Desktop\Face_rec\images\stu1.jpg')
        imgl=imgl.resize((740,130),Image.LANCZOS)
        self.photoimgl=ImageTk.PhotoImage(imgl)
        f_lb1=Label(left_frame,image=self.photoimgl)
        f_lb1.place(x=5,y=0,width=740,height=130)

        #current course
        course_frame=LabelFrame(left_frame,bd=2,bg='white',relief=RIDGE,text='Current Course information',font=('times new roman',12,'bold'))
        course_frame.place(x=5,y=135,width=740,height=115)
        #department
        dept_label=Label(course_frame,text='Department',font=('times new roman',12,'bold'),bg="white")
        dept_label.grid(row=0,column=0,padx=10)

        dept_combo=ttk.Combobox(course_frame,textvariable=self.var_dep,font=('times new roman',12),state='readonly')
        dept_combo['values']=('Select Department','Computer science','Electronics','Mechanical')
        dept_combo.current(0)
        dept_combo.grid(row=0,column=1,padx=2,pady=10,sticky=W)

        #course
        cou_label=Label(course_frame,text='Course',font=('times new roman',12,'bold'),bg="white")
        cou_label.grid(row=0,column=2,padx=10)

        cou_combo=ttk.Combobox(course_frame,textvariable=self.var_course,font=('times new roman',12),state='readonly')
        cou_combo['values']=('Select Course','BE','Mtech','MCA')
        cou_combo.current(0)
        cou_combo.grid(row=0,column=3,padx=2,pady=10)
        #year
        year_label=Label(course_frame,text='Year',font=('times new roman',12,'bold'),bg="white")
        year_label.grid(row=1,column=0,padx=10,sticky=W)

        year_combo=ttk.Combobox(course_frame,textvariable=self.var_year,font=('times new roman',12),state='readonly')
        year_combo['values']=('Select Year','2021-22','2022-23','2023-24')
        year_combo.current(0)
        year_combo.grid(row=1,column=1,padx=2,pady=10)
        #semester
        sem_label=Label(course_frame,text='Semester',font=('times new roman',12,'bold'),bg="white")
        sem_label.grid(row=1,column=2,padx=10,sticky=W)

        sem_combo=ttk.Combobox(course_frame,textvariable=self.var_semester,font=('times new roman',12),state='readonly')
        sem_combo['values']=('Select Semester','1','2','3','4')
        sem_combo.current(0)
        sem_combo.grid(row=1,column=3,padx=2,pady=10,sticky=W)
       
        #class course
        class_frame=LabelFrame(left_frame,bd=2,bg='white',relief=RIDGE,text='Class Student information',font=('times new roman',12,'bold'))
        class_frame.place(x=5,y=250,width=740,height=300)
        #student label

        stuid_label=Label(class_frame,text='StudentID No',font=('times new roman',12,'bold'),bg="white")
        stuid_label.grid(row=0,column=0,padx=10,sticky=W)

        stuid_entry=ttk.Entry(class_frame,textvariable=self.var_stu_id,width=20,font=('times new roman',12,'bold'))
        stuid_entry.grid(row=0,column=1,padx=10,sticky=W)

        #name
        stuname_label=Label(class_frame,text='Student name',font=('times new roman',12,'bold'),bg="white")
        stuname_label.grid(row=0,column=2,padx=10,sticky=W)

        stuname_entry=ttk.Entry(class_frame,textvariable=self.var_name,width=20,font=('times new roman',12,'bold'))
        stuname_entry.grid(row=0,column=3,padx=10,sticky=W)

        #class division
        div_label=Label(class_frame,text='Division',font=('times new roman',12,'bold'),bg="white")
        div_label.grid(row=1,column=0,padx=10,sticky=W)

        div_combo=ttk.Combobox(class_frame,textvariable=self.var_div,font=('times new roman',12),width=18,state='readonly')
        div_combo['values']=('Select Division','A','B','C','D')
        div_combo.current(0)
        div_combo.grid(row=1,column=1,padx=10,pady=10,sticky=W)

        #roll no
        roll_label=Label(class_frame,text='Roll No',font=('times new roman',12,'bold'),bg="white")
        roll_label.grid(row=1,column=2,padx=10,sticky=W)

        roll_entry=ttk.Entry(class_frame,width=20,textvariable=self.var_roll,font=('times new roman',12,'bold'))
        roll_entry.grid(row=1,column=3,padx=10,sticky=W)

        #gender
        gen_label=Label(class_frame,text='Gender',font=('times new roman',12,'bold'),bg="white")
        gen_label.grid(row=2,column=0,padx=10,sticky=W)

        gen_combo=ttk.Combobox(class_frame,textvariable=self.var_gender,font=('times new roman',12),width=18,state='readonly')
        gen_combo['values']=('Select Gender','female','Male')
        gen_combo.current(0)
        gen_combo.grid(row=2,column=1,padx=10,pady=10,sticky=W)

        #dob
        dob_label=Label(class_frame,text='DOB',font=('times new roman',12,'bold'),bg="white")
        dob_label.grid(row=2,column=2,padx=10,sticky=W)

        dob_entry=ttk.Entry(class_frame,textvariable=self.var_dob,width=20,font=('times new roman',12,'bold'))
        dob_entry.grid(row=2,column=3,padx=10,sticky=W)

        #email
        email_label=Label(class_frame,text='Email',font=('times new roman',12,'bold'),bg="white")
        email_label.grid(row=3,column=0,padx=10,sticky=W)

        email_entry=ttk.Entry(class_frame,textvariable=self.var_email,width=20,font=('times new roman',12,'bold'))
        email_entry.grid(row=3,column=1,padx=10,sticky=W)

        #Phone no
        phone_label=Label(class_frame,text='Phone Number',font=('times new roman',12,'bold'),bg="white")
        phone_label.grid(row=3,column=2,padx=10,sticky=W)

        phone_entry=ttk.Entry(class_frame,width=20,textvariable=self.var_phone,font=('times new roman',12,'bold'))
        phone_entry.grid(row=3,column=3,padx=10,sticky=W)

        #radio
        self.var_radio1=StringVar()
        radio_button1=ttk.Radiobutton(class_frame,variable=self.var_radio1,text="Take Photo sample",value='Yes')
        radio_button1.grid(row=4,column=0,padx=10,pady=10)

        radio_button2=ttk.Radiobutton(class_frame,variable=self.var_radio1,text="No Photo sample",value='No')
        radio_button2.grid(row=4,column=1,padx=10,pady=10)

        #Button Frame
        btn_frame=Frame(class_frame,bd=2,relief=RIDGE,bg='white')
        btn_frame.place(x=5,y=180,width=720,height=35)

        save_btn=Button(btn_frame,text="Save",command=self.add_data,width=19,font=('times new roman',12,'bold'),bg="blue",fg="white")
        save_btn.grid(row=0,column=0)

        upd_btn=Button(btn_frame,text="Update",command=self.update_data,width=19,font=('times new roman',12,'bold'),bg="blue",fg="white")
        upd_btn.grid(row=0,column=1)

        del_btn=Button(btn_frame,text="Delete",width=19,command=self.delete_data,font=('times new roman',12,'bold'),bg="blue",fg="white")
        del_btn.grid(row=0,column=2)

        reset_btn=Button(btn_frame,text="Reset",command=self.reset_data,width=19,font=('times new roman',12,'bold'),bg="blue",fg="white")
        reset_btn.grid(row=0,column=3)

        btn_frame1=Frame(class_frame,bd=2,relief=RIDGE,bg='white')
        btn_frame1.place(x=5,y=220,width=720,height=35)

        take_photo_btn=Button(btn_frame1,text="Take Photo Sample",command=self.generate_data,width=40,font=('times new roman',12,'bold'),bg="blue",fg="white")
        take_photo_btn.grid(row=1,column=0)

        save_btn=Button(btn_frame1,text="Update Photo Sample",width=40,font=('times new roman',12,'bold'),bg="blue",fg="white")
        save_btn.grid(row=1,column=1)

                        
        #right label
        right_frame=LabelFrame(main_frame,bd=2,bg='white',relief=RIDGE,text='Student Details',font=('times new roman',12,'bold'))
        right_frame.place(x=780,y=10,width=690,height=580)

        imgr=Image.open(r'C:\Users\Divya\Desktop\Face_rec\images\stu2.jpg')
        imgr=imgr.resize((740,130),Image.LANCZOS)
        self.photoimgr=ImageTk.PhotoImage(imgr)
        f_lbr=Label(right_frame,image=self.photoimgr)
        f_lbr.place(x=5,y=0,width=680,height=130)

        search_frame=LabelFrame(right_frame,bd=2,bg='white',relief=RIDGE,text='Search System',font=('times new roman',12,'bold'))
        search_frame.place(x=5,y=135,width=670,height=65)

        search_label=Label(search_frame,text='Search by:',font=('times new roman',12,'bold'),bg="red",fg="white")
        search_label.grid(row=0,column=0,padx=5,pady=5,sticky=W)

        search_combo=ttk.Combobox(search_frame,font=('times new roman',12),width=18,state='readonly')
        search_combo['values']=('Select','Roll no','Phone no')
        search_combo.current(0)
        search_combo.grid(row=0,column=1,padx=10,pady=10,sticky=W)

        search_entry=ttk.Entry(search_frame,width=18,font=('times new roman',12,'bold'))
        search_entry.grid(row=0,column=2,padx=10,sticky=W)

        search_btn=Button(search_frame,text="Search",width=10,font=('times new roman',12,'bold'),bg="blue",fg="white")
        search_btn.grid(row=0,column=3,padx=5,sticky=W)

        show_all_btn=Button(search_frame,text="Show All",width=10,font=('times new roman',12,'bold'),bg="blue",fg="white")
        show_all_btn.grid(row=0,column=4,padx=5,sticky=W)

        #tableframe

        table_frame=Frame(right_frame,bd=2,bg='white',relief=RIDGE)
        table_frame.place(x=5,y=200,width=670,height=350)

        scroll_x=ttk.Scrollbar(table_frame,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(table_frame,orient=VERTICAL)

        self.stu_table=ttk.Treeview(table_frame,columns=("Dep","course","year","Semester","id","name","div","roll","gender","dob","email","phone","photo"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)

        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)
        scroll_x.config(command=self.stu_table.xview)
        scroll_y.config(command=self.stu_table.yview)

        self.stu_table.heading("Dep",text="Department")
        self.stu_table.heading("course",text="Course")
        self.stu_table.heading("year",text="Year")
        self.stu_table.heading("Semester",text="Semester")
        self.stu_table.heading("id",text="Id")
        self.stu_table.heading("name",text="Name")
        self.stu_table.heading("div",text="Division")
        self.stu_table.heading("roll",text="Roll no")
        self.stu_table.heading("gender",text="Gender")
        self.stu_table.heading("dob",text="DOB")
        self.stu_table.heading("email",text="Email")
        self.stu_table.heading("phone",text="Phone")
        self.stu_table.heading("photo",text="Photo")
        self.stu_table["show"]="headings"

        self.stu_table.column("Dep",width=100)
        self.stu_table.column("course",width=100)
        self.stu_table.column("year",width=100)
        self.stu_table.column("Semester",width=100)
        self.stu_table.column("id",width=100)
        self.stu_table.column("name",width=100)
        self.stu_table.column("div",width=100)
        self.stu_table.column("roll",width=100)
        self.stu_table.column("gender",width=100)
        self.stu_table.column("dob",width=100)
        self.stu_table.column("email",width=100)
        self.stu_table.column("phone",width=100)
        self.stu_table.column("photo",width=100)

        self.stu_table.pack(fill=BOTH,expand=1)
        self.stu_table.bind("<ButtonRelease>",self.get_cursor)
        self.fetch_data()
        
    #+++++++++++++++++++function declaration+++++++++++++++++++
    def add_data(self):
        if self.var_dep.get()=="Select Department" or self.var_name.get()=="" or self.var_stu_id.get()=="":
            messagebox.showerror("Error","All fields are required",parent=self.root)
        else:
            try:
                conn=mysql.connector.connect(host="localhost",username="root",password="2003@Divya",database="face_rec")
                my_cursor=conn.cursor()
                my_cursor.execute("insert into student values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(
                    self.var_dep.get(),
                    self.var_course.get(),
                    self.var_year.get(),
                    self.var_semester.get(),
                    self.var_stu_id.get(),
                    self.var_name.get(),
                    self.var_div.get(),
                    self.var_roll.get(),
                    self.var_gender.get(),
                    self.var_dob.get(),
                    self.var_email.get(),
                    self.var_phone.get(),
                    self.var_radio1.get()

                ))
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Success","Student details has been added successfully",parent=self.root)
            except Exception as es:
                messagebox.showerror("Error",f"Due to :{str(es)}",parent=self.root)

#++++++++++++++++++++++fetch data++++++++++++++++++++++++
    def fetch_data(self):
        conn=mysql.connector.connect(host="localhost",username="root",password="2003@Divya",database="face_rec")
        my_cursor=conn.cursor()
        my_cursor.execute("select * from student")
        data=my_cursor.fetchall()

        if len(data)!=0:
            self.stu_table.delete(*self.stu_table.get_children())
            for i in data:
                self.stu_table.insert("",END,values=i)
            conn.commit()
        conn.close()


#++++++++++++++++++++++++get cursor++++++++++++++
    def get_cursor(self,event=""):
        cursor_focus=self.stu_table.focus()
        content=self.stu_table.item(cursor_focus)
        data=content["values"]

        self.var_dep.set(data[0])
        self.var_course.set(data[1])
        self.var_year.set(data[2])
        self.var_semester.set(data[3])
        self.var_stu_id.set(data[4])
        self.var_name.set(data[5])
        self.var_div.set(data[6])
        self.var_roll.set(data[7])
        self.var_gender.set(data[8])
        self.var_dob.set(data[9])
        self.var_email.set(data[10])
        self.var_phone.set(data[11])
        self.var_radio1.set(data[12])

#update
    def update_data(self):
        if self.var_dep.get()=="Select Department" or self.var_name.get()=="" or self.var_stu_id.get()=="":
                messagebox.showerror("Error","All fields are required",parent=self.root)
        else:
            try:
                Update=messagebox.askyesno('Update','Do you want to update this student details',parent=self.root)
                if Update>0:
                    conn=mysql.connector.connect(host="localhost",username="root",password="2003@Divya",database="face_rec")
                    my_cursor=conn.cursor()
                    my_cursor.execute("update student set Dep=%s,course=%s,year=%s,semester=%s,Name=%s,Division=%s,rollno=%s,gender=%s,Dob=%s,email=%s,Phone=%s,Photosample=%s where Student_id=%s",(
                        self.var_dep.get(),
                        self.var_course.get(),
                        self.var_year.get(),
                        self.var_semester.get(),
                        self.var_name.get(),
                        self.var_div.get(),
                        self.var_roll.get(),
                        self.var_gender.get(),
                        self.var_dob.get(),
                        self.var_email.get(),
                        self.var_phone.get(),
                        self.var_radio1.get(),
                        self.var_stu_id.get()
                    ))
                else:
                    if not Update:
                        return
                messagebox.showinfo('Success','Student details successfully updated',parent=self.root)
                conn.commit()
                self.fetch_data()
                conn.close()
            except Exception as e:
                messagebox.showerror('Error',f'Due to:{str(e)}',parent=self.root)

#++++++++++++delete function+++++++++++++++++   
    def delete_data(self):
        if self.var_stu_id.get()=="":
            messagebox.showerror("Error","Student id must be reqired",parent=self.root)
        else:
            try:
                delete=messagebox.askyesno("Student Delete page","Do you want to delete this student",parent=self.root)
                if delete>0:      
                    conn=mysql.connector.connect(host="localhost",username="root",password="2003@Divya",database="face_rec")
                    my_cursor=conn.cursor()
                    sql="delete from student where student_id=%s"
                    val=(self.var_stu_id.get(),)
                    my_cursor.execute(sql,val)
                else:
                    if not delete:
                        return

                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Delete","Successfully deleted student details",parent=self.root)     
            except Exception as e:
                messagebox.showerror('Error',f'Due to:{str(e)}',parent=self.root)

#++++++++++++++++++rerset data+++++++++++++++++
    def reset_data(self):
        self.var_dep.set("Select Department")
        self.var_course.set("Select Course")
        self.var_year.set("Select Year")
        self.var_semester.set("Select Semester")
        self.var_stu_id.set("")
        self.var_name.set("")
        self.var_div.set("Select Division")
        self.var_roll.set("")
        self.var_gender.set("Select Gender")
        self.var_dob.set("")
        self.var_email.set("")
        self.var_phone.set("")
        self.var_radio1.set("")

#++++++++++++++++++++++Generate data set take photo++++++++++++++++++++++
    def generate_data(self) :
        if self.var_dep.get()=="Select Department" or self.var_name.get()=="" or self.var_stu_id.get()=="":
                messagebox.showerror("Error","All fields are required",parent=self.root)
        else:
            try:
                conn=mysql.connector.connect(host="localhost",username="root",password="2003@Divya",database="face_rec")
                my_cursor=conn.cursor()
                my_cursor.execute("Select * from student")
                my_result=my_cursor.fetchall()
                id=0
                for x in my_result:
                    id+=1
                my_cursor.execute("update student set Dep=%s,course=%s,year=%s,semester=%s,Name=%s,Division=%s,rollno=%s,gender=%s,Dob=%s,email=%s,Phone=%s,Photosample=%s where Student_id=%s",(
                        self.var_dep.get(),
                        self.var_course.get(),
                        self.var_year.get(),
                        self.var_semester.get(),
                        self.var_name.get(),
                        self.var_div.get(),
                        self.var_roll.get(),
                        self.var_gender.get(),
                        self.var_dob.get(),
                        self.var_email.get(),
                        self.var_phone.get(),
                        self.var_radio1.get(),
                        self.var_stu_id.get()==id+1
                    ))
                conn.commit()
                self.fetch_data()
                self.reset_data()
                conn.close()
                #+++++++++++++++++++++++++++++++load predefined data on face frontals from open cv+++++++++
                face_classifier=cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
                def face_cropped(img):
                    gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
                    faces=face_classifier.detectMultiScale(gray,1.3,5)
                    #scaling factor 1.3  minneighbour  5
                    for (x,y,w,h) in faces:
                        face_cropped=img[y:y+h,x:x+w]
                        return face_cropped
                    
                cap=cv2.VideoCapture(0)
                img_id=0
                while True:
                    ret,my_frame=cap.read()
                    if face_cropped(my_frame) is not None:
                        img_id+=1
                        face=cv2.resize(face_cropped(my_frame),(450,450))
                        face=cv2.cvtColor(face,cv2.COLOR_BGR2GRAY)
                        file_name_path="data/user."+str(id)+"."+str(img_id)+".jpg"
                        cv2.imwrite(file_name_path,face)
                        cv2.putText(face,str(img_id),(50,503),cv2.FONT_HERSHEY_COMPLEX,2,(0,255,0),2)
                        cv2.imshow("cropped face",face)
                    if cv2.waitKey(1)==13 or int(img_id)==100:
                            break
                cap.release()
                cv2.destroyAllWindows()
                messagebox.showinfo("Result","Generating data set completed")
            except Exception as e:
                messagebox.showerror('Error',f'Due to:{str(e)}',parent=self.root)

                  




if __name__=="__main__":
    root=Tk()
    obj=Student(root)
    root.mainloop()
    