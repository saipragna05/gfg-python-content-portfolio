"""
Python Coding Practice and Quiz System
Author: Madaka Sai Pragna

A beginner-friendly quiz tool for Python and DSA learners.
Concepts: Functions, dictionaries, lists, loops, scoring,
input validation, and explanations.
"""

QUESTIONS = [
    {
        "question": "Which data structure stores key-value pairs?",
        "options": ["A. List", "B. Dictionary", "C. Tuple", "D. Set"],
        "answer": "B",
        "explanation": "A dictionary stores data as key-value pairs."
    },
    {
        "question": "What is the time complexity of binary search?",
        "options": ["A. O(n)", "B. O(n^2)", "C. O(log n)", "D. O(1)"],
        "answer": "C",
        "explanation": "Binary search halves the search space each step."
    },
    {
        "question": "Which keyword defines a function in Python?",
        "options": ["A. function", "B. define", "C. fun", "D. def"],
        "answer": "D",
        "explanation": "Python uses the def keyword to define functions."
    },
    {
        "question": "Which collection does not allow duplicate values?",
        "options": ["A. Set", "B. List", "C. Tuple", "D. String"],
        "answer": "A",
        "explanation": "A set stores unique elements."
    },
    {
        "question": "What does len([10, 20, 30]) return?",
        "options": ["A. 2", "B. 3", "C. 10", "D. 60"],
        "answer": "B",
        "explanation": "The list contains three elements."
    },
    {
        "question": "Which Python structure is best for FIFO processing?",
        "options": ["A. Stack", "B. Queue", "C. Set", "D. Tree"],
        "answer": "B",
        "explanation": "A queue follows First In, First Out (FIFO)."
    },
    {
        "question": "What does a stack follow?",
        "options": [
            "A. FIFO",
            "B. Random order",
            "C. LIFO",
            "D. Sorted order"
        ],
        "answer": "C",
        "explanation": "A stack follows Last In, First Out (LIFO)."
    },
    {
        "question": "Which method adds an item to the end of a list?",
        "options": [
            "A. insert_end()",
            "B. append()",
            "C. add_last()",
            "D. push_back()"
        ],
        "answer": "B",
        "explanation": "The append() method adds an item to a list."
    },
    {
        "question": "What is the result of 7 // 2 in Python?",
        "options": ["A. 3.5", "B. 4", "C. 3", "D. 1"],
        "answer": "C",
        "explanation": "The // operator performs floor division."
    },
    {
        "question": "Which algorithm requires sorted data for standard binary search?",
        "options": [
            "A. Linear search",
            "B. Binary search",
            "C. Counting",
            "D. Sequential printing"
        ],
        "answer": "B",
        "explanation": "Binary search relies on the data being sorted."
    }
]


def display_question(question, number, total):
    """Display one question and its options."""
    print(f"\nQuestion {number}/{total}")
    print(question["question"])

    for option in question["options"]:
        print(option)


def get_answer():
    """Read and validate a multiple-choice answer."""
    while True:
        answer = input("Your answer (A/B/C/D): ").strip().upper()

        if answer in {"A", "B", "C", "D"}:
            return answer

        print("Invalid input. Please enter A, B, C, or D.")


def run_quiz():
    """Run the quiz and show explanations after each answer."""
    score = 0
    total = len(QUESTIONS)

    print("=" * 45)
    print("PYTHON CODING PRACTICE & DSA QUIZ")
    print("=" * 45)
    print(f"Total questions: {total}")
    print("Answer each question to test your knowledge.")

    for number, question in enumerate(QUESTIONS, start=1):
        display_question(question, number, total)
        answer = get_answer()

        if answer == question["answer"]:
            print("Correct!")
            score += 1
        else:
            print(f"Incorrect. Correct answer: {question['answer']}")

        print("Explanation:", question["explanation"])

    percentage = (score / total) * 100

    print("\n" + "=" * 45)
    print("QUIZ RESULTS")
    print("=" * 45)
    print(f"Score: {score}/{total}")
    print(f"Percentage: {percentage:.1f}%")

    if percentage >= 80:
        print("Excellent work! Keep practising.")
    elif percentage >= 50:
        print("Good effort! Review the explanations and retry.")
    else:
        print("Keep learning. Practice the fundamentals and try again.")


def main():
    """Start the application."""
    while True:
        run_quiz()

        retry = input("\nWould you like to retry? (yes/no): ")
        if retry.strip().lower() not in {"yes", "y"}:
            print("Thanks for practising. Keep coding!")
            break


if __name__ == "__main__":
    main()
