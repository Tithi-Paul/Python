hour = float(input("Enter Hours: "))
rate = float(input("Enter Rate: "))
if hour <= 40:
    pay = hour*rate

else:
    pay = 40*rate + (hour-40)*rate*1.5

print("Pay: ", pay)