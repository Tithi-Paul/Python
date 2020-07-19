def guest_list(guests):
  for a in guests:
    name , age , work = a
    print("{} is {} years old and works as {}.".format(name,age,work))
    

guest_list([('Ken', 30, "Chef"), ("Pat", 35, 'Lawyer'), ('Amanda', 25, "Engineer")])
