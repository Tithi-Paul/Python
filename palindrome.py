def is_palindrome(input_string):
	# We'll create two strings, to compare them
	new_string = ""
	New_List = input_string.split()
	for i in New_List:
	  new_string += i
	
	reverse_string = ""
	Upper = new_string.upper()
	n = len(Upper)
	for i in range(0,n):
	  reverse_string += Upper[-i-1]
	  
	if reverse_string == Upper:
		return True
	return False

print(is_palindrome("Never Odd or Even")) # Should be True
print(is_palindrome("abc")) # Should be False
print(is_palindrome("kayak")) # Should be True
