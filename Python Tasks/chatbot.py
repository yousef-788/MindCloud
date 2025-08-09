user_name = None  # Store the user's name once they tell us

def format_number(number):
    """Format number to remove trailing zeros"""
    if number == int(number):
        return str(int(number))  # No decimal if it's a whole number
    else:
        return str(number).rstrip('0').rstrip('.')  # Remove extra zeros

def save_name(name):
    # Save the user's name so we can greet them later
    global user_name
    user_name = name
    return f"Hello, {user_name}! How can I help you today?"

def perform_math_operation(expression):
    try:
        # Let's figure out which math operation the user wants
        if '+' in expression:
            parts = expression.split('+')
            num1 = float(parts[0].strip())
            num2 = float(parts[1].strip())
            result = num1 + num2
            return f"The sum is: {format_number(result)}"
        elif '-' in expression:
            parts = expression.split('-')
            num1 = float(parts[0].strip())
            num2 = float(parts[1].strip())
            result = num1 - num2
            return f"The difference is: {format_number(result)}"
        elif '*' in expression:
            parts = expression.split('*')
            num1 = float(parts[0].strip())
            num2 = float(parts[1].strip())
            result = num1 * num2
            return f"The multiplication is: {format_number(result)}"
        elif '/' in expression:
            parts = expression.split('/')
            num1 = float(parts[0].strip())
            num2 = float(parts[1].strip())
            if num2 == 0:
                return "Error: Cannot divide by zero!"
            result = num1 / num2
            return f"The division is: {format_number(result)}"
        else:
            return "I can only perform '+', '-', '*' and '/' for now."
    except ValueError:
        return "Invalid numbers for mathematical operation."
    except Exception as e:
        return f"An error occurred during calculation: {e}"

def handle_unknown_question():
    # For questions the bot doesn’t understand
    return "I'm sorry, I don't understand that. Can you please rephrase your question or ask something else?"

def chat_bot():
    print("Hi! I'm a simple chatbot. What's your name?")
    while True:
        user_input = input("> ").strip().lower()

        if user_name is None:
            # First time we meet the user
            response = save_name(user_input.capitalize())
            print(response)
            print("\nYou can:")
            print("- Ask me to perform math operations: addition (+), subtraction (-), multiplication (*), or division (/)")
            print("- Examples: '5+3', '10-2', '4*7', '15/3'")
            print("- Ask me anything else, and I'll tell you if I understand")
            print("- Type 'exit' to quit")
        elif "+" in user_input or "-" in user_input or "*" in user_input or "/" in user_input:
            # If the input looks like math
            response = perform_math_operation(user_input)
            print(response)
        elif user_input == "exit":
            # Say goodbye and stop
            print(f"Goodbye, {user_name}! It was nice chatting with you.")
            break
        else:
            # We don't know how to handle it
            response = handle_unknown_question()
            print(response)

if __name__ == "__main__":
    chat_bot()
