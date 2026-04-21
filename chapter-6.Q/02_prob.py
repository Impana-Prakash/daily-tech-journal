
# Given 3 subjects marks, find the total percentage and check if the student is passed or failed. (pass mark is 40%)
marks1 = int(input("Enter marks of student 1: "))
marks2 = int(input("Enter marks of student 2: "))
marks3 = int(input("Enter marks of student 3: "))


# check for total percentage

total_percentage = (100 * (marks1 + marks2 + marks3) / 300)

if (total_percentage >= 40 and marks1>=33 and marks2>=33 and marks3>=33):
    print("You are Passed:", total_percentage)

else:
    print("You are Failed, try again!", total_percentage)

