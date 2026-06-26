# Beginner-friendly AI chatbot example in Python
# This chatbot uses user input, if-else conditions, and a while loop.

print("Welcome!")
print("Type 'quit' to exit.")

# Keep chatting until the user types 'quit'.
while True:
    user_input = input("You: ").strip().lower()

    # Exit condition for the while loop.
    if user_input == "quit":
        print("AI: Goodbye!")
        break

    # Check for empty input.
    if user_input == "":
        print("AI: Please type something.")
        continue

    # Respond based on user input using if-else conditions.
    if "hello" in user_input or "hi" in user_input:
        print("AI: Hello!")
    elif "how are you" in user_input:
        print("AI: I am fine.")
    elif "name" in user_input:
        print("AI: I am a Python chatbot.")
    elif "weather" in user_input:
        print("AI: I cannot check the weather.")
    elif "joke" in user_input:
        print("AI: Why did the computer go to school? To improve its memory!")
    else:
        print("AI: I don't understand.")

        