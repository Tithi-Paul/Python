hr = input("Enter Hours: ")
rt = input("Enter Rate: ")
try:
    hour = float(hr)
    rate = float(rt)
    if hour <= 40:
        pay = hour*rate

    else:
        pay = 40*rate + (hour-40)*rate*1.5

    print("Pay: ", pay)
except:
    print("Error, please enter numeric input")