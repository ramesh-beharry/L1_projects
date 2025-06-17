# June 16, 2025 AI welcome message project

'''

This is the initial code without the input field


# 1. Creating a variable called 'user_name' and storing the text "Alice" in it
user_name = "Alice"

# 2. Creating a variable called 'age' and storing the number 30 in it
age = 30

# 3. Creating a variable called 'is_student' and storing a boolean value (True/False) in it
is_student = True

# Now we can use these variables
print(f"User Name: {user_name}")
print(f"Age: {age}")
print(f"Is Student: {is_student}")

# We can also change the value of a variable
age = 31
print(f"New Age: {age}")




'''


# here is the revised code


# 1. Prompt the user to enter their name and store it in the 'user_name' variable
# The input() function pauses the program and waits for the user to type something and press Enter.
user_name = input("Please enter your name: ")

# 2. Define the event name and month
event_name = "AI Native"
event_month = "June 2025"

# 3. Create a custom welcome message using an f-string (formatted string literal)
# F-strings allow you to embed variables directly inside string literals by prefixing the string with 'f' or 'F'
# and enclosing expressions in curly braces {}.
welcome_message = f"Welcome {user_name} to {event_name} {event_month}!"

# 4. Print the welcome message
print(welcome_message)

# You can also use the variables individually if needed
print(f"Glad to have you, {user_name}!")

