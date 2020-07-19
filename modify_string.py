message = "A kong string with a silly typo"
#message[2] = "l"
new_message = message[0:2] + "l" + message[3:]
print(new_message)