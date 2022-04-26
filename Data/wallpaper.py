import os
from tkinter import *
from tkinter import filedialog as fd
from tkinter import messagebox
import json
walljson = None
try:
    wallfile = open(r'Data/wallpaper.json',mode='r').read()
    walljson = json.loads(wallfile)
except FileNotFoundError:
    wallfile = open(r'Data/wallpaper.json',mode='w+').read()
except json.decoder.JSONDecodeError:
    print("")
filetypes = (('PNG images', '*.png'),('Gif images', '*.gif'))
dialogOpen1 = False
wp_colors = ['white','black']
wp_filepath = None
def wp_create(parentwin):
    global wp,wp_image,wp_txt_color,wp_win_droptext
    wp = Canvas(parentwin,width=1920,height=1080)
    if walljson == None:
        wp_txt_color = "black"
        wp.pack()
        return
    newimg = str(walljson['Image'])
    wp_txt_color = walljson['FontColor']
    print(wp_txt_color)
    newimgRep = newimg.replace('/','\\')
    try:
        wp_image = PhotoImage(file=walljson['Image'])
    except TclError:
        messagebox.showerror(title='Wallpaper not found',message='The wallpaper chosen could not be found and thus could not be loaded, please re-run the wallpaper editor and re-select the wallpaper')
        wp_txt_color = 'black'
        wp.pack()
        return
    wp.pack()
    wp.create_image(0,0, anchor=NW, image=wp_image)
def wp_edit_fin():
    global wp_win,wp_win_droptext,wp_filepath
    wp_droptemp = str(wp_win_droptext.get())
    if wp_filepath == None:
        wp_filepath = str(walljson['Image'])
    if str(wp_win_droptext.get())== 'Colors':
        wp_droptemp = str(walljson['FontColor'])
    obj = {'Image':wp_filepath,'FontColor':wp_droptemp}
    print(obj)
    jsonString1 = json.dumps(obj)
    print(jsonString1)
    open(r'Data\wallpaper.json',mode='w').write(jsonString1)
    wp_win.destroy()
def wp_remove():
    global wp_win
    obj = {'Image':'','FontColor':'black'}
    print(obj)
    jsonString1 = json.dumps(obj)
    print(jsonString1)
    open(r'Data\wallpaper.json',mode='w').write(jsonString1)
    wp_win.destroy()
def wp_edit(parentwin):
    global wp_win,wp_win_droptext
    wp_win = Toplevel(parentwin)
    wp_win.iconbitmap(r'Data\mainicon.ico')
    wp_win.title('Wallpaper Editor')
    wp_win.geometry('300x300')
    wp_win.attributes('-topmost',True)
    wp_win_filebtn = Button(wp_win,text='Press to choose a background',command=wp_filechoose).pack()
    wp_win_lbl = Label(wp_win,text='Use the dropdown box below to choose \n the font color for the time and whatnot').pack()
    wp_win_droptext = StringVar(wp_win)
    wp_win_droptext.set('Colors')
    wp_win_dropmenu = OptionMenu(wp_win,wp_win_droptext, *wp_colors)
    wp_win_dropmenu.pack()
    wp_win_okbtn = Button(wp_win,text='Press to submit changes',command=wp_edit_fin).pack()
    wp_win_rembtn = Button(wp_win,text='Press to remove wallpaper',command=wp_remove).pack()
def wp_filechoose():
    global dialogOpen1,wp_filepath
    if dialogOpen1 == True:
        return
    dialogOpen1 = True
    wp_filepath = fd.askopenfilename(title='Submit changes',initialdir='/',filetypes=filetypes)
    dialogOpen1 = False
