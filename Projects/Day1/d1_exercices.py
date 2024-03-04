print("Executes the input first, then print this input:")
print(input()) 

print("Executes the input first, after calculates the length  of the input, then print this input:")
print(len(input()))

print("Hello " + input("What's your name? ") + "!") #Executes the input first, followed by the print content

print("switch the values of A and B")

a = input()
b = input()

c = b
b = a
a = c

print("A: " + a)
print("B: " + b)



