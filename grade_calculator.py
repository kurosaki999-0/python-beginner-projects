# Student Grade Calculator

# Taking marks from user
physics = int(input("Enter Physics marks: "))
chemistry = int(input("Enter Chemistry marks: "))
maths = int(input("Enter Maths marks: "))


# Calculating total marks
total = physics + chemistry + maths

# Calculating percentage
percentage = (total / 300) * 100


# Showing total and percentage
print("Total Marks:", total)
print("Percentage:", percentage)


# Checking if student failed in any subject
if physics < 33 or chemistry < 33 or maths < 33:

    print("Grade: F")
    print("Failed")

# Grade calculation
elif percentage >= 90:

    print("Grade: A")
    print("Excellent Performance!")

elif percentage >= 70:

    print("Grade: B")
    print("Good Performance!")

elif percentage >= 60:

    print("Grade: C")
    print("Keep Improving")

elif percentage >= 33:

    print("Grade: D")
    print("Need More Practice")

else:

    print("Grade: F")
