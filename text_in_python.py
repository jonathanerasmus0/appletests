# Topics

# Basic Control Structure
# Sequential control
# Selection/decision control statements
#

# if statements
# If else
# If elif else
# nested if statements


# for loops
# while loops
# range function


# functions

# For loop

# Today Thursday 26th of October 2023
# Text in Python



#new_string = 'today we are talking about text in python' # string doesnt need brackets
#new_string = "This is my second string"

# we can use escape quotes in a string by addng a \ at the start of quote and at the end of quote
#quotes_in_string = "Alex says \"Python is great\""
#print(quotes_in_string)

#name = 'Majid'# immutable


# Use of method / functions in string
#Long_string = " Alex is a python developer "

# find methods

#print(Long_string.find('python'))
#print(Long_string.find('python', 5, 20))

#index method

#print(Long_string.index('python'))

#isalpha method

#name = 'pawl'
#print(name.isalpha())

#isalpha method

#country = 'Germany'
#if country.isalpha():
#	print('it has only char values')
#else:
	#print('it does not consist of only characters')	

#is decimal

#country = 'Germany1'
'''
#if country.isalpha():
#	print('it has only char values')
#elif (country.isdecimal()):
#	print('it consists only decimals values')	
#else:
#	print ('the value of the coutry is not only chars as well as is not decimal')	
'''
#Capitalise

#info = 'i live in Berlin'
#print(info.capitalize())

# Upper case text 
''''
enter_first_value = input ('please enter Yes if you want to continue :')

if enter_first_value.upper() == 'YES':  # this is for UPPER CASE
	print('you choose to continue')
else:
	print(' you did not choose to continue')

	#lower method in string

enter_second_value = input('please enter Yes if you want to continue t learn lower case functions')

if enter_second_value.lower() == 'yes': # when comparing 2 values we MUST USE ==
	print('you decided to learn lower case')
else:
	print(' goodbye')

'''

'''
def withdraw_amount():
	user_amount = input ('please enter your amount here')
if user_amount.isdecimal():
	print('you entered the correct amount')
else:
	withdraw_amount()

withdraw_amount()
'''
# split

#fruits = 'Apples banana orange mango'
#print(fruits.split(' ',2))  #what you place within quotation marks if it isnt specified it will always use commas


# join functioh in string
#List_of_fruits = (apples banaas, oranges mango)
l#ist_of_fruits = ','.join(List_of_fruits) 


#
info = 'Hi eevryone I live in Berlin'
print (info.replace('Berlin','Munich'))

#Type casting
value = int = 12000

string_value = str(value) # int being converted to string









