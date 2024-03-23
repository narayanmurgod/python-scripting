name = input('Enter your name:')
age = int(input("Enter your age:"))

if age > 18:
    print(f"hey {name}..! You can vote")
else:
    print(f"hey {name}..! You aren't eligible to vote")