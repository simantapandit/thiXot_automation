from future.moves import tkinter
from tkinter import *
from tkinter import ttk
import os
from tkinter.ttk import Progressbar
from PIL import Image, ImageTk, ImageSequence
import time

import smtplib
import time
from tkinter import messagebox
from email.message import EmailMessage


def email():
   msg = EmailMessage()
   msg['Subject'] = ("ThinXot : Robustel R3000-L4L Test result for R'NB"+ str(rnb.get()))
   msg['From'] = 'no-reply@thinxtra.com'
   msg['To'] = ['simanta100pandit@gmail.com']

   msg.set_content('Please find the attached rest result')

   # with open('logs.txt') as email:  # message.txt  is the file for the body parts
   #    message = email.read()
   #    msg.set_content(message)

   with open('C:\\Users\\siman\\PycharmProjects\\pythonProject1\\logs .txt',
             'rb') as file:  # actual attachment to be sent
      file_data = file.read()
      file_name = file.name
      msg.add_attachment(file_data, maintype='application', subtype='txt', filename=file_name)
      print(file_data)
      print(file_name)
   with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
      server.login('no-reply@thinxtra.com', 'mjdpvhovhxhprkhm')
      server.send_message(msg)

   print('The test is completed and the report has been emailed to', msg['To'], 'please check the report')

pop = Tk()
pop.geometry("700x700")
pop.title("ThinXot")

image = Image.open('C:\\Users\\siman\\PycharmProjects\\pythonProject1\\Images\\thinXot logo.png')
resized = image.resize((150, 45), Image.ANTIALIAS)

new = ImageTk.PhotoImage(resized)

final = Label(pop, image=new).pack(pady=20)

label1 = Label (pop, text="Please enter the R'NB ", font = ('ari', 16,'bold')).pack()
rnb= StringVar()
e = Entry(pop, textvariable = rnb, width=12, borderwidth = 1).pack(pady=10)


progress = ttk.Progressbar(pop, style='TProgressbar',  orient=HORIZONTAL, length=500, mode='indeterminate')
progress.pack(pady=20)
def answer():
   pop.showerror("Answer", "Sorry, no answer available")

def submit():
   progress.start(20)
   let = "Lets start testing Router"
   mylabel = Label(pop, text=let)
   mylabel.pack()
   print('Following is the result for entire testing')
   print()
   print("R'NB =" + str(rnb.get()))
   os.system('entire_testing.py')
   email()

def stopprogram():
   let1 = "The testing process has been stopped"
   mylabel = Label(pop, text=let1)
   progress.stop()
   #global pop
   quit()





label2 = Label (pop, text="Run entire testing ", font = ('arial', 16,'bold')).pack()



start =  Button(pop, text= "Start", command = submit)
start.pack()

stop = Button(pop, text= "Stop", command= stopprogram)
stop.pack(pady =20 )

label3 = Label (pop, text="Run SIM slots testing ", font = ('arial', 16,'bold')).pack(pady = 20)

def validate_config():
   progress.start(20)
   let = "Lets start testing Router"
   mylabel = Label(pop, text=let)
   mylabel.pack()
   print('SIM slots testing ')
   print("R'NB =" + str(rnb.get()))
   os.system('simcardcheck.py')

start1 = Button(pop, text= "start", command= validate_config)
start1.pack()
stop = Button(pop, text= "Stop", command= stopprogram)
stop.pack(pady =20 )

label4 = Label (pop, text=" Application Installation and Configure ", font = ('arial', 16,'bold')).pack(pady = 20)

def validate_config1():
   progress.start(20)
   let = "Lets start testing Router"
   mylabel = Label(pop, text=let)
   mylabel.pack()
   print('Application istallation and configuration ')
   print("R'NB =" + str(rnb.get()))
   os.system('applications.py')
   email()

start1 = Button(pop, text= "start", command= validate_config1)
start1.pack()
stop = Button(pop, text= "Stop", command= stopprogram)
stop.pack(pady =20 )



pop.mainloop()



