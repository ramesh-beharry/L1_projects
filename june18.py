# June 2025 classwork 

# this script greets the user and calculates a lucky number

user_name = input("hello! what is your name?")

print(f"Nice to meet you, {user_name}!")

# this variable is intended to be used later
favorite_number = 7

lucky_number = favorite_number * 2

print(f"your lucky number is: {lucky_number}")

print("have a great day!")


'''

My python script [ enter code ] is giving me this error message: [ error message ]

What does this error mean? what part of my code is likely causing it suggest a fix.

Discuss how to give AI good context when asking for debugging help.




'''

debugging_advice = {
    "Your Goal or Intention for the Code": "Explain what you intended the code to do. For example, in this case, you could say: 'I want the lucky_number to be calculated by doubling a favorite_number, which I plan to set as 7.' This helps the AI understand the logic you're aiming for, not just the code as written.",
    "Steps to Reproduce the Error": "While you've already run the code and shown the output, for more complex issues, describing the exact steps you took to encounter the error is very helpful. This includes any inputs you provided, specific environment setups, or sequences of actions.",
    "Recent Changes Made": "If the code was working previously and you've recently made modifications, highlight those changes. For instance: 'I recently commented out the favorite_number line because I was experimenting with something, and now it's breaking.' This can give the AI clues about where the bug might have been introduced.",
    "Expected vs. Actual Output (Beyond the Error)": "If the code runs but produces incorrect results (not just an error), clearly state what you expected to see and what you actually saw. This helps the AI understand if the logic itself is flawed, even if there's no explicit error message.",
    "Constraints or Specific Requirements": "Mention any specific libraries you must use, performance requirements, or limitations you're working under. For example: 'I need this to run in Python 3.8,' or 'I'm trying to avoid using external libraries for this part.'"
}

# You can now access the advice like this:
# print(debugging_advice["Your Goal or Intention for the Code"])


def get_python_advice(key): 
    for key in debugging_advice:
        print(key)

    input("select what you would like to learn more about: ")




get_python_advice("Your Goal or Intention for the Code")






    