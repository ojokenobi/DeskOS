import datetime,os,time,random
from tkinter import *
from tkinter import messagebox
current = datetime.datetime.now()
aimOpen = False
def close():
    quit()
def helperWin():
    helpwin = Toplevel(root)
    helpwin.title("Help")
    helpwin.iconbitmap(r"Data\icon.ico")
    helpwin.geometry('400x150')
    helpbox = Text(helpwin,height=7,width=80)
    helpbox.insert('end','''
This program is simply just a menu program.
It can help with access programs,
telling the time and some other stuff.
To edit buttons, click the top left
menu and click Button Editor.''')
    helpbox.config(state='disabled')    
    helpbox.pack()
    helpokbtn = Button(helpwin,text='       Ok       ',command=helpwin.destroy)
    helpokbtn.pack()
def aboutWin():
    aboutwin = Toplevel(root)
    aboutwin.title("About")
    aboutwin.iconbitmap(r"Data\icon.ico")
    aboutwin.geometry('400x150')
    aboutbox = Text(aboutwin,height=6,width=35)
    aboutbox.insert('end','''Made by Owen
Shareware, you can distribute if
you want.''')
    aboutbox.config(state='disabled')    
    aboutbox.place(y=0,x=0)
    aboutokbtn = Button(aboutwin,text='       Ok       ',command=aboutwin.destroy)
    aboutokbtn.place(y=105,x=50)
def restart():
    os.startfile('DeskOS.py')
    quit()
def TimeUpdater():
    global timeWin,dateWin,root
    current = datetime.datetime.now()
    timeWin.set(current.strftime("The time is: %H:%M:%S"))
    dateWin.set(current.strftime("The date is: %d/%m/%Y"))
    root.after(500,TimeUpdater)
def timetracer(varname, index, mode):
    wallpaper.wp.itemconfigure(timetxt, text=root.getvar(varname))
def datetracer(varname, index, mode):
    wallpaper.wp.itemconfigure(datetxt, text=root.getvar(varname))
def finstart():
    startupWin.destroy()
    root.deiconify()
    TimeUpdater()
def aimtrain():
    global root
    aimWin = Toplevel(root)
    aimWin.attributes('-fullscreen',True)
    aimMenubar = Menu(aimWin)
    aimWin.config(menu=aimMenubar)
    aimMenu = Menu(aimMenubar,tearoff=0)
    aimMenu.add_command(label='Start Aim Trainer',command=lambda:os.startfile(r'Data\aimtrainer.pyw'))
    aimMenu.add_command(label='Quit',command=aimWin.destroy)
    aimMenubar.add_cascade(label='Controls',menu=aimMenu)
    aimmsg = messagebox.showinfo(title='Aim Trainer Mode',message='In aim trainer mode, a blank play space is provided so that you do not click items on your desktop by accident. Check the menu to start the in-built aim trainer')
    aimWin.lift()
def startupseq():
    global timeWin,dateWin,root,startupWin,timetxt,datetxt
    startupWin = Toplevel(root)
    startupWin.attributes('-fullscreen',True)
    startCanvas = Canvas(startupWin,width=1920,height=1080)
    startCanvas.pack()
    try:
        startimg = PhotoImage(master=startCanvas,file="Data\startup.png")
    except:
        startimg = PhotoImage(master=startCanvas,file="Data\startup.gif")
    startCanvas.create_image(0,0, anchor=NW, image=startimg)
    msgoftheday = ['Hello','abcdefghijklmnopqrstuvwxyz','What a wonderful box','Hmmm, message of the day huh?',"I don't know waht to write for this",'Always save your data!']
    root.attributes('-fullscreen',True)
    wallpaper.wp_create(root)
    timeWin = StringVar(root)
    timeWin.trace_variable('w', timetracer)
    dateWin = StringVar(root)
    dateWin.trace_variable('w', datetracer)
    timetxt = wallpaper.wp.create_text(757,70,font=("Arial",120),fill=wallpaper.wp_txt_color,text=timeWin.get())
    datetxt = wallpaper.wp.create_text(850,200,font=("Arial",120),fill=wallpaper.wp_txt_color,text=dateWin.get())
    wallpaper.wp.create_text(1510,500,font=('Arial',40),text='Message of the day',fill=wallpaper.wp_txt_color)
    wallpaper.wp.create_text(240,500,font=('Calibri',40),text='Apps area',fill=wallpaper.wp_txt_color)
    lbl5box = Text(root,height=3,width=45)
    lbl5box.insert('end',msgoftheday[random.randint(0,5)])
    lbl5box.config(state='disabled')
    lbl5box.place(y=540,x=1340)
    btnload.btns(root,False)
    root.iconbitmap(r'Data\mainicon.ico')
    menubar = Menu(root)
    root.config(menu=menubar)
    #Top left menu is added here
    control_menu = Menu(menubar,tearoff=0)
    control_menu.add_command(label='Aim Trainer Mode',command=aimtrain)
    control_menu.add_command(label='Button Editor',command= lambda:btnload.btnedit(root))
    control_menu.add_command(label='Wallpaper Editor',command= lambda:wallpaper.wp_edit(root))
    control_menu.add_command(label='Refresh',command= lambda:btnload.btns(root,True))
    control_menu.add_separator()
    control_menu.add_command(label='Restart',command=restart)
    control_menu.add_command(label='Quit',command=root.destroy)
    help_menu = Menu(menubar,tearoff=0)
    help_menu.add_command(label='Help',command=helperWin)
    help_menu.add_command(label='About',command=aboutWin)
    menubar.add_cascade(label="Menu",menu=control_menu,underline=1)
    menubar.add_cascade(label="Help",menu=help_menu,underline=1)
    root.after(2000,finstart)
    root.mainloop()
root = Tk()
root.iconify()
# imports at the bottom?! Yes, it's to stop the message that appears
# on first setup from creating a second, uneeded window
from Data import btnload
from Data import wallpaper
root.after(100,startupseq)
root.mainloop()



