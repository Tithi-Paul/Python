def pay_computation(hour, rate):
    if hour <= 40:
        pay = hour*rate

    else:
        pay = 40*rate + (hour-40)*rate*1.5
    return pay
    

h = float(input("Enter Hours: "))
r= float(input("Enter Rate: "))
money = pay_computation(h, r)
print(money)