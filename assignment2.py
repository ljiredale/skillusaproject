#Lucas Iredale
#Webb AM Prosser
#SkillsUSA Entry Project
 
import tkinter as tk
from tkinter import *
import math
def nextScore():
    testScore.append(test.get())
    test.set("")
 
def finished():
    root.withdraw()
    tempScr = tk.Toplevel()
    tempScr.geometry("600x600")
    tempScr.title("Grade Calculator")
    tempScr.configure(bg = "#DF8376")
   
    #labels for title, person, and school name
    titleLab = Label(tempScr, text = 'Grade', bg = "#DF8376", font = "Helvetica 24", width = 14).place(x = 170, y = 20)
    nameLab = Label(tempScr, text = "Name:" + name.get(), bg = "#DF8376", font = "Helvetica 14").place(x = 150, y = 100)
    schoolLab = Label(tempScr, text = "School: " + school.get(), bg = "#DF8376", font = "Helvetica 14").place(x = 150, y = 140)
   
    #create total variable, then run through the list adding it up. then find average by dividing total by length
    tot = 0
    for i in range(len(testScore)):
        tot += testScore[i]
    avg = tot / len(testScore)
    avg2 = round(avg, 0)
    averageLab = Label(tempScr, text = "Average: " + str(int(avg2)) + "%", bg = "#DF8376", font = 'Helvetica 14').place(x = 150, y = 200)
    grade = ""
    #grade
    if avg >= 90:
        grade = "A"
    if avg >= 80 and avg <=89:
        grade = "B"
    if avg >= 70 and avg <= 79:
        grade = "C"
    if avg >= 60 and avg <= 69:
        grade = "D"
    if avg <60:
        grade = "F"
    gradeLab = Label(tempScr, text = "Grade: " + grade, bg = "#DF8376", font = 'Helvetica 14').place(x = 150, y = 250)
 
    #this part will run through the list of scores and find a highest and a lowest then will put it on a label
    highest = 0
    highestnum = 0
    lowest = 100
    lowestnum = 0
    for i in range(len(testScore)):
        if testScore[i]>highest:
            highest = testScore[i]
            highestnum = i
    for i in range(len(testScore)):
        if testScore[i]<lowest:
            lowest = testScore[i]
            lowestnum = i
   
    #labels for highest and lowest
    highestLab = Label(tempScr, text = "Highest: " + str(highest) + "%. This was the " + str(highestnum) + " score", bg = "#DF8376", width = 30, font = "Helvetica 14").place(x = 150, y = 300)
    lowestLab = Label(tempScr, text = "Lowest: " + str(lowest) + "%. This was the " + str(lowestnum) + " score", bg = "#DF8376", width = 30, font = "Helvetica 14").place(x = 150, y = 350)
 
#create root
root = tk.Tk()
root.geometry("600x600")
root.title("Student Grade Calculator")
root.configure(bg = "#DF8376")
 
#title
title = Label(root, text = "Student Grade Calculator", width = 20, font = "Helvetica 24", bg = "#DF8376").place(x = 100, y = 10)
 
#variables
testScore = []
 
#create labels and entries
 
nameLab = Label(root, text = "Name: ", bg = "#DF8376", width = 16, font = "Helvetica 16").place(x = 100, y = 100)
name = StringVar()
nameEnt = Entry(root, textvariable = name).place(x = 250, y = 105)
 
schoolLab = Label(root, text = "School Name: ", bg = "#DF8376", width = 16, font = "Helvetica 16").place(x = 90, y = 150)
school = StringVar()
schoolEnt = Entry(root, textvariable = school).place(x = 260, y = 155)
 
testLab = Label(root, text = "Test Score: ", bg = "#DF8376", width = 16, font = "Helvetica 16").place(x = 90, y = 200)
test = IntVar()
testEnt = Entry(root, textvariable = test).place(x = 260, y = 205)
 
#Buttons to reset entry or find grade
nextTest = Button(root, text = "Submit and Go to Next Test Score", width = 30, font = "Helvetica 12", bg = "#BB7065", command = lambda: nextScore()).place(x = 150, y = 250)
 
finish = Button(root, text = "Find Grade!", width = 10, font = "Helvetica 20", bg = '#65BB79', command = lambda: finished()).place(x = 200, y = 400)
 
 
root.mainloop()
