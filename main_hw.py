from tkinter import *
window = Tk()
window.title("Currency Converter")
window.geometry("1000x500")
window.config(background="white")

def convert1():
    amount = enter1.get()
    if amount.isdigit():
        euros = float(amount)*1.15
        label5.config(text="Converted Amount: €{}".format(euros),bg="white")

def convert2():
    amount = enter2.get()
    if amount.isdigit():
        dollars = float(amount)*1.35
        label6.config(text="Converted Amount: ${}".format(dollars),bg="white")

def convert3():
    amount = enter3.get()
    if amount.isdigit():
        rupees = float(amount)*107.67
        label7.config(text="Converted Amount: ₹{}".format(rupees),bg="white")
    




label1 = Label(window,text="Currency converter",bg="light green",font=("times",20))
label1.pack()

button1 = Button(window,text="Pounds -> Euros",height=1,width=25,bg="blue",font=("times",14),command=convert1)
button1.place(x=75,y=150)

button2 = Button(window,text="Pounds -> US dollars",height=1,width=25,bg="blue",font=("times",14),command=convert2)
button2.place(x=75,y=250)

button3 = Button(window,text="Pounds -> Rupees",height=1,width=25,bg="blue",font=("times",14),command=convert3)
button3.place(x=75,y=350)


label2 = Label(window,text="Enter Amount: ",font=("times",16),bg="white")
label2.place(x=350,y=155)

label3 = Label(window,text="Enter Amount: ",font=("times",16),bg="white")
label3.place(x=350,y=255)

label4 = Label(window,text="Enter Amount: ",font=("times",16),bg="white")
label4.place(x=350,y=355)


enter1 = Entry(window,width=30)
enter1.place(x=480,y=155,height=27)

enter2 = Entry(window,width=30)
enter2.place(x=480,y=255,height=27)

enter3 = Entry(window,width=30)
enter3.place(x=480,y=355,height=27)


label5 = Label(window,font=("times",16))
label5.place(x=150,y=200)

label6 = Label(window,font=("times",16))
label6.place(x=150,y=300)

label7 = Label(window,font=("times",16))
label7.place(x=150,y=400)




window.mainloop()