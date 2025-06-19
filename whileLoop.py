def debugging_assistant():
    """
    Provides interactive debugging advice based on user's selection.
    The user can repeatedly ask for advice until they decide to stop.
    """
    debugging_advice = {
        "Your Goal or Intention for the Code": "Explain what you intended the code to do. For example, in this case, you could say: 'I want the lucky_number to be calculated by doubling a favorite_number, which I plan to set as 7.' This helps the AI understand the logic you're aiming for, not just the code as written.",
        "Steps to Reproduce the Error": "While you've already run the code and shown the output, for more complex issues, describing the exact steps you took to encounter the error is very helpful. This includes any inputs you provided, specific environment setups, or sequences of actions.",
        "Recent Changes Made": "If the code was working previously and you've recently made modifications, highlight those changes. For instance: 'I recently commented out the favorite_number line because I was experimenting with something, and now it's breaking.' This can give the AI clues about where the bug might have been introduced.",
        "Expected vs. Actual Output (Beyond the Error)": "If the code runs but produces incorrect results (not just an error), clearly state what you expected to see and what you actually saw. This helps the AI understand if the logic itself is flawed, even if there's no explicit error message.",
        "Constraints or Specific Requirements": "Mention any specific libraries you must use, performance requirements, or limitations you're working under. For example: 'I need this to run in Python 3.8,' or 'I'm trying to avoid using external libraries for this part.'"
    }

    # Convert keys to a list for easier display and validation
    advice_categories = list(debugging_advice.keys())

    while True: # Loop to allow repeated help
        print("\n--- Debugging Advice Categories ---")
        for i, category in enumerate(advice_categories):
            print(f"{i + 1}. {category}")
        print("-----------------------------------")

        user_choice_raw = input(
            "\nEnter the number or full name of the advice category you'd like to learn more about (e.g., '1' or 'Your Goal or Intention for the Code'): "
        ).strip()

        selected_key = None
        # Try to match by number first
        if user_choice_raw.isdigit():
            index = int(user_choice_raw) - 1
            if 0 <= index < len(advice_categories):
                selected_key = advice_categories[index]
        # If not a number or invalid number, try to match by name
        if selected_key is None:
            # Case-insensitive and flexible matching
            for key in advice_categories:
                if user_choice_raw.lower() == key.lower():
                    selected_key = key
                    break

        if selected_key:
            print(f"\n--- Advice for: {selected_key} ---")
            print(debugging_advice[selected_key])
            print("-----------------------------------")
        else:
            print("\nSorry, that's not a valid category. Please choose from the list or enter a correct number.")

        # Ask if the user needs more help
        needs_help_again = input("\nDo you need help with another debugging tip? (yes/no): ").lower().strip()
        if needs_help_again != 'yes':
            print("Alright! Happy debugging! Have a great day!")
            break # Exit the loop

# To run the function:
debugging_assistant()


