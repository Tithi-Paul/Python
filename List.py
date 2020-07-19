
My_List = "I have a pen and I will write".split()
print(My_List)

My_List.append("poem")
print(My_List)

My_List.insert(1,"OK")
print(My_List)

My_List.remove("I")
print(My_List)

My_List.pop(3)
print(My_List)

My_List[0] = "I"
print(My_List)

for i , value in enumerate(My_List):
    print("{} - {} ".format(i+1 , value))

New = [("Hridoy", "14") , ("Tithi" , "26")]
for name, roll in New:
    print("Roll :{} & Name :{}".format(roll , name))

multiples = [x*7 for x in range(1,10)]
multiples += [x*3 for x in range(1,14)]
print(multiples)

multiples.sort()
print(multiples)
multiples.reverse()
print(multiples)


def guest_list(guests):
  for name,age,work in guests:
    print("{} is {} years old and works as {}.".format(name,age,work))

guest_list([('Ken', 30, "Chef"), ("Pat", 35, 'Lawyer'), ('Amanda', 25, "Engineer")])

#Dectionaries

file_count = {"jpg":10 , "txt":14 , "py":23}
print(file_count)
print(file_count["jpg"])
print("txt" in file_count)
file_count["py"] = 100
print(file_count)

for ext, amount in file_count.items():
    print("There are {} files in {}.".format(amount,ext))

for value in file_count.values():
    print(value)
for key in file_count.keys():
    print(key)

del file_count["py"]
print(file_count)


Mp = {}
text = [10,2,10,22,2,10]
for i in text:
    if i not in Mp:
        Mp[i] = 1
    else:
        Mp[i] += 1
print(Mp[20])

