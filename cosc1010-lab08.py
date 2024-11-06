# Hannah Spicher
# UWYO COSC 1010
# 11/05/24
# Lab 08
# Lab Section: 11
# Sources, people worked with, help given to:
# your
# comments
# here


# Write a function that will properly check strings to see if they are an int or float, and convert them if so
# If they can't be converted return false
# Other wise return the converted int or float 
# Floats should only have one decimal point in them 
def tester(string):
    try:
        integer = int(string)
        return integer
    except ValueError:
        pass
    try:
        if string.count('.') == 1:
            float_number = float(string)
            return float_number
    except ValueError:
        pass

    return False
print(tester("12.3"))
print(tester("12.0"))
print(tester("1.2.1"))
print(tester("2..9"))


print("*" * 75)


# Point-slope y = mx + b
# This is used in mathematics to determine what the value y would be for any given x
# Where b is the y-intercept, where the line crosses the y-axis (x = 0)
# m is the slope of the line, the rate of change, how steep the line is
# x is the variable, and is determined by which point on the graph you wish to evaluate
# Create a function slope_intercept that takes in four parameters
    # m, the slope
    # b, the intercept
    # a lower x bound
    # an upper x bound
# Return a list for all values of y for the given x range, inclusive (whole number X's only)
# Check to make sure that the lower bound is less than or equal to the upper bound
# m, b can be floats or integers
# the bounds must be integers, if not return false
def slope_intercept (m,b,a,an):

    m_number = tester(m)
    b_number = tester(b)
    an_number = tester(an)
    a_number = tester(a)
    if a_number > an_number:
        return False
    if type(a_number)==float or type(an_number) == float:
        return False
    if ((m_number or m_number == 0) and (b_number or b_number ==0) and (a_number or a_number == 0) and (an_number or an_number == 0)):
        answer=[]
        for x in range(a_number, an_number+1):
            y=m_number*x+b_number
            answer.append(y)
        return answer
    

# Create a while loop to prompt users for their input for the four variables
# Exit on the word exit
# Remember all inputs are strings, but the function needs ints or floats
# Call your function and print the resulting list
while True:
    m = input("Enter the slope for your equation (b) or type 'exit' to quit:")
    if m.lower() == 'exit':
        break
    b = input("Enter the y-intercept for your equation (b) or type 'exit' to quit:")
    if b.lower() == 'exit':
        break
    a = input("Enter lower bound here (a) or type 'exit' to quit:")
    if a.lower() == 'exit':
        break
    an = input("Enter the upper bound here (an) or type 'exit' to quit:")
    if an.lower() == 'exit':
        break
    final_answer = slope_intercept(m,b,a,an)
    if final_answer is not False:
            print("The y values in the range:",final_answer)
    else:
            print("Error, try again")
            

print("*" * 75)


# Write a function to solve the quadratic formula
# https://en.wikipedia.org/wiki/Quadratic_formula
# Accept inputs for a, b, c
# Remember that this returns two values
# Create a loop like above to prompt the user for input for the three values
# Create a second function that just does the square root operation 
    # If the number you are trying to take the square root of is negative, return null
def quadratic_formula(a,b, c):
    if (sqrt(a,b,c) == False):
         return False
    x1= (-b + sqrt(a,b,c))/2*a
    
    x2 = (-b - sqrt(a,b,c))/2*a
    
    return x1, x2

def sqrt(a,b,c):
    y= (b**2)-(4*a*c)
    if y < 0:
        return False
    else:
        return y**(1/2)
while True:
    a = (input("Enter A value or type 'exit' to quit:"))
    if a.lower() == 'exit':
        break
    b = (input("Enter B value or type 'exit' to quit:"))
    if b.lower() == 'exit':
        break
    c = (input("Enter C value or type 'exit' to quit:"))
    if c.lower() == 'exit':
        break
    a=float(a)
    b=float(b)
    c=float(c)
    quad_answer = quadratic_formula(a,b,c)
    if quad_answer is not False:
            print("Answer:",quad_answer)
    else:
            print("Error, try again")
