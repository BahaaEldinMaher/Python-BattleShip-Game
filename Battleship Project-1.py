from random import randint
from tkinter import*
beeb=Tk()



beeb.title("Battle Ship Game")


beeb.geometry('600x400+150+150')

mlabel=Label(text="Welcome to Battleship Game").place(x=200, y=10)

mlabel=Label(text="Begin your Battle", fg='black', bg='dodger blue').place(x=290, y=100)

mbutton=Button(text="Start", fg='royal blue', relief=RAISED, cursor='pirate').place(x=290, y=50)


mentry=Entry(beeb)
mentry.place(x=290, y=130)

beeb.configure(background='Steel Blue2')





mbutton=Button(text="x", cursor='pirate').grid(row =0, column=1)
mbutton=Button(text="x", cursor='pirate').grid(row =0, column=2)
mbutton=Button(text="x", cursor='pirate').grid(row =0, column=3) 
mbutton=Button(text="x", cursor='pirate').grid(row =0, column=4)
mbutton=Button(text="x", cursor='pirate').grid(row =0, column=5)
mbutton=Button(text="x", cursor='pirate').grid(row =0, column=6)
mbutton=Button(text="x", cursor='pirate').grid(row =1, column=1)
mbutton=Button(text="x", cursor='pirate').grid(row =1, column=2)
mbutton=Button(text="x", cursor='pirate').grid(row =1, column=3)
mbutton=Button(text="x", cursor='pirate').grid(row =1, column=4)
mbutton=Button(text="x", cursor='pirate').grid(row =1, column=5)
mbutton=Button(text="x", cursor='pirate').grid(row =1, column=6)
mbutton=Button(text="x", cursor='pirate').grid(row =2, column=1)
mbutton=Button(text="x", cursor='pirate').grid(row =2, column=2)
mbutton=Button(text="x", cursor='pirate').grid(row =2, column=3)
mbutton=Button(text="x", cursor='pirate').grid(row =2, column=4)
mbutton=Button(text="x", cursor='pirate').grid(row =2, column=5)
mbutton=Button(text="x", cursor='pirate').grid(row =2, column=6)
mbutton=Button(text="x", cursor='pirate').grid(row =3, column=1)
mbutton=Button(text="x", cursor='pirate').grid(row =3, column=2)
mbutton=Button(text="x", cursor='pirate').grid(row =3, column=3)
mbutton=Button(text="x", cursor='pirate').grid(row =3, column=4)
mbutton=Button(text="x", cursor='pirate').grid(row =3, column=5)
mbutton=Button(text="x", cursor='pirate').grid(row =3, column=6)



beeb.mainloop()


              
#Map section
#
Map=[]

for i in range(0,4):
    Map.append(["x"]*6)
    
print(Map)

def make_map(Map):
    for row in Map: 
        print (" ".join(row))
        
make_map(Map)
#^^^^^^^^^^^^^^^^^^^^^^^^^^^^^#
#
def randROW(Map):
    return randint(0,len(Map)-1)

def randCOL(Map):
    return randint(0,len(Map)-1)

randROW(Map)
randCOL(Map)

ship_row = randROW(Map)
ship_col = randCOL(Map)
#^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^#
for turn in range(4):
    print("Turn",turn+1)

    guess_row = int(input("Try your shot(in row)!': "))
    guess_col = int(input("Try your shot(in col)!: "))
    
    print(ship_row)
    print(ship_col)
                
    #gameplay#>>
    if(guess_row == ship_row and guess_col == ship_col):
        print("winner winner shawrma dinner")
        break
    
    elif (5 <= guess_row) or (5 <= guess_col):           
            print("Oops it's out of map range")
        
    else:        
            print("You missed my ship!")
            Map[guess_row][guess_col]="0"
            if turn == 3:
                print("Game Over")
            
    print(make_map(Map))

