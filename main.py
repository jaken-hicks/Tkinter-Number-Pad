from playsound import playsound
from tkinter import*

def playone():
    playsound('p1.mp3')
def playtwo():
    playsound('p2.mp3')
def playthree():
    playsound('p3.mp3')
def playfour():
    playsound('p4.mp3')
def playfive():
    playsound('p5.mp3')
def playsix():
    playsound('p6.mp3')
def playseven():
    playsound('p7.mp3')
def playeight():
    playsound('p8.mp3')
def playnine():
    playsound('p9.mp3')
def playzero():
    playsound('p0.mp3')
def playstar():
    playsound('star.mp3')
def playpound():
    playsound('pound.mp3')
def playcall():
    playsound('calling.mp3')
def playhangup():
    playsound('hangup.mp3')


expression = ""

def press(num):
    global expression
    expression = expression + str(num)
    numbers.set(expression)

def clear():
    global expression
    expression = ""
    numbers.set("")

if __name__ == "__main__":
    gui = Tk()

    gui.configure(background="black")

    gui.title("Number Pad")

    gui.geometry("220x248")

    numbers = StringVar()
    input_field = Entry(gui, textvariable=numbers)
    input_field.grid(columnspan=3, ipadx=47.45, ipady=12)

    buttoncall = Button(gui, text=' Call ', fg='black', bg ='light green', command=lambda:[playcall(), press("")], height=2, width=9)
    buttoncall.grid(row=6, column=0)

    buttonhangup = Button(gui, text=' Hang Up ', fg='black', bg='red', command=lambda: [playhangup(), clear()], height=2, width=9)
    buttonhangup.grid(row=6, column=2)

    button0 = Button(gui, text=' 0 ', fg='black', command=lambda: [playzero(), press(0)],height=2, width=9)
    button0.grid(row=5, column=1)

    button1 = Button(gui, text=' 1 ', fg='black', command=lambda: [playone(), press(1)], height=2, width=9)
    button1.grid(row=2, column=0)

    button2 = Button(gui, text=' 2 ', fg='black', command=lambda: [playtwo(), press(2)], height=2, width=9)
    button2.grid(row=2, column=1)

    button3 = Button(gui, text=' 3 ', fg='black', command=lambda: [playthree(), press(3)], height=2, width=9)
    button3.grid(row=2, column=2)

    button4 = Button(gui, text=' 4 ', fg='black', command=lambda: [playfour(), press(4)], height=2, width=9)
    button4.grid(row=3, column=0)

    button5 = Button(gui, text=' 5 ', fg='black', command=lambda: [playfive(), press(5)], height=2, width=9)
    button5.grid(row=3, column=1)

    button6 = Button(gui, text=' 6 ', fg='black', command=lambda: [playsix(), press(6)], height=2, width=9)
    button6.grid(row=3, column=2)

    button7 = Button(gui, text=' 7 ', fg='black', command=lambda: [playseven(), press(7)], height=2, width=9)
    button7.grid(row=4, column=0)

    button8 = Button(gui, text=' 8 ', fg='black', command=lambda: [playeight(), press(8)], height=2, width=9)
    button8.grid(row=4, column=1)

    button9 = Button(gui, text=' 9 ', fg='black', command=lambda: [playnine(), press(9)], height=2, width=9)
    button9.grid(row=4, column=2)

    buttonstar = Button(gui, text=' * ', fg='black', command=lambda: [playstar() ,press("*")], height=2, width=9)
    buttonstar.grid(row=5, column=0)

    buttonpound = Button(gui, text=' # ', fg='black', command=lambda:[playpound(), press("#")], height=2, width=9)
    buttonpound.grid(row=5, column=2)

    gui.mainloop()
