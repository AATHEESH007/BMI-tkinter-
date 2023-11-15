# Imports all from Tkinter GUI Package
from tkinter import *
import random

def reset ():
    na.set("")
    ma.set(0)
    he.set(0)
    b.set(0)
    resLabelText.set("")


l = ['1@3$', '*76%', '0*6%', '2#6$', '%45&', '*7%&']
choose = random.choice(l)
print('for human verification pls enter the elements given below')
print(choose)
choose1 = input("enter the elements given above:")
if choose1 == choose:
    # Initialization
    app = Tk()
    ma = IntVar(None)
    he = IntVar(None)
    b = IntVar(None)
    na = StringVar(None)

    # Calculates Body Mass Index (BMI) with user inputs, then put the user in one of four categories
    # Also check if the values entered are not zero

    def calculate_bmi():
        try:
            bmi = float(mass.get()) / (float(height.get()) * float(height.get()))
            b.set(bmi)
        except ZeroDivisionError:
            ma.set(None)
            he.set(None)
            b.set(None)
            return
        if bmi < 18.5:
            resLabelText.set("you are categorised as Underweight")
        if 18.5 < bmi < 24.9:
            resLabelText.set("you are categorised as Normal")
        if 25 < bmi < 29.9:
            resLabelText.set("you are categorised as Overweight")
        if bmi > 30:
            resLabelText.set("you are categorised as Obese")
        return

    ########################### Graphical User Interface (Tkinter) ###########################################

    #  Sets size and title
    app.geometry("600x600")
    app.title("BMI Calculator")
    icon=PhotoImage(file='scl.png')
    app.iconphoto(True,icon)    
    app.config(background="#f1bd5d")

    # Label and text box for name
    nLabelText = StringVar()
    nLabelText.set("Enter your name: ")
    nameLabel = Label(app, textvariable=nLabelText ,font=("Garamond",20,'bold'),fg="blue",bg="#f1bd5d")
    nameLabel.pack()

    name = Entry(app, textvariable=na)
    name.pack()




    # Label and test box for mass in kg
    mLabelText = StringVar()
    mLabelText.set("Enter your weight in kg: ")
    massLabel = Label(app, textvariable=mLabelText ,font=("Garamond",20,'bold'),fg="blue",bg="#f1bd5d")
    massLabel.pack()

    mass = Entry(app, textvariable=ma)
    mass.pack()

    # Label and text box for height
    hLabelText = StringVar()
    hLabelText.set("Enter your height in meter: ")
    heightLabel = Label(app, textvariable=hLabelText,font=("Garamond",20,'bold'),fg="blue",bg="#f1bd5d")
    heightLabel.pack()

    height = Entry(app, textvariable=he)
    height.pack()

    # Button and label and textbox for BMI calculation and reset
    # Button for BMI calculation
    button = Button(app, text="Calculate BMI",font=("Garamond",20,'bold'),fg="blue",
                    bg="#f42424", activebackground='#f1bd5d', activeforeground='#f42424',
                    borderwidth=8, command=calculate_bmi)
    button.pack(padx=15, pady=15)
    # Button for reset
    button1 = Button(app, text="reset", font=("Garamond", 20, 'bold'), fg="blue",
                     bg="#f42424",activebackground='#f1bd5d', activeforeground='#f42424',
                     borderwidth=8, command=reset)
    button1.pack(padx=15, pady=20)

    #box for yor bmi
    bmiLabelText = StringVar()
    bmiLabelText.set("Your BMI is: ")
    bmiLabel = Label(app, textvariable=bmiLabelText,font=("Garamond",20,'bold'),fg="blue",bg="#f1bd5d")
    bmiLabel.pack()



    bmi = Entry(app,textvariable=b)
    bmi.pack()
    resLabelText = StringVar()
    resLabelText.set(" you are categorised as: ")
    resLabel = Label(app, textvariable=resLabelText,font=("Garamond",20,'bold'),fg="blue",bg="#f1bd5d")
    resLabel.pack()



    # Starts the GUI
    app.mainloop()

else:
    print('YOU FAILED HUMAN VERIFICATION I CONSIDER YOU AS A ROBO!!!!!!!')
