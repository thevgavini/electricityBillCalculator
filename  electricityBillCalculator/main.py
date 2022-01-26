from tkinter import *
from functions import billCalculate
root=Tk()
root.title("Electricity Bill Calculator")
root.geometry("500x600")

def calBill(unitsC):
    ostring=f"The total bill is ₹{billCalculate(unitsC)}/-"
    output_field.insert(END, ostring)

def calButton():
    if output_field.get():
        output_field.delete(0,END)
    calBill(units_field)
    
def reset():
    units_field.delete(0,END)
    output_field.delete(0,END)

my_heading=Label(root, text="Electricity Bill Calculator", font=("Helvetica", 34))
my_heading.pack(pady=20)

lab_final=Label(root, text="Enter the units consumed", font=("Helvetica" ,24))
lab_final.pack(pady=10)


units_field = Entry(root, font=("Helvetica", 22), justify=CENTER, width=30, bd=0, bg="white")
units_field.pack(pady=10)

calc_button = Button(root, text="Calculate Power Bill", justify=LEFT, command=calButton, font=("Helvetica",24))
calc_button.pack(pady=20)

reset_button = Button(root, text="Reset Fields", justify=RIGHT, command=reset , font=("Helvetica" ,24))
reset_button.pack(pady=20)

output_field = Entry(root, font=("Helvetica", 22), justify=CENTER, width=30, bd=0, bg="white")
output_field.pack(pady=20)

root.mainloop()