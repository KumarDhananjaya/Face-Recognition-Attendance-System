from tkinter import*
from tkinter import ttk
import tkinter
from PIL import Image,ImageTk #pip install pillow


class ChatBot:
    def __init__(self,root):
        self.root=root
        self.root.title("CHATBOT")
        self.root.geometry("730x680+0+0")
        self.root.wm_iconbitmap("face1.ico") 

        main_frame=Frame(self.root,bd=4,bg="powder blue",width=610)
        main_frame.pack()

        img_chat=Image.open("chat.jpg")
        img_chat=img_chat.resize((200,70),Image.ANTIALIAS)
        self.photoimg=ImageTk.PhotoImage(img_chat)

        Title_lbl=Label(main_frame,bd=3,relief=RAISED,anchor='nw',width=720,compound=LEFT,image=self.photoimg,text="START CHATTING",font=('arial',30,'bold'),bg="white",fg="green")
        Title_lbl.pack(side=TOP)

        self.scroll_y=ttk.Scrollbar(main_frame,orient=VERTICAL)
        self.text=Text(main_frame,width=65,height=20,bd=20,relief=RAISED,font=("arial",14),yscrollcommand=self.scroll_y.set)
        self.scroll_y.pack(side=RIGHT,fill=Y)
        self.text.pack()


        Btn_frame=Frame(self.root,bd=4,bg="white",width=730)
        Btn_frame.pack()

        label_l=Label(Btn_frame,text="Type Something",font=('arial',14,'bold'),bg="white",fg="green")
        label_l.grid(row=0,column=0,padx=5,sticky=W)



        self.entry=StringVar()
        self.entry1=ttk.Entry(Btn_frame,textvariable=self.entry,width=40,font=("times new roman",16,"bold"))
        self.entry1.grid(row=0,column=1,padx=5,sticky=W)

        self.send=Button(Btn_frame,text="SEND>>",command=self.send,font=("arial",15,"bold"),width=8,bg="green")
        self.send.grid(row=0,column=2,padx=5,sticky=W)


        self.clear=Button(Btn_frame,command=self.clear,text="Clear Data",font=("arial",15,"bold"),width=8,bg="black",fg="white")
        self.clear.grid(row=1,column=0,padx=5,sticky=W)


        self.msg=""
        self.label_1=Label(Btn_frame,text=self.msg,font=('arial',14,'bold'),bg="white",fg="red")
        self.label_1.grid(row=1,column=1,padx=5,sticky=W)


    #======================function declaration====================
    def enter_func(self,event):
        self.send.invoke()
        self.entry.set('')

    def clear(self):
        self.text.delete('1.0',END)
        self.entry.set('')


    def send(self):
        
        send='\t\t\t\t\t'+' You: '+self.entry.get()
        self.text.insert(END,'\n'+send)
        self.text.yview(END)
        

        if (self.entry.get()==''):
            self.msg="Please Enter Something" 
            self.label_1.config(text=self.msg,fg="red")

        else:
            self.msg=""
            self.label_1.config(text=self.msg,fg="red")

        if (self.entry.get()=='hello'):
            self.text.insert(END,'\n\n'+'Bot: Hi')


        elif (self.entry.get()=='hi'):
            self.text.insert(END,'\n\n'+'Bot: Hello')


        elif (self.entry.get()=='how are you'):
            self.text.insert(END,'\n\n'+'Bot: Fine and You')

        elif (self.entry.get()=='fantastic'):
            self.text.insert(END,'\n\n'+'Bot: Nice To Hear')
        
        elif (self.entry.get()=='who created you'):
            self.text.insert(END,'\n\n'+'Bot: Thejas and Kumar created me!!')

        elif (self.entry.get()=='what is your name'):
            self.text.insert(END,'\n\n'+'Bot: My Name is Dynamo')

        elif (self.entry.get()=='can you speak kannada'):
            self.text.insert(END,'\n\n'+"Bot: I'm still Learning it.....")

        elif (self.entry.get()=='what is machine learning'):
            self.text.insert(END,'\n\n'+'Bot: Machine learning is a branch \n of artificial intelligence (AI) and computer science \n which focuses on the use of data and algorithms \nto imitate the way that humans learn,\n gradually improving its accuracy.')

        elif (self.entry.get()=='how does face recognition work'):
            self.text.insert(END,'\n\n'+'Bot: Step 1: Face detection\nStep 2: Face analysis\nStep 3: Converting the image to data\nStep 4: Finding a match')

        else :
            self.text.insert(END,'\n\n'+"Bot: Sorry i didn't get it..." )




       
        










if __name__=="__main__":
    root=Tk()
    obj=ChatBot(root)
    root.mainloop()


        