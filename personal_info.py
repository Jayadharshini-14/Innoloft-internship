#Your First python Script
name="Jayadharshini"
age=18
gpa=8.8
is_student=True

print(f"Name: {name}")
print("Age:",age)
print("Type of age:",type(age))

#f-strings - modern way to format
print(f"Hello{name}! You are {age} years old")

#Taking input from user
#Ask users input
year=int(input("Enter your birth year:"))
currentage=2026-year
print(f"Current age of yours is {currentage},Your age in 10 years will be {currentage+10}")

