from flask import Flask, render_template, request

app = Flask(__name__)

# Your debugging_advice dictionary (copied from earlier)
debugging_advice = {
    "Your Goal or Intention for the Code": "Explain what you intended the code to do. For example, in this case, you could say: 'I want the lucky_number to be calculated by doubling a favorite_number, which I plan to set as 7.' This helps the AI understand the logic you're aiming for, not just the code as written.",
    "Steps to Reproduce the Error": "While you've already run the code and shown the output, for more complex issues, describing the exact steps you took to encounter the error is very helpful. This includes any inputs you provided, specific environment setups, or sequences of actions.",
    "Recent Changes Made": "If the code was working previously and you've recently made modifications, highlight those changes. For instance: 'I recently commented out the favorite_number line because I was experimenting with something, and now it's breaking.' This can give the AI clues about where the bug might have been introduced.",
    "Expected vs. Actual Output (Beyond the Error)": "If the code runs but produces incorrect results (not just an error), clearly state what you expected to see and what you actually saw. This helps the AI understand if the logic itself is flawed, even if there's no explicit error message.",
    "Constraints or Specific Requirements": "Mention any specific libraries you must use, performance requirements, or limitations you're working under. For example: 'I need this to run in Python 3.8,' or 'I'm trying to avoid using external libraries for this part.'"
}

@app.route('/', methods=['GET', 'POST'])
def index():
    advice_categories = list(debugging_advice.keys())
    selected_advice = None
    user_input_value = ""
    
    # This block executes when the user submits the form (POST request)
    if request.method == 'POST':
        user_choice_raw = request.form.get('user_choice', '').strip()
        user_input_value = user_choice_raw # Store user's input to re-fill the form field

        selected_key = None
        # Try to match by number first
        if user_choice_raw.isdigit():
            index = int(user_choice_raw) - 1
            if 0 <= index < len(advice_categories):
                selected_key = advice_categories[index]
        
        # If not a number or invalid number, try to match by name (case-insensitive)
        if selected_key is None:
            for key in advice_categories:
                if user_choice_raw.lower() == key.lower():
                    selected_key = key
                    break

        if selected_key:
            selected_advice = debugging_advice[selected_key]
        else:
            selected_advice = "Sorry, that's not a valid category. Please choose from the list or enter a correct number."
    
    # Render the HTML template, passing data from Python to HTML
    return render_template('index.html', 
                           categories=advice_categories, 
                           advice=selected_advice,
                           user_input=user_input_value)

# This runs the Flask development server when you execute app.py
if __name__ == '__main__':
    # debug=True allows for automatic reloading on code changes and more detailed error messages
    app.run(debug=True)


