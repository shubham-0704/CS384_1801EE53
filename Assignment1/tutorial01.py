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

#function to calculate power	
def power(num1, num2): #num1 ^ num2
	if(isinstance(num1,(int,float)) and isinstance(num2,(int,float))):
		if(num2==int(num2)):
			result=1
			for _ in range(int(num2)):
				result*=num1
			return round(result,3)
		else :return 0
	else :return 0

# Python 3 program to print GP.  geometric Progression
#You cant use the inbuilt python function. Write your own function
def printGP(a, r, n):
	if isinstance(a,(int,float)) and isinstance(r,(int,float)) and isinstance(n,(int,float)):
		if(n==int(n)):
			gp=[]
			for i in range(int(n)):
				gp.append(a*power(r,i))
			gp=[round(x,3) for x in gp]
			return gp 
		else :return 0
	else :return 0