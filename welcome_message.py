def get_welcome_message(name):
    return f"Welcome, {name}! We're excited to have you here!"

def main():
    # Get user's name
    name = input("Please enter your name: ")
    
    # Generate and print welcome message
    welcome_message = get_welcome_message(name)
    print(welcome_message)

if __name__ == "__main__":
    main() 