#### EXAMPLES ####
print("Hello"[0]) #Picking the first letter of the string -> This method is called 'Subscript'
print(1+5)
print(123_456_789) #Python ignores the underscores -> It's like a comma (Dot in portuguese), just to be more readable

test = len(input("What's your name? "))
print(type(test)) #Seeing what's the type of the variable

#Type cast -> converting a type to another type. Int to String, for example
casting = str(test)
print("Your name has " + casting + " characters")


#### CLASS 21 ####
number = input("Write a number: ")
print(int(number[0]) + int(number[1]))


#### CLASS 22 ####

print(type(6/2)) #The division always returns a float
print(2 ** 2) 

#PEMDAS - Order of priority:
    # () Parentheses
    # ** Exponents
    #  * Multiplication
    #  / Division
    #  + Addition
    #  - Subtraction

#### CLASS 23 ####
height = input("Write your height: ")
weight = input("Write your weight: ")
imc = int(weight) / float(height) ** 2
print("Your BMI is: " + str(imc))

#### CLASS 24 ####
print(round((9/2), 3)) #Three decimal places
print(9//2) #Cutting all of decimal places, Int type

#F-String
number = 10
number2 = 20
print(f"Your number is {number}, and your number 2 is {number2}.")

#### CLASS 25 ####
age = int(input("Write your age: "))
years = 90 - age
weeksLeft = years * 52
print(f"You have {weeksLeft} weeks left.")

