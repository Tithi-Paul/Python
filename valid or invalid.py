def is_valid(x):
    if len(x) > 2:
        return True
    return False
def validate_users(users):
  for user in users:
    if is_valid(user):
      print(user + " is valid")
    else:
      print(user + " is invalid")
myList = ["purplecat"] 
validate_users(myList)
