def billCalculate(unitsC):
    if unitsC.get():
        units=int(unitsC.get())
        total=100
        if units > 200:
            total+=200*0.8
            if units > 300:
                total+=100*0.9
                total+=(units-300)*1
            else:
                total+=(units-200)*0.9
        else:
            total+=units*0.8


        if total>400:
            total+=0.15*total
        
        return total