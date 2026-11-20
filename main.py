def run_quiz():
    questions = [
        {
            "question": "Which data type in Python is immutable (cannot be changed after creation)?",
            "options": ["A) List", "B) Dictionary", "C) Tuple", "D) Set"],
            "answer": "C"
        },
        {
            "question": "What keyword is used to define a function in Python?",
            "options": ["A) func", "B) def", "C) function", "D) lambda"],
            "answer": "B"
        },
        {
            "question": "What is the output of len([10, 20, 30, 40])?",
            "options": ["A) 3", "B) 4", "C) 5", "D) Error"],
            "answer": "B"
        },
        {
            "question": "Which operator is used for exponentiation (power) in Python?",
            "options": ["A) ^", "B) *", "C) **", "D) //"],
            "answer": "C"
        },
        {
            "question": "Which built-in function is used to take user input in Python?",
            "options": ["A) scan()", "B) read()", "C) get()", "D) input()"],
            "answer": "D"
        }
    ]

    score = 0
    total = len(questions)

    print("\n=== Python Quiz Game ===")
    print(f"Answer all {total} questions by typing A, B, C, or D.\n")

    for index, item in enumerate(questions, start=1):
        print(f"Q{index}. {item['question']}")
        for option in item["options"]:
            print(f"   {option}")

        while True:
            user_choice = input("Your answer (A/B/C/D): ").strip().upper()
            if user_choice in ["A", "B", "C", "D"]:
                break
            print("Invalid input! Please enter A, B, C, or D.")

        if user_choice == item["answer"]:
            print("Correct!\n")
            score += 1
        else:
            print(f"Wrong! The correct answer was {item['answer']}.\n")

    percentage = (score / total) * 100
    print("=== Quiz Finished ===")
    print(f"Your Score: {score}/{total} ({percentage:.1f}%)")

    if percentage >= 80:
        print("Great job! You really know your Python basics.")
    elif percentage >= 50:
        print("Nice effort! Keep practicing to level up.")
    else:
        print("Good start! Review the basics and try again.")


if __name__ == "__main__":
    run_quiz()
