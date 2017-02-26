place = input("What place is your doggie? ")
array = [] 
def generate(num):
	if num in  (11,12,13):
		string = str(num) + 'th'
		return string	
	elif num % 10 == 1:
		string = str(num) + 'st'
		return string	
	elif num % 10 == 2:
		string = str(num) + 'nd'
		return string	
	elif num % 10 == 3:
		string = str(num) + 'rd'
		return string	
	else:
		string = str(num) + 'th'
		return string	

contestants = input("How many contestants? ")

for i in range(1,int(contestants)+1):
	if str(i) == place:
		continue
	else:
		array.append(generate(i))

print(array)		

