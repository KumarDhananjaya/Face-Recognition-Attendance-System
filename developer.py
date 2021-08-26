from logging import exception
from re import escape
from tkinter import*
from tkinter import ttk
from typing import Pattern
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
import cv2 






class developer:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1920x1020")
        self.root.title("Face Recognition System")
        self.root.wm_iconbitmap("face1.ico") 


        title_lbl=Label(self.root,text="DEVELOPER",font=("times new roman",35,"bold"),bg="white",fg="BLACK")
        title_lbl.place(x=0,y=0,width=1530,height=45)


        img_top=Image.open(r"D:\Face Recognition\college_images\david-jorre-712468-unsplash.jpg")
        img_top=img_top.resize((1530,720),Image.ANTIALIAS)
        self.photoimg_top=ImageTk.PhotoImage(img_top)

        f_lbl=Label(self.root,image=self.photoimg_top)
        f_lbl.place(x=0,y=55,width=1530,height=720)

        #Frame
        main_frame= Frame(f_lbl,bd=3,bg="white")
        main_frame.place(x=100,y=50,width=1300,height=600)

        #thejas
        img_top1=Image.open(r"D:\Face Recognition\college_images\b8a704a7-9314-4869-aea6-386160344954.jpg")
        img_top1=img_top1.resize((300,300),Image.ANTIALIAS)
        self.photoimg_top1=ImageTk.PhotoImage(img_top1)

        f_lbl=Label(main_frame,image=self.photoimg_top1)
        f_lbl.place(x=775,y=100,width=300,height=500)

        #kumar
        img_top2=Image.open(r"D:\Face Recognition\college_images\b8a704a7-9314-4869-aea6-386160344954b8a704a7-9314-4869-aea6-386160344954.jpg")
        img_top2=img_top2.resize((300,300),Image.ANTIALIAS)
        self.photoimg_top2=ImageTk.PhotoImage(img_top2)

        f_lbl=Label(main_frame,image=self.photoimg_top2)
        f_lbl.place(x=230,y=100,width=300,height=500)


        deV_label=Label(main_frame,text=" HELLO WE ARE THE DEVELOPERS OF THIS PROJECT ",font=("times new roman",20,"bold"),bg="white")
        deV_label.place(x=300,y=20)
        deV_label=Label(main_frame,text=" S KUMAR DHANANJAYA ",font=("times new roman",17,"bold"),bg="white")
        deV_label.place(x=235,y=130)
        deV_label=Label(main_frame,text=" THEJAS M ",font=("times new roman",20,"bold"),bg="white")
        deV_label.place(x=850,y=130)
        deV_label=Label(main_frame,text=" CSE ",font=("times new roman",23,"bold"),bg="white")
        deV_label.place(x=320,y=510)
        deV_label=Label(main_frame,text=" ECE ",font=("times new roman",23,"bold"),bg="white")
        deV_label.place(x=890,y=510)














if  __name__ == "__main__":
    root=Tk()
    obj=developer(root)
    root.mainloop()