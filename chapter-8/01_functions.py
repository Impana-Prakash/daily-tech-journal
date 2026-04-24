'''a = int(input("Enter your number: "))
b = int(input("Enter your number: "))
c = int(input("Enter your number: "))

average = (a + b + c) / 3
print(average)
'''

# a = 3
# b = 2
# c = 1

# average = (a + b + c) / 3
# print(average)

# Function Definition:

def avg():
    a = int(input("Enter your number: "))
    b = int(input("Enter your number: "))
    c = int(input("Enter your number: "))

    average = (a + b + c) / 3
    return average
print(avg())

avg()  # function call, it will execute the code inside the function and return the average of the three numbers entered by the user.



