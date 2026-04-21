marks = int(input("Enter your marks: "))
if(marks <=100 and marks >= 90):
    print("Your grade is A")
elif(marks <90 and marks >= 80):
    print("Your grade is B")    
elif(marks <80 and marks >= 70):
    print("Your grade is C")
elif(marks <70 and marks >= 60):
    print("Your grade is D")    
elif(marks <60 and marks >= 40):
    print("Your grade is E")    
elif(marks <40 and marks >= 0):
    print("You failed, try again!")                    