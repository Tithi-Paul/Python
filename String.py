
First  =  "I Love My Country"
print(First[2:6])
print(First[-1])
print(First.find("My"))

stirngs_list = First.split()
print(stirngs_list)
print(stirngs_list[1])
print('.'.join(map(str, stirngs_list)))

To_Lower = First.lower()
print(To_Lower) 

To_Upper = First.upper()
print(To_Upper)

String_Summations = ""
for i in stirngs_list:
    String_Summations += i
print(String_Summations)

print("This is Example of Formate {}".format(To_Upper))

Neumeric = "522349"
print(Neumeric.isnumeric())
print(Neumeric.count("2"))
print(Neumeric.strip())

N = "12"
print("++",N.isalpha())

Reverse = ""
n = len(Neumeric)
for i in range(0,n):
    Reverse += Neumeric[-1-i]
print(Reverse)

ans = 12.3455
print("{:.1f}".format(ans))

def highlight_word(sentence, word):
	return(sentence.replace(word, word.upper()))

print(highlight_word("Have a nice day", "nice"))