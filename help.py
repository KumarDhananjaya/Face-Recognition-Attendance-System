from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
import mysql.connector
from cv2 import cv2

class Help:
    def __init__(self, root):
        self.root=root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recognition System") 
        self.root.wm_iconbitmap("face1.ico") 

        title_lbl = Label(self.root, text="HELP DESK", font=("times new roman",35,"bold"),bg="white",fg="black")
        title_lbl.place(x=0,y=0,width=1530,height=45)


        img3 = Image.open(r"D:\Face Recognition\college_images\sys.jpeg")
        img3 = img3.resize((1530,710),Image.ANTIALIAS)
        self.photoimg3 = ImageTk.PhotoImage(img3)

        
        bg_img = Label(self.root,image = self.photoimg3)
        bg_img.place(x=0,y=50,width=1530,height=710)

        dev_label = Label(bg_img, text="Email: kumar62.shivu@gmail.com", font=("times new roman",35,"bold"),bg="black",fg="burlywood")
        dev_label.place(x=400,y=160 )
        dev_label = Label(bg_img, text="Email: thejasm52@gmail.com", font=("times new roman",35,"bold"),bg="black",fg="burlywood")
        dev_label.place(x=400,y=250 )

       

if __name__ == "__main__":
    root = Tk()
    obj = Help(root)
    root.mainloop()