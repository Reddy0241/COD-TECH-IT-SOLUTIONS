import random

# Define the questions and answers for each category
questions = {
    "History": {
        "What year did World War II end?": ["1945", "1942", "1950", "1939"],
        "Who was the first President of the United States?": ["George Washington", "Thomas Jefferson", "Abraham Lincoln", "John Adams"]
    },
    "Science": {
        "What is the chemical symbol for water?": ["H2O", "CO2", "O2", "H2SO4"],
        "Who developed the theory of relativity?": ["Albert Einstein", "Isaac Newton", "Stephen Hawking", "Galileo Galilei"]
    },
    "Geography": {
        "What is the capital of France?": ["Paris", "London", "Rome", "Berlin"],
        "Which continent is the largest by land area?": ["Asia", "Africa", "North America", "Europe"]
    }
}

# Function to ask a random question from a given category
def ask_question(category):
    question = random.choice(list(questions[category].keys()))
    answer_options = questions[category][question]
    correct_answer = answer_options[0]
    random.shuffle(answer_options)
    
    print(f"\n{category} Question:")
    print(question)
    for i, option in enumerate(answer_options):
        print(f"{i+1}. {option}")
    
    user_answer = int(input("Enter your answer (1/2/3/4): ")) - 1
    user_response = answer_options[user_answer]
    
    return user_response == correct_answer

# Function to conduct the quiz
def conduct_quiz():
    score = 0
    for category in questions.keys():
        print(f"\n{category} Category")
        print("=" * (len(category) + 10))
        result = ask_question(category)
        if result:
            print("Correct!")
            score += 1
        else:
            print("Incorrect!")
            print(f"The correct answer is {correct_answer}")
    
    print("\nQuiz Completed!")
    print(f"Your score is {score}/{len(questions)}")

if __name__ == "__main__":
    conduct_quiz()

