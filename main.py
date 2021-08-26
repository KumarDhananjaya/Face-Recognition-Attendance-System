import tkinter
from developer import developer
from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
from student import Student
import os
from developer import developer
from attendence import Attendance
from student import Student
from train import Train
from help import Help
from face_recognition import Face_Recognition
from chatbot import ChatBot


class Face_Recognition_System:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1920x1020")
        self.root.title("Face Recognition System")
        self.root.wm_iconbitmap("face1.ico") 
        
        #Image 1
        img=Image.open(r"D:\Face Recognition\college_images\MITT.jpg")
        img=img.resize((500,130),Image.ANTIALIAS)
        self.photoimg=ImageTk.PhotoImage(img)

        f_lbl=Label(self.root,image=self.photoimg)
        f_lbl.place(x=0,y=0,width=500,height=130)
        
        #Image 2
        img1=Image.open(r"D:\Face Recognition\college_images\facialrecognition.png")
        img1=img1.resize((500,130),Image.ANTIALIAS)
        self.photoimg1=ImageTk.PhotoImage(img1)

        f_lbl=Label(self.root,image=self.photoimg1)
        f_lbl.place(x=500,y=0,width=500,height=130)

        #Image 3
        img2=Image.open(r"D:\Face Recognition\college_images\campusview.jpg")
        img2=img2.resize((550,130),Image.ANTIALIAS)
        self.photoimg2=ImageTk.PhotoImage(img2)

        f_lbl=Label(self.root,image=self.photoimg2)
        f_lbl.place(x=1000,y=0,width=550,height=130)

        #background Image
        img3=Image.open(r"D:\Face Recognition\college_images\bg5.jpg")
        img3=img3.resize((1530,710),Image.ANTIALIAS)
        self.photoimg3=ImageTk.PhotoImage(img3)

        bg_img=Label(self.root,image=self.photoimg3)
        bg_img.place(x=0,y=130,width=1530,height=710)


        title_lbl=Label(bg_img,text="FACE RECOGNITION ATTENDANCE SYSTEM SOFTWARE",font=("times new roman",35,"bold"),bg="white",fg="brown")
        title_lbl.place(x=0,y=0,width=1530,height=45)



        #student button
        img4=Image.open(r"D:\Face Recognition\college_images\studentdet.png")
        img4=img4.resize((220,220),Image.ANTIALIAS)
        self.photoimg4=ImageTk.PhotoImage(img4)

        b1=Button(bg_img,image=self.photoimg4,command=self.student_details, cursor="hand2")
        b1.place(x=200,y=100,width=220,height=220)

        b1=Button(bg_img,text="Student Details",command=self.student_details,cursor="hand2",font=("times new roman",15,"bold"),bg="darkblue",fg="white")
        b1.place(x=200,y=300,width=220,height=40)

        
        #Detect face button
        img5=Image.open(r"D:\Face Recognition\college_images\biom.png")
        img5=img5.resize((220,220),Image.ANTIALIAS)
        self.photoimg5=ImageTk.PhotoImage(img5)

        b1=Button(bg_img,image=self.photoimg5,cursor="hand2",command=self.face_data)
        b1.place(x=500,y=100,width=220,height=220)

        b1=Button(bg_img,text="Face Detector",command=self.face_data,cursor="hand2",font=("times new roman",15,"bold"),bg="darkblue",fg="white")
        b1.place(x=500,y=300,width=220,height=40)


         #Attendence Face button
        img6=Image.open(r"D:\Face Recognition\college_images\attend.jpg")
        img6=img6.resize((220,220),Image.ANTIALIAS)
        self.photoimg6=ImageTk.PhotoImage(img6)

        b1=Button(bg_img,image=self.photoimg6,cursor="hand2",command=self.attendence_data)
        b1.place(x=800,y=100,width=220,height=220)

        b1=Button(bg_img,text="Attendance",command=self.attendence_data,cursor="hand2",font=("times new roman",15,"bold"),bg="darkblue",fg="white")
        b1.place(x=800,y=300,width=220,height=40)


        #Chatbot button
        img7=Image.open(r"D:\Face Recognition\college_images\chat.jpg")
        img7=img7.resize((220,220),Image.ANTIALIAS)
        self.photoimg7=ImageTk.PhotoImage(img7)

        b1=Button(bg_img,image=self.photoimg7,command=self.chatbot_data,cursor="hand2")
        b1.place(x=1100,y=100,width=220,height=220)

        b1=Button(bg_img,text="ChatBot",cursor="hand2",command=self.chatbot_data,font=("times new roman",15,"bold"),bg="darkblue",fg="white")
        b1.place(x=1100,y=300,width=220,height=40)


        #Train Face button
        img8=Image.open(r"D:\Face Recognition\college_images\train1.jpg")
        img8=img8.resize((220,220),Image.ANTIALIAS)
        self.photoimg8=ImageTk.PhotoImage(img8)

        b1=Button(bg_img,image=self.photoimg8,cursor="hand2",command=self.train_data)
        b1.place(x=200,y=380,width=220,height=220)

        b1=Button(bg_img,text="Train Data",command=self.train_data,cursor="hand2",font=("times new roman",15,"bold"),bg="darkblue",fg="white")
        b1.place(x=200,y=580,width=220,height=40)


        #photos Face button
        img9=Image.open(r"D:\Face Recognition\college_images\friends.jpg")
        img9=img9.resize((220,220),Image.ANTIALIAS)
        self.photoimg9=ImageTk.PhotoImage(img9)

        b1=Button(bg_img,image=self.photoimg9,command=self.open_img,cursor="hand2")
        b1.place(x=500,y=380,width=220,height=220)

        b1=Button(bg_img,text="Photos",command=self.open_img,cursor="hand2",font=("times new roman",15,"bold"),bg="darkblue",fg="white")
        b1.place(x=500,y=580,width=220,height=40)


        #Developer face button
        img10=Image.open(r"D:\Face Recognition\college_images\develop.jpg")
        img10=img10.resize((220,220),Image.ANTIALIAS)
        self.photoimg10=ImageTk.PhotoImage(img10)

        b1=Button(bg_img,image=self.photoimg10,cursor="hand2",command=self.developer_data)
        b1.place(x=800,y=380,width=220,height=220)

        b1=Button(bg_img,text="Developer",command=self.developer_data,cursor="hand2",font=("times new roman",15,"bold"),bg="darkblue",fg="white")
        b1.place(x=800,y=580,width=220,height=40)



        #Exit Face button
        img11=Image.open(r"D:\Face Recognition\college_images\exit2.jpg")
        img11=img11.resize((220,220),Image.ANTIALIAS)
        self.photoimg11=ImageTk.PhotoImage(img11)

        b1=Button(bg_img,image=self.photoimg11,cursor="hand2",command=self.iExit)
        b1.place(x=1100,y=380,width=220,height=220)

        b1=Button(bg_img,text="Exit Face",command=self.iExit,cursor="hand2",font=("times new roman",15,"bold"),bg="darkblue",fg="white")
        b1.place(x=1100,y=580,width=220,height=40)

    def open_img (self):
        os.startfile("data")


    def iExit(self):
          self.iExit=tkinter.messagebox.askyesno("Face Recognition","Do you want to exit this project",parent=self.root)
          if self.iExit>0:
               self.root.destroy()
          else:
               return




    #============== Function Button ====================
    def student_details(self):
         self.new_window=Toplevel(self.root)
         self.app=Student(self.new_window)

    def face_data(self):
         self.new_window=Toplevel(self.root)
         self.app=Face_Recognition(self.new_window)

    def train_data(self):
         self.new_window=Toplevel(self.root)
         self.app=Train(self.new_window)

    def attendence_data(self):
         self.new_window=Toplevel(self.root)
         self.app=Attendance(self.new_window)
     
    def developer_data(self):
         self.new_window=Toplevel(self.root)
         self.app=developer(self.new_window)

    #def help_data(self):
         #self.new_window=Toplevel(self.root)
         #self.app=Help(self.new_window)


    def chatbot_data(self):
         self.new_window=Toplevel(self.root)
         self.app=ChatBot(self.new_window)

     


  









if __name__ == "__main__":
    root=Tk()
    obj= Face_Recognition_System(root)
    root.mainloop()
        