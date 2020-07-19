def format_name(first_name, last_name):
	N= "Name: "
	if len(first_name)>0 and len(last_name)>0:
		N +=last_name
		N += " , "
		N += first_name
	elif len(first_name) > 0:
		N += first_name
	elif len(last_name) > 0:
		N += last_name
	else:
		N = ""
	return N


print(format_name("Ernest", "Hemingway"))
# Should return the string "Name: Hemingway, Ernest"

print(format_name("", "Madonna"))
# Should return the string "Name: Madonna"

print(format_name("Voltaire", ""))
# Should return the string "Name: Voltaire"

print(format_name("", ""))
# Should return an empty string
