def lucky_number(name):
  number = len(name) * 9
  line = "Hello " + name + ". Your lucky number is " + str(number);
  return line;
print(lucky_number("Kay")) 
print(lucky_number("Cameron"))
