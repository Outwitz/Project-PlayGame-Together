#import tkinter gui
from tkinter import *
#import tooltips
from tkinter.tix import *
#import image pillow
from PIL import Image,ImageTk
#import font
from tkinter.font import Font 
#import tkinter treeview,messagebox
from tkinter import ttk,messagebox

from tkinter import filedialog
#import open_web
import webbrowser
#import check_url
import validators
#import sql.db
import sqlite3
conn = sqlite3.connect(r"D:\python_nas\project\_vlr_ui\game_db.db")
c = conn.cursor()
#main_menu
def login_main():
  global root
  root = Tk()
  root.title("Dota 2 Together")
  root.geometry("1278x768+300+100")
  root.resizable(False, False)
  #tkinter icon
  root.iconbitmap('D:\python_nas\project\_vlr_ui\_vt_icon.ico')
  #tkinter font
  global BigFont,MidFont
  BigFont = Font(family="OPTIwtcGoudy-Medium",size=36,weight="bold")
  MidFont = Font(family="OPTIwtcGoudy-Medium",size=18)
  TextFont= Font(family="Helvetica",size=18)
  smallFont = Font(family="OPTIwtcGoudy-Medium",size=16)
  #tkinter background image
  load = Image.open('image\\dota_wall_1.png')
  render = ImageTk.PhotoImage(load)
  Label(root,image = render).place(x=0,y=0)
#tkinter main Label
  Label(root,text="Dota 2 Together",font=BigFont,bg="#9370DB",fg="#ffffff").pack(pady=25)
  Label(root,text="play together win together lose together",font=MidFont,fg="#ffffff",bg="#9370DB").place(x=410,y=100)
  Label(root,text="Login",font=MidFont,fg="#ffffff",bg="#9370DB").place(x=600,y=150)
  Label(root,text="username",font=MidFont,bg="#9370DB",fg="#ffffff").place(x=350,y=200)
  Label(root,text="password",font=MidFont,bg="#9370DB",fg="#ffffff").place(x=350,y=250)
  uesr_input_var=StringVar()
  pass_input_var=StringVar()
  uesr_input=Entry(root,text="",font=TextFont,textvariable=uesr_input_var)
  uesr_input.place(x=550,y=200)
  pass_input=Entry(root,text="",show="•",font=TextFont,textvariable=pass_input_var)
  pass_input.place(x=550,y=250)
  Button(root,text="Login",font=smallFont,fg="#ffffff",bg="#9370DB",width=5,height=1,command=lambda:login()).place(x=520,y=300)
  Button(root,text="register",font=smallFont,fg="#ffffff",bg="#9370DB",width=8,height=1,command=lambda:register()).place(x=620,y=300)
#exit_progarm
  def exit_pro():
    root.destroy()
    #close data base
    conn.close()
  Button(root,text="exit",font=smallFont,fg="#ffffff",bg="#9370DB",width=8,height=1,command=lambda:exit_pro()).place(x=760,y=300)
#showpassword
  c_v1=IntVar(value=0)
  def showpass():
    if (c_v1.get() ==1):
      pass_input.config(show="")
    else:
      pass_input.config(show="•")
  Checkbutton(root,text='show password',variable=c_v1,onvalue=1,offvalue=0,command=showpass).place(x=820,y=255)
#func login
  def login():
    conn = sqlite3.connect(r"D:\python_nas\project\_vlr_ui\game_db.db")
    c = conn.cursor()
    username=uesr_input.get()
    password=pass_input.get()
    c.execute("SELECT * FROM dota_2_tgt WHERE username=? AND password=?",(username,password))
    row=c.fetchone()
    if row:
      if len(uesr_input.get()) > 1:
        uesr_input.delete(0, 'end')
        pass_input.delete(0, 'end')
        root.withdraw()
        main()
        messagebox.showinfo("Login","login successful",parent=root)
    elif username and password == 'admin_dota':
      admin_dota()
      
    else:
      messagebox.showerror("Error","please try again",parent=root)
#register
  def register():
    new_window=Toplevel(root)
    new_window.geometry("1278x768+300+100")
    new_window.title("Dota 2 Together")
    new_window.iconbitmap('D:\python_nas\project\_vlr_ui\_vt_icon.ico')
    Label(new_window,image = render).place(x=0,y=0)
    Label(new_window,text="username",font=smallFont,bg="#9370DB",fg="#ffffff").place(x=250,y=150)
    Label(new_window,text="password",font=smallFont,bg="#9370DB",fg="#ffffff").place(x=250,y=200)
    Label(new_window,text="confirm password",font=smallFont,bg="#9370DB",fg="#ffffff").place(x=250,y=250)
    Label(new_window,text="Enter your name:",font=smallFont,bg="#9370DB",fg="#ffffff").place(x=250,y=300)
    input_1_lft_Entry=Entry(new_window,text="",font=TextFont)
    input_1_lft_Entry.place(x=550,y=300)
  #input_data_riot_id
    Label(new_window,text="Enter your steam link:",font=smallFont,bg="#9370DB",fg="#ffffff").place(x=250,y=350)
    input_2_lft_Entry=Entry(new_window,text="",font=TextFont)
    input_2_lft_Entry.place(x=550,y=350)
  #input_data_rank
    def comboclick(event):
      cbo_rank.get()

    rank_list = ['Unranked','Herald','Guardian','Crusader','Archon','Legend','Ancient','Divine','Immortal']
    cbo_rank = ttk.Combobox(new_window, values=rank_list, state='readonly',font=('Helvetica',16))
    cbo_rank.bind("<<ComboboxSelectted>>",comboclick)
    cbo_rank.place(x=550,y=400)
    Label(new_window,text="Enter your rank:",font=smallFont,bg="#9370DB",fg="#ffffff").place(x=250,y=400)
    
  #input_contact
    Label(new_window,text="Enter your contact:",font=smallFont,bg="#9370DB",fg="#ffffff").place(x=250,y=450)
    input_4_lft_Entry=Entry(new_window,text="",font=TextFont)
    input_4_lft_Entry.place(x=550,y=450)

    def comboclick_role(event):
      cbo_role.get()

    role_list = ['Carry','Mid lane','Off-lane','Support','Hard Support']
    cbo_role = ttk.Combobox(new_window, values=role_list, state='readonly',font=('Helvetica',16))
    cbo_role.bind("<<ComboboxSelectted>>",comboclick_role)
    cbo_role.place(x=550,y=500)
    Label(new_window,text="Enter your role:",font=TextFont,bg="#9370DB",fg="#ffffff").place(x=250,y=500)
  
  #input_data_title
    Label(new_window,text="Enter your title:",font=smallFont,bg="#9370DB",fg="#ffffff").place(x=250,y=550)
    input_6_lft_Entry=Entry(new_window,text="",font=TextFont)
    input_6_lft_Entry.place(x=550,y=550)
  #tooltips
    b1=Balloon(new_window)
    b1.bind_widget(input_4_lft_Entry,balloonmsg='you can put your link discord or link facebook')
    newuser_input=Entry(new_window,text="",font=TextFont)
    newuser_input.place(x=550,y=150)
    newpass_input=Entry(new_window,text="",show="•",font=TextFont)
    newpass_input.place(x=550,y=200)
    confirm_pass=Entry(new_window,text="",show="•",font=TextFont)
    confirm_pass.place(x=550,y=250)
    Label(new_window,text="register",font=BigFont,fg="#ffffff",bg="#9370DB").place(x=500,y=50)
    Button(new_window,text="confirm",font=smallFont,fg="#ffffff",bg="#9370DB",width=8,height=1,command=lambda:confirm()).place(x=550,y=600)
    Button(new_window,text="back",font=smallFont,fg="#ffffff",bg="#9370DB",width=5,height=1,command=lambda:new_window.destroy()).place(x=700,y=600)
#show_password
    c_v1=IntVar(value=0)
    def showpass():
      if (c_v1.get() ==1):
        newpass_input.config(show="")
        confirm_pass.config(show="")
      else:
         newpass_input.config(show="•")
         confirm_pass.config(show="•")
    Checkbutton(new_window,text='show password',variable=c_v1,onvalue=1,offvalue=0,command=showpass).place(x=820,y=256)

    def add_user():
      conn = sqlite3.connect(r"D:\python_nas\project\_vlr_ui\game_db.db")
      c = conn.cursor()
      username=newuser_input.get()
      password=newpass_input.get()
      name=input_1_lft_Entry.get()
      steam_link=input_2_lft_Entry.get()
      rank=cbo_rank.get()
      contact=input_4_lft_Entry.get()
      title=input_6_lft_Entry.get()
      role=cbo_role.get()
    
      c.execute("INSERT INTO dota_2_tgt (username,password,name,steam_link,rank,contact,role,title) VALUES(?,?,?,?,?,?,?,?)",(username,password,name,steam_link,rank,contact,role,title))
      conn.commit()

#confirm register
    def confirm():
      url_contact=(input_4_lft_Entry.get())
      url_steam=(input_2_lft_Entry.get())
      valid_con=validators.url(url_contact)
      valid_stm=validators.url(url_steam)
      conn = sqlite3.connect(r"D:\python_nas\project\_vlr_ui\game_db.db")
      c = conn.cursor()
      c.execute("SELECT * FROM dota_2_tgt WHERE username=? ",(newuser_input.get(),))
      row=c.fetchone()
      response = messagebox.askokcancel("Please Confirm","Please Confirm",parent=new_window)
      if response == True:
        if len(newuser_input.get()) == 0:
          messagebox.showerror("Error","please enter your username",parent=new_window)
        elif len(newpass_input.get()) == 0:
          messagebox.showerror("Error","please enter your password",parent=new_window)
        elif row:
            messagebox.showerror("Error","this username is already in use",parent=new_window)
        elif newpass_input.get() != confirm_pass.get():
            messagebox.showerror("Error","Password did not match Please try again",parent=new_window)
        elif len(input_1_lft_Entry.get()) == 0:
          messagebox.showerror("Error","please enter your name",parent=new_window)
        elif len(input_2_lft_Entry.get()) == 0:
          messagebox.showerror("Error","please enter your steam link",parent=new_window)
        elif len(input_4_lft_Entry.get()) == 0:
          messagebox.showerror("Error","please enter your contact",parent=new_window)
        elif len(cbo_rank.get()) == 0:
          messagebox.showerror("Error","please enter your rank",parent=new_window)
        elif len(input_6_lft_Entry.get()) == 0:
          messagebox.showerror("Error","please enter your title",parent=new_window)
        elif len(cbo_role.get()) == 0:
          messagebox.showerror("Error","please enter your role",parent=new_window)
        elif valid_con== True and valid_stm == True:
            add_user()
            newuser_input.delete(0, 'end')
            newpass_input.delete(0, 'end')
            confirm_pass.delete(0, 'end')
            input_1_lft_Entry.delete(0, 'end')
            input_2_lft_Entry.delete(0, 'end')
            input_4_lft_Entry.delete(0, 'end')
            input_6_lft_Entry.delete(0, 'end')
            messagebox.showinfo("register","register successful",parent=new_window) 
        else:
            messagebox.showerror("Error","url invalid",parent=new_window)
#main_menu
def main():
#tkinter main
  global main_menu
  main_menu = Toplevel(root)
  main_menu.title("Dota 2 Together")
  main_menu.geometry("1278x768+300+100")
  main_menu.resizable(False, False)
  main_menu.deiconify()
#tkinter icon
  main_menu.iconbitmap('D:\python_nas\project\_vlr_ui\_vt_icon.ico')
#tkinter font
  global BigFont,MidFont,TextFont,smallFont
  BigFont = Font(family="OPTIwtcGoudy-Medium",size=42,weight="bold")
  MidFont = Font(family="OPTIwtcGoudy-Medium",size=16,weight="bold")
  TextFont= Font(family="Helvetica",size=18)
  smallFont = Font(family="OPTIwtcGoudy-Medium",size=18)
#tkinter background image
  global render
  load = Image.open('image\\dota_wall_1.png')
  render = ImageTk.PhotoImage(load)
  Label(main_menu,image = render).place(x=0,y=0)
  Label(main_menu,text ="Created by Kroekchai and Saroot",font=('Helvetica',12)).place(x=1020,y=730)
#tkinter main Label
  Label(main_menu,text="Dota 2 Together",font=BigFont,bg="#9370DB",fg="#ffffff").pack(pady=25)
  Label(main_menu,text="play together win together lose together",font=MidFont,fg="#ffffff",bg="#9370DB").pack()
#tkinter main btn
  Button(main_menu,text="Find Team",font=MidFont,fg="#ffffff",bg="#9370DB",width=12,height=1,command=lambda:search_lft()).place(x=550,y=270)
  Button(main_menu,text="update",font=MidFont,fg="#ffffff",bg="#9370DB",width=12,height=1,command=lambda:update_data_player()).place(x=550,y=320)
  Button(main_menu,text="report",font=MidFont,fg="#ffffff",bg="#9370DB",width=12,height=1,command=lambda:report()).place(x=550,y=370)
#exit program
  def Logout():
    root.deiconify()
    main_menu.destroy()
    messagebox.showinfo("Logout","Logout successful",parent=root)
  def Logout_btn():
    Button(main_menu,text="Logout",font=MidFont,fg="#ffffff",bg="#9370DB",width=12,height=1,command=lambda:Logout()).place(x=550,y=420)
  Logout_btn()

#func_search

#search_data
def search_lft():
  new_window=Toplevel(root)
  new_window.geometry("1278x768+300+100")
  new_window.title("Dota 2 Together")
  new_window.iconbitmap('D:\python_nas\project\_vlr_ui\_vt_icon.ico')
  new_window.resizable(False, False)
  Label(new_window,image = render).place(x=0,y=0)
  Label(new_window,text="Dota Together",font=BigFont,bg="#9370DB",fg="#ffffff").pack(pady=25)

  Label(new_window,text="search by role:",font=MidFont,bg="#9370DB",fg="#ffffff").place(x=250,y=470)
  Button(new_window,text="search",font=MidFont,fg="#ffffff",bg="#9370DB",width=8,height=1,command=lambda:search_records()).place(x=750,y=470)
  def comboclick(event):
    search_entry.get()
  role_list = ['Carry','Mid lane','Off-lane','Support','Hard Support']
  search_entry = ttk.Combobox(new_window, values=role_list, state='readonly',font=('Helvetica',16))
  search_entry.bind("<<ComboboxSelectted>>",comboclick)
  search_entry.place(x=460,y=470)
  Label(new_window,text="Contact:",font=('Helvetica',12),bg="#9370DB",fg="#ffffff").place(x=140,y=570)
  input_4_lft_Entry=Entry(new_window,text="",font=('Helvetica',12))
  input_4_lft_Entry.place(x=210,y=570)
  Label(new_window,text="Steam link:",font=('Helvetica',12),bg="#9370DB",fg="#ffffff").place(x=120,y=610)
  input_2_lft_Entry=Entry(new_window,text="",font=('Helvetica',12))
  input_2_lft_Entry.place(x=210,y=610)
  Button(new_window,text="back",font=MidFont,fg="#ffffff",bg="#9370DB",width=10,height=1,command=lambda:new_window.destroy()).place(x=500,y=530)
  Button(new_window,text="refresh",font=MidFont,fg="#ffffff",bg="#9370DB",width=8,height=1,command=lambda:SELECT()).place(x=900,y=470)
  
  
  Button(new_window,text="Open",fg="#ffffff",bg="#9370DB",command=lambda:openweb_contact()).place(x=410,y=570)
  Button(new_window,text="Open",fg="#ffffff",bg="#9370DB",command=lambda:openweb_valorant_tracker()).place(x=410,y=610)

  def openweb_valorant_tracker():
    
    webbrowser.open(input_2_lft_Entry.get())
  def  openweb_contact():
    webbrowser.open(input_4_lft_Entry.get())
#table lfp
  style = ttk.Style()
  style.theme_use("default")
  tree_frame = Frame(new_window)
  tree_frame.place(x=90,y=100)
  tv = ttk.Treeview(tree_frame,columns=(1,2,3,4,5,6),show='headings',height='15')
  tree_scroll_x=Scrollbar(tree_frame,orient='horizontal',command=tv.xview)
  tree_scroll_x.pack(side=BOTTOM,fill='x')
  tree_scroll_y=Scrollbar(tree_frame,orient='vertical',command=tv.yview)
  tree_scroll_y.pack(side=RIGHT, fill='y')
  tv.config(yscrollcommand=tree_scroll_y.set,xscrollcommand=tree_scroll_x.set)
  
  tv.heading(1,text='name')
  tv.heading(2,text='steam_link')
  tv.heading(3,text='rank')
  tv.heading(4,text='contact')
  tv.heading(5,text='role')
  tv.heading(6,text='title')
  
  tv.column(1,width=200,minwidth=200)
  tv.column(2,width=200,minwidth=200)
  tv.column(3,width=200,minwidth=200)
  tv.column(4,width=200,minwidth=200)
  tv.column(5,width=200,minwidth=200)
  tv.column(6,width=200,minwidth=200)
  
  tv.pack()
  def clear_textbox():
    input_2_lft_Entry.delete(0, 'end')
    input_4_lft_Entry.delete(0, 'end')
    

  def click_getvalue(event):
    clear_textbox()
    
    row_id = tv.selection()[0]
    select = tv.set(row_id)
    input_2_lft_Entry.insert(0,select['2'])
    input_4_lft_Entry.insert(0,select['4'])

  def search_records():
    conn = sqlite3.connect(r"D:\python_nas\project\_vlr_ui\game_db.db")
    c = conn.cursor()
    lookup_record = search_entry.get()
    for result in tv.get_children():tv.delete(result)
    c.execute("SELECT name,steam_link,rank,contact,role,title FROM dota_2_tgt WHERE role like ?",(lookup_record,))
    result = c.fetchall()
    
    for x in result:tv.insert('','end',value=x)
    conn.commit()
    
  def SELECT():
    conn = sqlite3.connect(r"D:\python_nas\project\_vlr_ui\game_db.db")
    c = conn.cursor()
    clear_textbox()
  
    for result in tv.get_children():tv.delete(result)
    c.execute('''SELECT name,steam_link,rank,contact,role,title FROM dota_2_tgt''')
    result=c.fetchall()
    
    for x in result:tv.insert('','end',value=x)
  SELECT()
  tv.bind('<Double-Button-1>',click_getvalue)
  
#Exit
def update_data_player():
  new_window=Toplevel(root)
  new_window.geometry("1278x768+300+100")
  new_window.title("Apex Legends Together")
  new_window.iconbitmap('D:\python_nas\project\_vlr_ui\_vt_icon.ico')
  img = Label(new_window,image = render)
  img.place(x=0,y=0)
  Label(new_window,text="Dota 2 Together",font=BigFont,bg="#9370DB",fg="#ffffff").pack(pady=25)
  Button(new_window,text="update player data",command=lambda:data_lft(),font=MidFont,fg="#ffffff",bg="#9370DB",width=20,height=1).place(x=450,y=300)
  Button(new_window,text="back",command=lambda:new_window.destroy(),font=MidFont,fg="#ffffff",bg="#9370DB",width=20,height=1).place(x=450,y=400)
  
  def data_lft():
    new_window=Toplevel(root)
    new_window.geometry("1278x768+300+100")
    new_window.title("Dota 2 Together")
    new_window.iconbitmap('D:\python_nas\project\_vlr_ui\_vt_icon.ico')
    new_window.resizable(False, False)
    Label(new_window,image = render).place(x=0,y=0)
    Label(new_window,text="Dota Together",font=BigFont,bg="#9370DB",fg="#ffffff").pack(pady=25)

    Label(new_window,text="Name:",font=('Helvetica',12),bg="#9370DB",fg="#ffffff").place(x=800,y=530)
    input_1_lft_Entry=Entry(new_window,text="",font=('Helvetica',12))
    input_1_lft_Entry.place(x=900,y=530)
#input_data_riot_id
    Label(new_window,text="Steam link:",font=('Helvetica',12),bg="#9370DB",fg="#ffffff").place(x=800,y=560)
    input_2_lft_Entry=Entry(new_window,text="",font=('Helvetica',12))
    input_2_lft_Entry.place(x=900,y=560)
#input_data_rank
    def comboclick(event):
      input_3_lft_Entry.get()

    rank_list = ['Unranked','Herald','Guardian','Crusader','Archon','Legend','Ancient','Divine','Immortal']
    input_3_lft_Entry = ttk.Combobox(new_window, values=rank_list, state='readonly',font=('Helvetica',12))
    input_3_lft_Entry.bind("<<ComboboxSelectted>>",comboclick)
    Label(new_window,text="rank:",font=('Helvetica',12),bg="#9370DB",fg="#ffffff").place(x=800,y=590)
    input_3_lft_Entry.place(x=900,y=590)
    
#input_contact
    Label(new_window,text="Contact:",font=('Helvetica',12),bg="#9370DB",fg="#ffffff").place(x=800,y=620)
    input_4_lft_Entry=Entry(new_window,text="",font=('Helvetica',12))
    input_4_lft_Entry.place(x=900,y=620)

    
    def comboclick_role(event):
      input_role_lft_Entry.get()

    role = ['Carry','Mid lane','Off-lane','Support','Hard Support']
    input_role_lft_Entry = ttk.Combobox(new_window, values=role, state='readonly',font=('Helvetica',12))
    input_role_lft_Entry.bind("<<ComboboxSelectted>>",comboclick_role)
    input_role_lft_Entry.place(x=900,y=680)
    Label(new_window,text="Role:",font=('Helvetica',12),bg="#9370DB",fg="#ffffff").place(x=800,y=680)


#input_data_title
    Label(new_window,text="Title:",font=('Helvetica',12),bg="#9370DB",fg="#ffffff").place(x=800,y=650)
    input_6_lft_Entry=Entry(new_window,text="",font=('Helvetica',12))
    input_6_lft_Entry.place(x=900,y=650)

    Label(new_window,text="Enter your username:",font=('Helvetica',12),bg="#9370DB",fg="#ffffff").place(x=80,y=470)
    search_entry_1=Entry(new_window,text="",font=('Helvetica',12))
    search_entry_1.place(x=240,y=470)

    Label(new_window,text="Enter your password:",font=('Helvetica',12),bg="#9370DB",fg="#ffffff").place(x=80,y=500)
    Button(new_window,text="submit",font=('Helvetica',12),fg="#ffffff",bg="#9370DB",width=5,command=lambda:search_confrim()).place(x=430,y=470)

    Label(new_window,text="Username:",font=('Helvetica',12),bg="#9370DB",fg="#ffffff").place(x=800,y=470)
    username=Entry(new_window,text="",font=('Helvetica',12))
    username.place(x=900,y=470)

    Label(new_window,text="Password:",font=('Helvetica',12),bg="#9370DB",fg="#ffffff").place(x=800,y=500)
    password=Entry(new_window,text="",font=('Helvetica',12))
    password.place(x=900,y=500)


    
    search_entry_2=Entry(new_window,text="",font=('Helvetica',12),show="•")
    search_entry_2.place(x=240,y=500)
    Button(new_window,text="update",font=('Helvetica',12),fg="#ffffff",bg="#9370DB",command=lambda:confirm_update()).place(x=850,y=720)
    Button(new_window,text="delete",font=('Helvetica',12),fg="#ffffff",bg="#9370DB",command=lambda:confirm_delete()).place(x=950,y=720)
    Button(new_window,text="back",font=('Helvetica',12),fg="#ffffff",bg="#9370DB",width=5,command=lambda:new_window.destroy()).place(x=1050,y=720)
    Button(new_window,text="refresh",font=('Helvetica',12),fg="#ffffff",bg="#9370DB",width=5,command=lambda:clear_textbox()).place(x=490,y=470)
  
    style = ttk.Style()
    style.theme_use("default")
    tree_frame = Frame(new_window)
    tree_frame.pack(fill='x')
    tv = ttk.Treeview(tree_frame,columns=(1,2,3,4,5,6,7,8),show='headings',height='15')
    tree_scroll_x=Scrollbar(tree_frame,orient='horizontal',command=tv.xview)
    tree_scroll_x.pack(side=BOTTOM,fill='x')
    tree_scroll_y=Scrollbar(tree_frame,orient='vertical',command=tv.yview)
    tree_scroll_y.pack(side=RIGHT, fill='y')
    tv.config(yscrollcommand=tree_scroll_y.set,xscrollcommand=tree_scroll_x.set)
    tv.heading(1,text='username')
    tv.heading(2,text='password')
    tv.heading(3,text='name')
    tv.heading(4,text='steam link')
    tv.heading(5,text='rank')
    tv.heading(6,text='contact')
    tv.heading(7,text='role')
    tv.heading(8,text='title')
    tv.column(1,width=200,minwidth=200)
    tv.column(2,width=200,minwidth=200)
    tv.column(3,width=200,minwidth=200)
    tv.column(4,width=200,minwidth=200)
    tv.column(5,width=200,minwidth=200)
    tv.column(6,width=200,minwidth=200)
    tv.column(7,width=200,minwidth=200)
    tv.column(8,width=200,minwidth=200)
    tv.pack()
# confirm update button
    def confirm_update():
      url_contact=(input_4_lft_Entry.get())
      url_steam=(input_2_lft_Entry.get())
      valid_con=validators.url(url_contact)
      valid_stm=validators.url( url_steam)
      response = messagebox.askokcancel("confirm","confirm",parent=new_window)
      if response == 1:
        if len(input_1_lft_Entry.get()) == 0:
          messagebox.showerror("Error","please enter your name",parent=new_window)
        elif len(input_2_lft_Entry.get()) == 0:
          messagebox.showerror("Error","please enter your steam link",parent=new_window)
        elif len(input_4_lft_Entry.get()) == 0:
          messagebox.showerror("Error","please enter your contact",parent=new_window)
        elif len(input_3_lft_Entry.get()) == 0:
          messagebox.showerror("Error","please enter your rank",parent=new_window)
        elif len(input_6_lft_Entry.get()) == 0:
          messagebox.showerror("Error","please enter your title",parent=new_window)
        elif len(search_entry_1.get()) == 0:
          messagebox.showerror("Error","please enter your password",parent=new_window)
        elif valid_con == True and valid_stm == True:
          update()
          clear_textbox()
          messagebox.showinfo("update","update successful",parent=new_window)
        else:
          messagebox.showerror("Error","Invalid url",parent=new_window)
#confirm delete
    def confirm_delete():
      response = messagebox.askokcancel("confirm","confirm",parent=new_window)
      if response == 1:
          delete()
          clear_textbox()
          messagebox.showinfo("delete","delete successful",parent=new_window)
#func clear textbox
    def clear_textbox():
      search_entry_1.delete(0,'end')
      search_entry_2.delete(0,'end')
      input_1_lft_Entry.delete(0, 'end')
      input_2_lft_Entry.delete(0, 'end')
      input_4_lft_Entry.delete(0, 'end')
      input_6_lft_Entry.delete(0, 'end')
      username.delete(0, 'end')
      password.delete(0, 'end')

  
#func_update
    def update():
      conn = sqlite3.connect(r"D:\python_nas\project\_vlr_ui\game_db.db")
      c = conn.cursor()
      id_username=search_entry_1.get()
      update_username=username.get()
      update_password=password.get()
      update_name=input_1_lft_Entry.get()
      update_steam_link=input_2_lft_Entry.get()
      update_rank=input_3_lft_Entry.get()
      update_contact=input_4_lft_Entry.get()
      update_role=input_role_lft_Entry.get()
      update_titles=input_6_lft_Entry.get()
      
      c.execute('''UPDATE dota_2_tgt SET username = ?, password = ?,name = ?,steam_link= ?, rank = ?, contact = ?,role = ?,title = ? WHERE username = ?''',(update_username,update_password,update_name,update_steam_link,update_rank,update_contact,update_role,update_titles,id_username))
      conn.commit()
#func delete
    def delete():
      del_select=search_entry_1.get()
      conn = sqlite3.connect(r"D:\python_nas\project\_vlr_ui\game_db.db")
      c = conn.cursor()
      c.execute('''DELETE FROM dota_2_tgt WHERE username = ?''',(del_select,))
      conn.commit()
# click_getvalue
    def click_getvalue(event):
      clear_textbox()
      row_id = tv.selection()[0]
      select = tv.set(row_id)
      search_entry_1.insert(0,select['1'])
      search_entry_2.insert(0,select['2'])
      username.insert(0,select['1'])
      password.insert(0,select['2'])
      input_1_lft_Entry.insert(0,select['3'])
      input_2_lft_Entry.insert(0,select['4'])
      input_3_lft_Entry.insert(0,select['5'])
      input_4_lft_Entry.insert(0,select['6'])
      input_6_lft_Entry.insert(0,select['8'])
    
#search_records
    def search_confrim():
      conn = sqlite3.connect(r"D:\python_nas\project\_vlr_ui\game_db.db")
      c = conn.cursor()
      username=search_entry_1.get()
      password=search_entry_2.get()
      c.execute("SELECT * FROM dota_2_tgt WHERE username=? AND password=?",(username,password))
      row=c.fetchone()
      if row:
        search_records()
      else:
        messagebox.showerror("Error","Username or password incorrect",parent=new_window) 
    def search_records():
      conn = sqlite3.connect(r"D:\python_nas\project\_vlr_ui\game_db.db")
      c = conn.cursor()
      lookup_record = search_entry_1.get()
      for result in tv.get_children():tv.delete(result)
      c.execute("SELECT username,password,name,steam_link,rank,contact,role,title FROM dota_2_tgt WHERE username = ?",(lookup_record,))
      result = c.fetchall()
      for x in result:tv.insert('','end',value=x)
      conn.commit()
      tv.bind('<Double-Button-1>',click_getvalue)

    

def report():
  new_window=Toplevel(root)
  new_window.geometry("1278x768+300+100")
  new_window.title("Dota 2 Together")
  new_window.iconbitmap('D:\python_nas\project\_vlr_ui\_vt_icon.ico')
  new_window.resizable(False, False)
  Label(new_window,image = render).place(x=0,y=0)
  Label(new_window,text="report",font=BigFont,bg="#9370DB",fg="#ffffff").pack(pady=25)
  Label(new_window,text="Enter steam link you want to report:",font=MidFont,bg="#9370DB",fg="#ffffff").place(x=200,y=150)
  report_id=Entry(new_window,text="",font=('Helvetica',16))
  report_id.place(x=600,y=150)
  Label(new_window,text="reason:",font=MidFont,bg="#9370DB",fg="#ffffff").place(x=200,y=200)
  def comboclick(event):
      reason_list.get()

  reason_list = ['Toxic','Hacking','Leaving the game/AFK','Other']
  reason_list = ttk.Combobox(new_window, values=reason_list, state='readonly',font=('Helvetica',16))
  reason_list.bind("<<ComboboxSelectted>>",comboclick)
  reason_list.place(x=600,y=200)
  Label(new_window,text="reason title:",font=MidFont,bg="#9370DB",fg="#ffffff").place(x=200,y=250)
  reason_title = Entry(new_window,text="",font=('Helvetica',16))
  reason_title.place(x=600,y=250)

  def confirm_uplond():
      response = messagebox.askokcancel("confirm","confirm",parent=new_window)
      if response == True:
        if len(reason_list.get()) == 0:
          messagebox.showerror("Error","please enter your reason",parent=new_window)
        elif len(report_id.get()) == 0:
          messagebox.showerror("Error","please enter your steam link",parent=new_window)
        elif len(reason_title.get()) == 0:
          messagebox.showerror("Error","please enter your steam link",parent=new_window)
        else:
          insert_image()
          messagebox.showinfo("uplond","uplond successful",parent=new_window)

  
  def filedialogs():
    global get_image
    get_image = filedialog.askopenfilenames(title="SELECT IMAGE", filetypes=( ("png", "*.png"), ("jpg" , "*.jpg"), ("Allfile", "*.*")))

#Image need to be conver into binary before insert into database
  def conver_image_into_binary(filename):
    with open(filename, 'rb') as file:
        photo_image = file.read()
    return photo_image

  def insert_image():
    conn = sqlite3.connect(r"D:\python_nas\project\_vlr_ui\game_db.db")
    c = conn.cursor()
    
    for image in get_image:
       insert_photo   = conver_image_into_binary(image)
       c.execute("INSERT INTO report_dota_fix(steam_link,reason,reason_title,image) VALUES(?,?,?,?)",(report_id.get(),reason_list.get(),reason_title.get(),insert_photo))
                 
    conn.commit()
  Button(new_window,text="upload evidence",command=lambda:confirm_uplond(),font=MidFont,bg="#9370DB",fg="#ffffff").place(x=500,y=350)
  Button(new_window,text="Select Image",command=filedialogs,font=MidFont,bg="#9370DB",fg="#ffffff").place(x=530,y=300)
  Button(new_window,text="Back",command=new_window.destroy,font=MidFont,bg="#9370DB",fg="#ffffff").place(x=730,y=350)
def admin_dota():
  
  new_window=Toplevel(root)
  new_window.geometry("800x600+500+200")
  new_window.title("Valorant Together")
  new_window.resizable(False, False)
  new_window.config(bg='black')
  
  Label(new_window,text="admin",bg="#dc3d4b").pack(pady=25)

  
  Button(new_window,text="delete",width=8,height=1,command=lambda:confirm_delete()).place(x=670,y=470)
  search_entry=Entry(new_window,text="",font=('Helvetica',12))
  search_entry.place(x=460,y=470)
  
#table lfp
  style = ttk.Style()
  style.theme_use("default")
  tree_frame = Frame(new_window)
  tree_frame.place(x=30,y=100)
  tv = ttk.Treeview(tree_frame,columns=(1,2,3),show='headings',height='15')
  tree_scroll_x=Scrollbar(tree_frame,orient='horizontal',command=tv.xview)
  tree_scroll_x.pack(side=BOTTOM,fill='x')
  tree_scroll_y=Scrollbar(tree_frame,orient='vertical',command=tv.yview)
  tree_scroll_y.pack(side=RIGHT, fill='y')
  tv.config(yscrollcommand=tree_scroll_y.set,xscrollcommand=tree_scroll_x.set)
  
  tv.heading(1,text='riot_id')
  tv.heading(2,text='reason')
  tv.heading(3,text='reason title')
  
  
  tv.column(1,width=200,minwidth=200)
  tv.column(2,width=200,minwidth=200)
  tv.column(3,width=200,minwidth=200)
  
  
  tv.pack()
 
  def click_getvalue(event):
    
    row_id = tv.selection()[0]
    select = tv.set(row_id)
    search_entry.insert(0,select['1'])
    

    
  def SELECT():
    conn = sqlite3.connect(r"D:\python_nas\project\_vlr_ui\game_db.db")
    c = conn.cursor()
  
    for result in tv.get_children():tv.delete(result)
    c.execute('''SELECT * FROM report_dota_fix''')
    result=c.fetchall()
    
    for x in result:tv.insert('','end',value=x)
  SELECT()
  tv.bind('<Double-Button-1>',click_getvalue)
  def confirm_delete():
      response = messagebox.askokcancel("confirm","confirm",parent=new_window)
      if response == 1:
          delete()
          
          messagebox.showinfo("delete","delete successful",parent=new_window)
  def delete():
      del_select=search_entry.get()
      conn = sqlite3.connect(r"D:\python_nas\project\_vlr_ui\game_db.db")
      c = conn.cursor()
      c.execute('''DELETE FROM dota_2_tgt WHERE steam_link = ?''',(del_select,))
      c.execute('''DELETE FROM report_dota_fix WHERE steam_link = ?''',(del_select,))
      conn.commit()
  
#run_all_func                   
login_main()
root.mainloop()