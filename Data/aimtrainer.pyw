# Made By Owen A, DONT BLOODY NICK IT!
from tkinter import *
from tkinter import messagebox
import random
import time
import os
started = 0
reds = 0
dif_selected_easy = False
dif_selected_medium = False
dif_selected_hard = False
delayer = 2750
lives = 3
blues = 0
dif_selected = 0
destroyed = False
restarted = False
saved = False
subOpen = False
lastGreen = False
prevDiffMedium = False
prevDiffHard = False
prevDiffEasy = False
lastGreen = False
def restart():
    global blues,reds,delayer,lives,restarted,end
    if restarted == True:
        return
    restarted = True
    blues = 0
    reds = 0
    end.set("")
    if dif_selected_hard == True:
        delayer = 1500
        lives = 1
        updateTextSet()
        window_create()
    if dif_selected_medium == True:
        delayer = 2750
        lives = 3
        updateTextSet()
        window_create()
    if dif_selected_easy == True:
        delayer = 3500
        lives = 5
        updateTextSet()
        window_create()
def exiting():
    exit()
def start():
    global started,dif_selected,end
    if dif_selected_hard == True:
        dif_selected += 1
    if dif_selected_medium == True:
        dif_selected += 1
    if dif_selected_easy == True:
        dif_selected += 1
    if dif_selected == 1:
        if started == 0:
            started = 1
            dif_selected = 0
            end.set("")
            window_create()
        if started == 1:
            return
    else:
        messagebox.showerror(title="Error",message="No difficulty is selected, please select a difficulty.")
def easy():
    global delayer,lives,easybtn,dif_selected_easy,dif_selected_medium,dif_selected_hard,restarted,started
    if started == 1:
        return
    if restarted == True:
        return
    if dif_selected_easy == False:
        if dif_selected_hard == True:
            dif_selected_hard = False
            hardbtn.configure(bg="grey")
        if dif_selected_medium == True:
            dif_selected_medium = False
            medbtn.configure(bg="grey")
        delayer = 3500
        lives = 5
        easybtn.configure(bg="green")
        dif_selected_easy = True
        updateTextSet()
        scorewin.mainloop()
    if dif_selected_easy == True:
        pass
def medium():
    global delayer,lives,easybtn,dif_selected_medium,dif_selected_hard,dif_selected_easy,restarted,started
    if started == 1:
        return
    if restarted == True:
        return
    if dif_selected_medium == False:
        if dif_selected_hard == True:
            dif_selected_hard = False
            hardbtn.configure(bg="grey")
        if dif_selected_easy == True:
            dif_selected_easy = False
            easybtn.configure(bg="grey")
        delayer = 2750
        lives = 3
        medbtn.configure(bg="green")
        dif_selected_medium = True
        updateTextSet()
        scorewin.mainloop()
    if dif_selected_medium == True:
        pass
def hard():
    global delayer,lives,easybtn,dif_selected_hard,dif_selected_medium,dif_selected_easy,restarted,started
    if started == 1:
        return
    if restarted == True:
        return
    if dif_selected_hard == False:
        if dif_selected_easy == True:
            dif_selected_easy = False
            easybtn.configure(bg="grey")
        if dif_selected_medium == True:
            dif_selected_medium = False
            medbtn.configure(bg="grey")
        delayer = 1500
        lives = 1
        hardbtn.configure(bg="green")
        dif_selected_hard = True
        updateTextSet()
        scorewin.mainloop()
    if dif_selected_hard == True:
        pass
def updateTextSet():
    sb.set(str(blues)+" blue tiles hit")
    sr.set(str(reds)+" red tiles dodged")
    lv.set(str(lives)+" lives left")
    dev.set("Time: "+str(delayer/1000))
def wait():
    global root,destroyed,lives,rob,scorewin,reds,delayer
    if destroyed == False:
        if rob == "b":
            lives -= 1
            delayer += 250
        if rob == "r":
            reds += 1
        root.destroy()
        updateTextSet()
        window_create()
        return
def endofgame():
    global started,restarted,saved,end,prevDiffHard,prevDiffEasy,prevDiffMedium
    Button(scorewin, text="Restart", bg='orange',fg='black', command=restart).place(x=20,y=150)
    Button(scorewin, text="Submit", bg='orange',fg='black', command=user_window).place(x=120,y=150)
    restarted = False
    saved = False
    if dif_selected_hard == True:
        prevDiffHard = True
        prevDiffEasy = False
        prevDiffMedium = False
    if dif_selected_medium == True:
        prevDiffMedium = True
        prevDiffEasy = False
        prevDiffHard = False
    if dif_selected_easy == True:
        prevDiffEasy = True
        prevDiffMedium = False
        prevDiffHard = False
    started = 0
    scorewin.mainloop()
def disable_event():
    pass
def oh_no():
    global root,delayer,lives,destroyed,scorewin,reds
    destroyed = True
    root.destroy()
    delayer += 250
    lives -= 1
    updateTextSet()
    window_create()
def on_click():
    global root,delayer,lives,blues,destroyed
    destroyed = True
    root.destroy()
    blues += 1
    delayer = int((delayer/1.04)//1)
    updateTextSet()
    window_create()
def on_green():
    global root,delayer,lives,destroyed,lastGreen
    destroyed = True
    lastGreen = True
    root.destroy()
    delayer += 100
    updateTextSet()
    window_create()
def window_create():
    global root,lives,delayer,destroyed,rob,scorewin,lastGreen
    destroyed = False
    if lives == 0:
        end.set("You have lost, you hit "+str(blues)+" blue tiles.\n Press the exit button to quit.")
        endofgame()
    if lastGreen == False:
        rob = random.choice("rrrbbbbbg")
    if lastGreen == True:
        rob = random.choice("rrrbbbbb")
    root = Toplevel(scorewin)
    if rob == "r":
        if dif_selected_easy == True:
            Button(root, text="             Click             \n\n", bg='red', command=oh_no).pack()
        if dif_selected_medium == True:
            Button(root, text="            Click            \n", bg='red', command=oh_no).pack()
        if dif_selected_hard == True:
            Button(root, text="     Click     \n", bg='red', command=oh_no).pack()
        lastGreen = False
    if rob == "b":
        if dif_selected_easy == True:
            Button(root, text="             Click             \n\n", bg='blue',fg='white', command=on_click).pack()
        if dif_selected_medium == True:
            Button(root, text="            Click            \n", bg='blue',fg='white', command=on_click).pack()
        if dif_selected_hard == True:
            Button(root, text="     Click     \n", bg='blue',fg='white', command=on_click).pack()
        lastGreen = False
    if rob == "g":
        if dif_selected_easy == True:
            Button(root, text="             Click             \n", bg='green',fg='white', command=on_green).pack()
        if dif_selected_medium == True:
            Button(root, text="         Click        \n", bg='green',fg='white', command=on_green).pack()
        if dif_selected_hard == True:
            Button(root, text="    Click   \n", bg='green',fg='white', command=on_green).pack()
        lastGreen = True
    root.protocol("WM_DELETE_WINDOW", disable_event)
    root.resizable(False,False)
    root.attributes('-topmost',True)
    root.geometry("+"+str(random.randint(1,1800))+"+"+str(random.randint(1,950)))
    root.after(delayer, wait)
    root.mainloop()
def score_save():
    global reds,blues,text,saved,userwin,dif_selected_easy,dif_selected_medium,dif_selected_hard,subOpen
    if saved == True:
        messagebox.showerror(title="Error",message="You have already saved this session's score.")
        return
    score = reds + blues
    file = open("scores.txt",'a')
    file.write(str(text.get(1.0, "end-1c"))+" "+str(score))
    if prevDiffEasy == True:
        file.write(" E")
        file.write("\n")
    if prevDiffMedium == True:
        file.write(" M")
        file.write("\n")
    if prevDiffHard == True:
        file.write(" H")
        file.write("\n")
    messagebox.showinfo(title="Saved Score", message="Your scored should be saved")
    userwin.destroy()
    saved = True
    subOpen = False
def user_window():
    global text,saved,userwin,subOpen
    if saved == True:
        messagebox.showerror(title="Error",message="You have already saved this session's score.")
        return
    if subOpen == True:
        return
    subOpen = True
    userwin = Tk()
    text = Text(userwin, width=20, height=1)
    text.pack()
    text.insert(END,"")
    Button(userwin, text="Submit", bg='grey',fg='black', command=score_save).pack()
scorewin = Tk()
scorewin.attributes('-topmost',True)
sb = StringVar(scorewin)
sr = StringVar(scorewin)
lv = StringVar(scorewin)
dev = StringVar(scorewin)
end = StringVar(scorewin)
Label(scorewin,textvar=sb).pack()
Label(scorewin,textvar=sr).pack()
Label(scorewin,textvar=lv).pack()
Label(scorewin,textvar=dev).pack()
Label(scorewin,textvar=end).place(x=0,y=115)
Button(scorewin, text="Exit", bg='green',fg='white', command=exiting).place(x=80,y=150)
Button(scorewin, text="Start", bg='Yellow',fg='black', command=start).place(x=20,y=150)
easybtn = Button(scorewin, text="Easy", bg='grey',fg='black', command=easy)
easybtn.place(x=20,y=85)
medbtn = Button(scorewin, text="Medium", bg='grey',fg='black', command=medium)
medbtn.place(x=60,y=85)
hardbtn = Button(scorewin, text="Hard", bg='grey',fg='black', command=hard)
hardbtn.place(x=125,y=85)
scorewin.title("Score")
scorewin.geometry("185x180")
updateTextSet()
scorewin.mainloop()
