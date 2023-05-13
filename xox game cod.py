
from tkinter import*
from tkinter import messagebox

window=Tk()
window.title("welcome to my game world")
window.geometry("420x320")

lab1=Label(window,text="TIC  TAC  TOE",font=("arial" , "15"),fg="red")
lab1.grid(row=0,column=0)
lab2=Label(window,text="PLAYER__1:  X",font=("Helvetica" , "10"))
lab2.grid(row=2,columns=2)
lab3=Label(window,text="PLAYER__2:  O",font=("Helvetica" , "10"))
lab3.grid(row=3,columns=2)

turn=1;
def click1 ():
        global turn
        if but1["text"]==" ":
                if turn==1:
                        turn=2;
                        but1["text"]="X"
                elif turn==2:
                        turn=1;
                        but1["text"]="O"
                check();
def click2 ():
        global turn
        if but2["text"]==" ":
                if turn==1:
                        turn=2;
                        but2["text"]="X"
                elif turn==2:
                        turn=1;
                        but2["text"]="O"
                check();
def click3 ():
        global turn
        if but3["text"]==" ":
                if turn==1:
                        turn=2;
                        but3["text"]="X"
                elif turn==2:
                        turn=1;
                        but3["text"]="O"
                check();
def click4 ():
        global turn
        if but4["text"]==" ":
                if turn==1:
                        turn=2;
                        but4["text"]="X"
                elif turn==2:
                        turn=1;
                        but4["text"]="O"
                        check();
def click5 ():
        global turn
        if but5["text"]==" ":
                if turn==1:
                        turn=2;
                        but5["text"]="X"
                elif turn==2:
                        turn=1;
                        but5["text"]="O"
                check();
def click6 ():
        global turn
        if but6["text"]==" ":
                if turn==1:
                        turn=2;
                        but6["text"]="X"
                elif turn==2:
                        turn=1;
                        but6["text"]="O"
                check();
def click7 ():
        global turn
        if but7["text"]==" ":
                if turn==1:
                        turn=2;
                        but7["text"]="X"
                elif turn==2:
                        turn=1;
                        but7["text"]="O"
                check();
def click8 ():
        
        global turn
        if but8["text"]==" ":
                if turn==1:
                        turn=2;
                        but8["text"]="X"
                elif turn==2:
                        turn=1;
                        but8["text"]="O"
                check();
def click9 ():
        global turn
        if but9["text"]==" ":
                if turn==1:
                        turn=2;
                        but9["text"]="X"
                elif turn==2:
                        turn=1;
                        but9["text"]="O"
                check();
flag=1;
def check():
        global flag;
        b1=but1["text"];
        b2=but2["text"];
        b3=but3["text"];
        b4=but4["text"];
        b5=but5["text"];
        b6=but6["text"];
        b7=but7["text"];
        b8=but8["text"];
        b9=but9["text"];
        flag=flag +1;

        if b1==b2 and b1==b3 and b1=="O" or b1==b2 and b1==b3 and b1=="X":
                win(but1["text"])
        if b4==b5 and b4==b6 and b4=="O" or b4==b5 and b4==b6 and b4=="X":
                win(but4["text"])
        if b7==b8 and b7==b9 and b7=="O" or b7==b8 and b7==b9 and b7=="X":
                win(but7["text"])
        if b1==b4 and b1==b7 and b1=="O" or b1==b4 and b1==b7 and b1=="X":
                win(but1["text"])
        if b2==b5 and b2==b8 and b2=="O" or b2==b5 and b2==b8 and b2=="X":
                win(but2["text"])
        if b3==b6 and b3==b9 and b3=="O" or b3==b6 and b3==b9 and b3=="X":
                win(but3["text"])
        if b1==b5 and b1==b9 and b1=="O" or b1==b5 and b1==b9 and b1=="X":
                win(but1["text"])
        if b7==b5 and b7==b3 and b7=="O" or b7==b5 and b7==b3 and b7=="X":
                win(but7["text"])
        if flag ==10:
                messagebox.showinfo ("TIE","Match Tied!!! Try Again :)")
                window.destroy()

def win (player):
        ans="Game Complete" + player + "WINS";
        messagebox.showinfo("Congratulations", ans)
        window.destroy()

but1=Button(window, text=" ",bg="yellow",fg="black",width=5,height=2,font=("Helvetica" , "20"),command=click1)
but2=Button(window, text=" ",bg="yellow",fg="black",width=5,height=2,font=("Helvetica" , "20"),command=click2)
but3=Button(window, text=" ",bg="yellow",fg="black",width=5,height=2,font=("Helvetica" , "20"),command=click3)
but4=Button(window, text=" ",bg="yellow",fg="black",width=5,height=2,font=("Helvetica" , "20"),command=click4)
but5=Button(window, text=" ",bg="yellow",fg="black",width=5,height=2,font=("Helvetica" , "20"),command=click5)
but6=Button(window, text=" ",bg="yellow",fg="black",width=5,height=2,font=("Helvetica" , "20"),command=click6)
but7=Button(window, text=" ",bg="yellow",fg="black",width=5,height=2,font=("Helvetica" , "20"),command=click7)
but8=Button(window, text=" ",bg="yellow",fg="black",width=5,height=2,font=("Helvetica" , "20"),command=click8)
but9=Button(window, text=" ",bg="yellow",fg="black",width=5,height=2,font=("Helvetica" , "20"),command=click9)

but1.grid(row=2,column=4)
but2.grid(row=2,column=5)
but3.grid(row=2,column=6)
but4.grid(row=3,column=4)
but5.grid(row=3,column=5)
but6.grid(row=3,column=6)
but7.grid(row=4,column=4)
but8.grid(row=4,column=5)
but9.grid(row=4,column=6)

window.mainloop()
