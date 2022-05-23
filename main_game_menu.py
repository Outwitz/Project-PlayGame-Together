from tkinter import *

from PIL import Image,ImageTk

import os

#main_gui
root = Tk()
root.title("Play Game Together")
root.geometry("1278x768+300+100")
root.resizable(False, False)
load = Image.open('D:\python_nas\project\_vlr_ui\image\main.jpg')
render = ImageTk.PhotoImage(load)
Label(root,image = render).place(x=0,y=0)
Label(root,text='Play Game Together',font=('Jungle Adventurer',46),bg='#215992',fg='#ffffff').place(x=600,y=30)

vlr_img=PhotoImage(file="image/vlrq.png")
vlr_img_btn=Button(root,image=vlr_img,borderwidth=0.5,command=lambda:valorant_page())
vlr_img_btn.place(x=400,y=300)
apex_img=PhotoImage(file="image/apex_i.png")
apex_img_btn=Button(root,image=apex_img,borderwidth=0.5,command=lambda:apex_page())
apex_img_btn.place(x=600,y=300)
dota_img=PhotoImage(file="image/dotaq.png")
dota_img_btn=Button(root,image=dota_img,borderwidth=0.5,command=lambda:dota_page())
dota_img_btn.place(x=800,y=300)
exit_img=PhotoImage(file="image/exit_i.png")
exit_img_btn=Button(root,image=exit_img,borderwidth=0.5,command=root.destroy)
exit_img_btn.place(x=1000,y=300)

def valorant_page():
  os.system("D:\python_nas\project\_vlr_ui\_vlr_lft_project.py")
  
def apex_page():
  os.system("D:\python_nas\project\_vlr_ui\_apex_lft_project.py")
  
def dota_page():
  os.system("D:\python_nas\project\_vlr_ui\dota2_tgt.py")

root.mainloop()
