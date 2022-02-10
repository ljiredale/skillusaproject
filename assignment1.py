#Lucas Iredale
#Webb AM Prosser
#SkillsUSA Entry Project

#imports
from functools import total_ordering
import tkinter as tk
from tkinter import *
import random
import math
#Global Variables
 
 

#functions
def goBack(screen):
    #This function will delete the screen given, and will restart the main menu
    root.deiconify()
    screen.destroy()
 
 
def concessions():
    #This function will create a new toplevel which will have different options for concessions.
    root.withdraw() #hide the main menu
 
    #create a new temporary screen and give it a size, background, and title
    tempScr = tk.Toplevel()
    tempScr.geometry("600x600")
    tempScr.title("Concessions Selecter")
    tempScr.configure(bg = "#38B7AF")
    options = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
 
    #button to go back
    returnButt = Button(tempScr, text = "Go Back", bg = "#3FC7BE", font = "Helvetica 12", command = lambda: goBack(tempScr)).place(x = 515, y = 20)
   
    #title label
    titleLab = Label(tempScr, text = "Concession Selector", bg = "#38B7AF", font = "Helvetica 24").place(x = 150, y = 20)
 
    #Labels and OptionMenus for the Concessions
 
 
    #Small Popcorn
    smallPop = Label(tempScr, text = "Small Popcorn: $3.00", font = "Helvetica 16", bg = "#61A2FF", width = 18).place(x = 100, y = 100)
 
    #Create optionmenu to select how many they would like
    smallPopOption = OptionMenu(tempScr, smallPopAmt, *options).place(x = 350, y = 100)
 
    #Medium Popcorn
    mediumPop = Label(tempScr, text = "Medium Popcorn: $4.00", font = "Helvetica 16", bg = "#EEFF61", width = 18).place(x = 100, y = 150)
    mediumPopOption = OptionMenu(tempScr, mediumPopAmt, *options).place(x = 350, y = 150)
 
    #Large Popcorn
    largePop = Label(tempScr, text = "Large Popcorn: $5.00", font = "Helvetica 16", bg = "#61A2FF", width = 18).place(x = 100, y = 200)
    largePopOption = OptionMenu(tempScr, largePopAmt, *options).place(x = 350, y = 200)
 
    #Soda
    soda = Label(tempScr, text = "Soda: $2.00", font = "Helvetica 16", bg = "#EEFF61", width = 18).place(x = 100, y = 250)
    sodaOption = OptionMenu(tempScr, sodaAmt, *options).place(x = 350, y = 250)
 
    #Candy
    candy = Label(tempScr, text = "Candy: $1.00", font = "Helvetica 16", bg = "#61A2FF", width = 18).place(x = 100, y = 300)
    candyOption = OptionMenu(tempScr, candyAmt, *options).place(x = 350, y = 300)
 
    #Submit Button
    submit = Button(tempScr, text = "Done!", bg = "#3FC7BE", font = "Helvetica 20", width = 18, command = lambda: goBack(tempScr)).place(x = 110, y = 400)
 
 
def checkout():
   
    #This function will create a new toplevel which will checkout the user
    root.withdraw() #hide the main menu
 
    #create a new temporary screen and give it a size, background, and title
    tempScr = tk.Toplevel()
    tempScr.geometry("600x600")
    tempScr.title("Checkout")
    tempScr.configure(bg = "#38B7AF")
   
    #button to go back
    returnButt = Button(tempScr, text = "Go Back", bg = "#3FC7BE", font = "Helvetica 12", command = lambda: goBack(tempScr)).place(x = 515, y = 20)
 
    #title label
    titleLab = Label(tempScr, text = "Checkout", bg = "#38B7AF", font = "Helvetica 24").place(x = 200, y = 20)
 
    #This part of the code will show the amount of money was spent on each
    #Small Popcorn
    sPopNum = smallPopAmt.get()*3
    smallPop = Label(tempScr, text = "Small Popcorn: $" + str(sPopNum), font = "Helvetica 16", bg = "#61A2FF", width = 18).place(x = 150, y = 100)
 
    #Medium Popcorn
    mPopNum = mediumPopAmt.get()*4
    mediumPop = Label(tempScr, text = "Medium Popcorn: $" + str(mPopNum), font = "Helvetica 16", bg = "#EEFF61", width = 18).place(x = 150, y = 150)
 
    #Large Popcorn
    lPopNum = largePopAmt.get()*5
    largePop = Label(tempScr, text = "Large Popcorn: $" + str(lPopNum), font = "Helvetica 16", bg = "#61A2FF", width = 18).place(x = 150, y = 200)
 
    #Soda
    
    sodaNum = sodaAmt.get()*2
    soda = Label(tempScr, text = "Soda: $" + str(sodaNum), font = "Helvetica 16", bg = "#EEFF61", width = 18).place(x = 150, y = 250)
 
    #Candy
    canNum = candyAmt.get()
    candy = Label(tempScr, text = "Candy: $" + str(canNum), font = "Helvetica 16", bg = "#61A2FF", width = 18).place(x = 150, y = 300)
 
    #Total Amount
    totAmt = sPopNum+mPopNum+lPopNum+sodaNum+canNum
    totAmountLab = Label(tempScr, text = "Total Amount: $" + str(totAmt), width = 18, bg = "#38B7AF", font = "Helvetica 20").place(x = 100, y = 350)
 
    #Amount Imput Label
    amtInput = Label(tempScr, text = "Amount Pay With: ", bg = "#38B7AF", width = 16, font = "Helvetica 16").place(x = 40, y = 425)
    #Entry for Amount
    amtEntry = Entry(tempScr, textvariable = amountInputted, font = "Helvetica 16").place(x = 240, y = 425)
 
    #Done Button
    doneButt = Button(tempScr, text = "Done!", bg = "#2A8A84", width = 18, font = "Helvetica 24", command = lambda: checkoutDone(tempScr, totAmt)).place(x = 100, y = 500)
 
def checkoutDone(screen, tot): #screen to check and congratulate, then delete the information
    if int(amountInputted.get()) >= tot:
        screen.withdraw()
        tempScr = Toplevel()
        tempScr.geometry("600x600")
        tempScr.title("Congrats")
        tempScr.configure(bg = "#38B7AF")
        #labels and buttons to return and title
        returnButt = Button(tempScr, text = "Go Back", bg = "#38B7AF", font = "Helvetica 12", command = lambda: goBack(tempScr)).place(x = 515, y = 20)
        title = Label(tempScr, text = "Congrats!", bg = '#38B7AF', font = "Helvetica 24").place(x = 200, y = 20)
 
        #change return
        change = Label(tempScr, text = "Change: $" + str(int(amountInputted.get()) - tot), bg = "#38B7AF", font = "Helvetica 20", width = 18).place(x = 200, y = 300)

 
        smallPopAmt.set(0)
        mediumPopAmt.set(0)
        largePopAmt.set(0)
        sodaAmt.set(0)
        candyAmt.set(0)
       
 
def manager():
    root.withdraw() #hide the main menu
 
    #create a new temporary screen and give it a size, background, and title
    tempScr = tk.Toplevel()
    tempScr.geometry("600x600")
    tempScr.title("Manager")
    tempScr.configure(bg = "#38B7AF")
    #button to go back
    returnButt = Button(tempScr, text = "Go Back", bg = "#3FC7BE", font = "Helvetica 12", command = lambda: goBack(tempScr)).place(x = 515, y = 20)
 
    #title label
    titleLab = Label(tempScr, text = "Manager", bg = "#38B7AF", font = "Helvetica 24").place(x = 200, y = 20)
 
 
    #entry and label for password
    entlab = Label(tempScr, text = "Input Password: ", bg = "#38B7AF", font = "Helvetica 20")
    entlab.place(x = 100, y = 200)
    ent = Entry(tempScr, textvariable = password, show = "*")
    ent.place(x = 300, y = 210)
    
    manAmtSmallPop =+ int(smallPopAmt.get())
    manAmtMediumPop =+ int(mediumPopAmt.get())
    manAmtLargePop =+ int(largePopAmt.get())
    manAmtSoda =+ int(sodaAmt.get())
    manAmtCandy =+ int(candyAmt.get())
    
    #button to continue
    butt = Button(tempScr, text = "Click to Continue", bg = "#38B7AF", font = "Helvetica 16", command = lambda: manContinue(tempScr, entlab, ent, butt))
    butt.place(x = 100, y = 250)
 
def manContinue(screen, lab1, lab2, lab3):
    if password.get() == "7777":
        lab1.destroy()
        lab2.destroy()
        lab3.destroy()

        smallPopE = Label(screen, text = "Small Popcorn: " + str(manAmtSmallPop), bg = "#38B7AF", font = "Helvetica 12").place(x = 200, y = 100)
        mediumPopE = Label(screen, text = "Medium Popcorn: " + str(mediumPopAmt.get()), bg = "#38B7AF", font = "Helvetica 12").place(x = 200, y = 150)
        largePopE = Label(screen, text = "Large Popcorn: " + str(largePopAmt.get()), bg = "#38B7AF", font = "Helvetica 12").place(x = 200, y = 200)
        sodaE = Label(screen, text = "Soda: " + str(sodaAmt.get()), bg = "#38B7AF", font = "Helvetica 12").place(x = 200, y = 250)
        candyE = Label(screen, text = "Candy " + str(candyAmt.get()), bg = "#38B7AF", font = "Helvetica 12").place(x = 200, y = 300)
        amountToday = Label(screen, text = "Amount Today: $" + str(totAmt), bg = "#38B7AF", font = "Helvetica 12").place(x = 200, y = 400)
 
       
    else: #if password isn't 7777 it'll destroy
        screen.destroy()
 

 
   
 
 
 
 
 
 
 
#create the window, size, title, and background color
root = tk.Tk()
root.geometry("600x600")
root.title("Movie Theatre Concessions")
root.configure(bg = "#38B7AF")
 
#Global Variables
password = StringVar()
smallPopAmt = IntVar()
smallPopAmt.set(0)
mediumPopAmt = IntVar()
mediumPopAmt.set(0)
largePopAmt = IntVar()
largePopAmt.set(0)
sodaAmt = IntVar()
sodaAmt.set(0)
candyAmt = IntVar()
candyAmt.set(0)
amountInputted = StringVar()
totAmt = 0
manTotAmt= 0
manAmtSmallPop = 0
manAmtMediumPop = 0
manAmtLargePop = 0
manAmtSoda = 0
manAmtCandy = 0
 
#Main Title
title = Label(root, text = "Concession Menu", font = "Helvetica 24", bg = "#38B7AF").place(x = 175, y = 20)
 
#Buttons for Concessions, Checkout, and Manager
concButt = Button(root, text = "Concessions", bg = "#3FC7BE", width = 15, font = "Helvetica 16", command = lambda: concessions()).place(x = 210, y = 200)
checkoutButt = Button(root, text = "Checkout", bg = "#3FC7BE", width = 15, font = "Helvetica 16", command = lambda: checkout()).place(x = 210, y = 300)
managerButt = Button(root, text = "Manager", bg = "#3FC7BE", width = 15, font = "Helvetica 16", command = lambda: manager()).place(x = 210, y = 400)
 
 
 
 
root.mainloop()






