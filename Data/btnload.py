import os
from tkinter import *
from tkinter import messagebox
from tkinter import filedialog as fd
import json
fgchange = ['white','cyan','yellow','green']
window = None
try:
    btnread = open(r'Data\btnstore.json').read()
    btnjson = json.loads(btnread)
except FileNotFoundError:
    btnread = open(r'Data\btnstore.json','w+').read()
    btnjson = []
    messagebox.showinfo('First Time Setup',"""Welcome to DeskOS! This prompt has appeared because your button config file could not be read/found. But that's ok, becuase you may be starting DeskOS for the first time. Click OK to enter DeskOS.""")
except json.decoder.JSONDecodeError:
    btnjson = []
    messagebox.showinfo('First Time Setup',"Welcome to DeskOS! This prompt has appeared because your button config file could not be read/found. But that's ok, becuase you may be starting DeskOS for the first time. Click OK to enter DeskOS.")
dialogOpen = False
colors = ['white','black','red','green','blue','cyan','yellow','magenta']

def prgfindingerror():
    messagebox.showerror('Program not found','The program associated with this button is either not installed or an error has occured and the program could not be found at the path specified. This could be down to the file being moved, renamed or deleted. If this is not the case, please remove and setup the button using the editor again',icon='error')

def prgOpen(file):
    global btnjson
    #jsonlist = json.loads(open(r'Data\btnstore.json',mode='r').read())
    try:
        for obj in btnjson:
            if obj['Name'] == file:
                print(file)
                fil = obj['Path']
                print(fil)
                filename = fil.replace("/","\\")
                print(filename)
                os.startfile('"'+filename+'"')
                break
    except FileNotFoundError:
        prgfindingerror()
        
def rightclickmenu(event):
    print(event)
    
def btns(parentwin,reloadBool):
    x = 1
    #jsonlist = json.loads(open(r'Data\btnstore.json',mode='r').read())
    global xcoord,ycoord,fgchange,btnjson
    if reloadBool == True:
        deleting = True
        while deleting == True:
            try:
                globals()['btn%s' % x].destroy()
                x += 1
            except KeyError:
                print('Finished removing buttons, moving on to adding...')
                parentwin.update()
                deleting = False
        if window != None:
            window.destroy()
    x = 1
    xcoord = 130
    ycoord = 550
    print(btnjson)
    for obj in btnjson:
        if obj['Color'] in fgchange:
            fore = "black"
        if obj['Color'] not in fgchange:
            fore = "white"
        if xcoord > 1300:
            ycoord += 40
            xcoord = 130
            globals()['btn%s' % x] = Button(parentwin,text=obj['Name'],command= lambda m=obj['Name']:prgOpen(m),bg=obj['Color'],fg=fore)
            continue
        globals()['btn%s' % x] = Button(parentwin,text=obj['Name'],command= lambda m=obj['Name']:prgOpen(m),bg=obj['Color'],fg=fore)
        globals()['btn%s' % x].place(y=ycoord,x=xcoord)
        globals()['btn%s' % x].bind("<Button-3>", rightclickmenu)
        print(obj['Path']+" added")
        xcoord += int(len(str(obj['Name']))) * 5
        xcoord += 40
        x += 1
        parentwin.update()


def filechooser():
    global usrpath,dialogOpen
    if dialogOpen == True:
        return
    dialogOpen = True
    usrpath = fd.askopenfilename(title='Choose the file to be accessed on the button',initialdir='/')
    dialogOpen = False
    
def deletebutton():
    filnam = nameinput.get("1.0",'end-1c')
    filename = filnam.replace('\n','')
    for i in range(len(btnjson)):
        if btnjson[i]['Name'] == filename:
            del btnjson[i]
            break
        if btnjson[i]['Name'] == filename+'...':
            del btnjson[i]
            break
    jsonString = json.dumps(btnjson)
    open(r'Data\btnstore.json',"w").write(jsonString)
    messagebox.showinfo(title="Complete",message='The operation was completed, remember to click the refresh button to show your changes')

def check():
    filnam = nameinput.get("1.0",'end-1c')
    filename = filnam.replace('\n','')
    for i in range(len(btnjson)):
        if btnjson[i]['Name'] == filename:
            messagebox.showerror(title='Program listed',message='This program is already listed as a button, please remove and re-add the button to make changes to it')
            return
    else:
        write(filename)

def write(filename):
    global usrpath
    if len(filename) > 20:
        filename = filename[:20] + "..."
    if usrpath == "":
        usrpath = pathinput.get("1.0",'end-1c')
    obj = {"Name":filename,"Path":usrpath,"Color":dropText.get()}
    btnjson.append(obj)
    jsonString = json.dumps(btnjson)
    open(r'Data\btnstore.json',"w").write(jsonString)
    messagebox.showinfo(title="Complete",message='The operation was completed, remember to click the refresh button to show your changes')

def btnedit(parentwin):
    global nameinput,dropText,pathinput,window
    window = Tk()
    window.title('Button Editor')
    window.iconbitmap(r"Data\mainicon.ico")
    window.attributes('-topmost',True)
    Button(window,text="Choose a file",command=filechooser).pack()
    pathinput = Text(window,height=1,width=40)
    pathinput.pack()
    Label(window,text='Use the text box to name the button,\n or type the name of a button to remove,\n and press remove').pack()
    nameinput = Text(window,height=1,width=40)
    nameinput.pack()
    Button(window,text="Submit",command=check).pack()
    Button(window,text="Remove a button",command=deletebutton).pack()
    Label(window,text="Pick a background color, default is white").pack()
    dropText = StringVar(window)
    dropText.set(colors[0])
    dropdown = OptionMenu(window,dropText, *colors)
    dropdown.pack()
    window.geometry('300x300')
    window.protocol("WM_DELETE_WINDOW", lambda: btns(parentwin,True))
    window.mainloop()
