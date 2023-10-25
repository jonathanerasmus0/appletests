# Examples of Loop
# Range gives a sequence of numbers 
# container of items list, tuple, dictinoary (iterable items)
#for item in range(5):
	# do anything we want
	#print("Everything went well!")
	#print("item", item)
#amount: int = 3000
#for number in range(4,11):
	# 4 5 6 7 8 9 10
	#print("item number", number)
	#amount += 100

#print("amount is", amount)	

#for item in range(2,9,3):
#	print("item number", item)

for item in range (10):
	print("item number", item)
	if item == 2:
		print("I want to go to the next item")
		continue
	elif item == 6:
		print("I am done with the loop")
		break
		print("going to the next item")
		pass
	else:
		print("I am done")
		
	



