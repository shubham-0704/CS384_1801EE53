# Function to add two numbers 
def add(num1, num2):
	if(isinstance(num1,(int,float)) and isinstance(num2,(int,float))):

		addition = num1 + num2
		return addition
	else :return 0

# Function to subtract two numbers 
def subtract(num1, num2): 
	if(isinstance(num1,(int,float)) and isinstance(num2,(int,float))):
		subtraction = num1 - num2
		return subtraction
	else :return 0

# Function to multiply two numbers 
def multiply(num1, num2): 
	#Multiplication Logic 
	if(isinstance(num1,(int,float)) and isinstance(num2,(int,float))):
		multiplication=num1*num2
		return multiplication
	else :return 0

# Function to divide two numbers 
def divide(num1, num2): 
	#DivisionLogic 
	if(isinstance(num1,(int,float)) and isinstance(num2,(int,float))):
		try:
			division = num1/num2
			return division
		except:
			return 0
	else: return 0
	