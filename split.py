def format_address(address_string):
  my_list = address_string.split()
  # Declare variables

  # Separate the address string into parts

  # Traverse through the address parts
  n = len(my_list)
  name = ""
  for i in range(1,n):
      name += my_list[i]
      name += " "
        
    # Determine if the address part is the
    # house number or part of the street name

  # Does anything else need to be done 
  # before returning the result?
  
  # Return the formatted string  
  name = name.strip()
  return "house number {} on street named {}".format(my_list[0] , name)

print(format_address("123 Main Street"))
# Should print: "house number 123 on street named Main Street"

print(format_address("1001 1st Ave"))
# Should print: "house number 1001 on street named 1st Ave"

print(format_address("55 North Center Drive"))
# Should print "house number 55 on street named North Center Drive"

