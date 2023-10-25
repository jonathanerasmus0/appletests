# Score of 89 A
# score of 60 B
# 1. input functions
# 2. if statement
# 3. a few data types 
# 4. Use int and float function for data conversions
# true and true = true
# false and false = false
# false and true = false
user_input: str = input("What did you score in your exam?:")
score: int = int(user_input)

if score > 75 : 
	print("you have got an A")
elif (score > 65) and (score < 75) :
	print("you have got a B")	
elif  (score > 55) and (score < 65) :
	print("you have a C")		
else: 
	print("you have a pass")	

print ("Grading is done")				

