#Define a function
#def sum_numbers():
#	'''it helps to add two numbers'''
#	print("function sum_numbers was called")

#	sum_numbers()

#unction with an argument

#def sum_numbers(age: int):
#	'''it helps add two numbers'''
#	print("argument given is age",age)

#sum_numbers(400, 3000)

#Function with a return keyword

def sum_numbers(age: int, ratio: float):
#	'''it helps add two numbers'''
	print("argument given is age",age)
	result: float = age + ratio
	return result 

new_age = sum_numbers(400,20.0)
print(new_age)



