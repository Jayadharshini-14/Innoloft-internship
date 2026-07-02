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
user_name=input("Enter your name:")
user_age=int(input("Enter your age:"))
print(f"In 5 years,{user_name} will be {user_age+5}")
