import pyttsx3

# Initialize the text-to-speech engine
engine = pyttsx3.init()

# Function to speak text
def speak(text):
    engine.say(text)
    engine.runAndWait()

# Function to present choices and get player input
def get_choice(choices):
    while True:
        speak(" ".join(choices.keys()))
        user_input = input("Enter your choice: ").lower()
        if user_input in choices:
            return user_input
        else:
            speak("Please select a valid option.")

# Function to handle the player's choice
def handle_choice(choice):
    if choice == "enter":
        speak("You cautiously enter the mansion.")
        enter_mansion()
    elif choice == "ignore":
        speak("You decide to ignore the mansion and continue your journey.")
        speak("You walk away, leaving the mansion behind.")
        speak("The End.")
    else:
        speak("Invalid choice.")

# Function to continue the story after entering the mansion
def enter_mansion():
    speak("As you step inside, the door slams shut behind you.")
    speak("You find yourself in a dimly lit hallway.")
    speak("To your left is a staircase leading up, and to your right is a doorway.")
    
    choices = {
        "left": "Climb the staircase",
        "right": "Enter the doorway"
    }
    
    choice = get_choice(choices)
    
    if choice == "left":
        speak("You climb the staircase.")
        speak("As you reach the top, you hear a faint whisper.")
        speak("You turn around and see a ghostly figure.")
        speak("Terrified, you run back downstairs and out of the mansion.")
        speak("The End.")
    elif choice == "right":
        speak("You enter the doorway and find yourself in a dusty library.")
        speak("You notice a book on the table with a strange symbol on its cover.")
        speak("Do you want to open the book?")
        
        choices = {
            "yes": "Open the book",
            "no": "Leave the book alone"
        }
        
        choice = get_choice(choices)
        
        if choice == "yes":
            speak("You open the book and a burst of light engulfs you.")
            speak("When the light fades, you find yourself back outside the mansion, unharmed.")
            speak("You walk away, grateful to have escaped the haunted mansion.")
            speak("The End.")
        elif choice == "no":
            speak("You decide to leave the book alone.")
            speak("You leave the library and explore other parts of the mansion.")
            speak("As you wander deeper into the mansion, you feel a chill down your spine.")
            speak("Suddenly, the lights flicker and you hear eerie whispers.")
            speak("You realize you are not alone...")
            speak("The End.")
        else:
            speak("Invalid choice.")

# Main function to start the story
def main():
    speak("Welcome to 'The Haunted Mansion'.")
    speak("You are traveling through a dark forest when you come across an old, abandoned mansion.")
    speak("Do you want to enter the mansion or ignore it?")
    
    choices = {
        "enter": "Enter the mansion",
        "ignore": "Ignore the mansion and continue your journey"
    }
    
    choice = get_choice(choices)
    handle_choice(choice)

if __name__ == "__main__":
    main()