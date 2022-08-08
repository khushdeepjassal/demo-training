from turtle import width
from pyqrcode import create
import tkinter

root = tkinter.Tk()
root.title('Qr Code Generator')
root.geometry('600x700')
root['bg']='sky blue'
data = tkinter.Entry(root)



def gen_qr():
    global dta
    dta = data.get()
    dta = create(dta)
    test = dta.xbm(scale=5)
    global xbm_image
    xbm_image = tkinter.BitmapImage(data=test, foreground="black", background='white')
    image_view.config(image=xbm_image)
    statement.config(text="this is a qr code for : " + str(data.get()))


heading = tkinter.Label(root, text="QR code Generator",bg="SteelBlue3", font="times 30",width=28)
subtitle = tkinter.Label(root, text="Enter the data: ", font="times 20",bg='white',fg='blue',width=15)
make_button = tkinter.Button(root, text=" Make QR", font="times 15", command=gen_qr,bg='orange',fg='white')
image_view = tkinter.Label(root)
statement = tkinter.Label(root)

# gui grid

# heading.grid(row=0, column=0, columnspan=2)
# subtitle.grid(row=4, column=0)
# data.grid(row=4, column=1)
# make_button.grid(row=6, column=0, columnspan=2)
# image_view.grid(row=8, column=0, columnspan=2)
# statement.grid(row=10, column=0, columnspan=2)
heading.place(x=30,y=30)
subtitle.place(x=35,y=100)
data.place(x=35,y=150)
make_button.place(x=35,y=180)
image_view.place(x=35,y=250)
statement.place(x=35,y=550)
root.mainloop()