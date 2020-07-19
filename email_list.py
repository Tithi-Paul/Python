def email_list(domains):
	emails = []
	for v in domains:
	  users = domains[v]
	  for user in users:
	    emails.append(user+"@"+v)
	return(emails)

print(email_list({"gmail.com": ["clark.kent", "diana.prince", "peter.parker"], "yahoo.com": ["barbara.gordon", "jean.grey"], "hotmail.com": ["bruce.wayne"]}))
