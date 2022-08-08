from tkinter import *
 
import phonenumbers
 
from phonenumbers import geocoder
 
from phonenumbers import carrier


 
root = Tk()
 
root.geometry("500x500")
 
label1 = Label(text="Phone Number Tracker",bg="SteelBlue3")
 
label1.pack()

 
def getResult():
    num = number.get("1.0",END)
    num = phonenumbers.parse(num)
    result.insert(END,"The country of this number is " + geocoder.description_for_number(num,"en"))
    result.insert(END,"\nThe sim card of this number is " + carrier.name_for_number(num,"en"),END)
    
 
number = Text(height=3)
 
number.pack()
 
button = Button(text="Submit",command=getResult)
 
button.pack()
 
result = Text(height=5)
 
result.pack()
 
root.mainloop()