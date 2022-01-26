
def calButton():
    if output_field.get():
        output_field.delete(0,END)
    calBill(units_field)
    