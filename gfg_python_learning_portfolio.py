"""
GeeksforGeeks-Aligned Python Learning Portfolio
Author: Madaka Sai Pragna

Topics:
1. Beginner Python tutorials
2. Student performance data analysis
3. Data Structures and Algorithms
4. Practice questions and explanations

Run: python gfg_python_learning_portfolio.py
"""

import csv
import math
from collections import Counter
from io import StringIO


# =========================================================
# PROJECT 1: PYTHON LEARNING RESOURCES
# =========================================================

def calculate_percentage(obtained, maximum):
    """Calculate percentage with basic input validation."""
    if maximum <= 0:
        raise ValueError("Maximum marks must be greater than zero.")

    if obtained < 0 or obtained > maximum:
        raise ValueError("Obtained marks must be within valid limits.")

    return (obtained / maximum) * 100


def count_topics(topics):
    """Count the frequency of each topic."""
    return dict(Counter(topics))


def word_frequency(sentence):
    """Count words without considering letter case."""
    words = sentence.lower().split()
    return dict(Counter(words))


def demonstrate_python_basics():
    """Demonstrate lists, dictionaries, loops and functions."""
    scores = [78, 91, 84, 67, 95]

    print("\n--- Python Basics ---")
    print("Scores:", scores)
    print("Average:", round(sum(scores) / len(scores), 2))
    print("Highest score:", max(scores))
    print("Scores above or equal to 80:",
          sum(score >= 80 for score in scores))

    topics = ["Python", "SQL", "Python", "Git", "SQL", "Python"]
    print("Topic frequencies:", count_topics(topics))

    print("Percentage:", calculate_percentage(42, 50))


# =========================================================
# PROJECT 2: STUDENT PERFORMANCE DATA ANALYSIS
# =========================================================

SAMPLE_DATA = """student_id,study_hours,attendance_pct,python_score
S001,2.0,72,61
S002,4.5,90,84
S003,1.5,65,55
S004,5.0,95,92
S005,3.0,80,73
S006,6.0,98,96
S007,2.5,75,68
S008,4.0,88,81
S009,1.0,60,48
S010,3.5,85,78
S011,5.5,93,90
S012,2.0,70,59
"""


def load_student_data():
    """Load a small synthetic dataset from CSV text."""
    return list(csv.DictReader(StringIO(SAMPLE_DATA)))


def mean(values):
    """Return the arithmetic mean."""
    if not values:
        raise ValueError("Cannot calculate mean of empty data.")

    return sum(values) / len(values)


def correlation(xs, ys):
    """Calculate Pearson correlation without external libraries."""
    if len(xs) != len(ys) or len(xs) < 2:
        raise ValueError("Provide equal-length datasets with 2+ values.")

    x_mean = mean(xs)
    y_mean = mean(ys)

    numerator = sum(
        (x - x_mean) * (y - y_mean)
        for x, y in zip(xs, ys)
    )

    x_variance = sum((x - x_mean) ** 2 for x in xs)
    y_variance = sum((y - y_mean) ** 2 for y in ys)

    denominator = math.sqrt(x_variance * y_variance)

    if denominator == 0:
        raise ValueError("Correlation is undefined for constant data.")

    return numerator / denominator


def analyze_student_performance():
    """Summarize synthetic student data and explore relationships."""
    records = load_student_data()

    study_hours = [float(row["study_hours"]) for row in records]
    attendance = [float(row["attendance_pct"]) for row in records]
    scores = [float(row["python_score"]) for row in records]

    print("\n--- Student Performance Analysis ---")
    print("Dataset type: Synthetic demonstration data")
    print("Number of students:", len(records))
    print("Average study hours:", round(mean(study_hours), 2))
    print("Average attendance:", round(mean(attendance), 2), "%")
    print("Average Python score:", round(mean(scores), 2))

    print("\nStudents scoring below 60:")
    low_scores = [
        row for row in records
        if float(row["python_score"]) < 60
    ]

    if low_scores:
        for row in low_scores:
            print(row["student_id"], row["python_score"])
    else:
        print("None")

    result = correlation(study_hours, scores)
    print("\nCorrelation between study hours and scores:",
          round(result, 3))

    print(
        "Interpretation: Correlation describes an association in this "
        "synthetic dataset; it does not establish causation."
    )


# =========================================================
# PROJECT 3: DATA STRUCTURES AND ALGORITHMS
# =========================================================

def contains_duplicate(values):
    """
    Check whether a list contains duplicate values.

    Time: O(n) average
    Space: O(n)
    """
    seen = set()

    for value in values:
        if value in seen:
            return True
        seen.add(value)

    return False


def two_sum(values, target):
    """
    Return indices of two values that add to target.

    Returns None if no solution exists.
    Time: O(n) average
    Space: O(n)
    """
    seen = {}

    for index, value in enumerate(values):
        required = target - value

        if required in seen:
            return [seen[required], index]

        seen[value] = index

    return None


def binary_search(sorted_values, target):
    """
    Search a sorted list using binary search.

    Returns the index or -1 if not found.
    Time: O(log n)
    Space: O(1)
    """
    left = 0
    right = len(sorted_values) - 1

    while left <= right:
        middle = (left + right) // 2

        if sorted_values[middle] == target:
            return middle

        if sorted_values[middle] < target:
            left = middle + 1
        else:
            right = middle - 1

    return -1


def demonstrate_dsa():
    """Run sample DSA examples."""
    print("\n--- Data Structures and Algorithms ---")

    numbers = [2, 7, 11, 15]
    target = 9

    print("Numbers:", numbers)
    print("Two Sum target:", target)
    print("Matching indices:", two_sum(numbers, target))

    print("Contains duplicate:",
          contains_duplicate([1, 2, 3, 1]))

    sorted_numbers = [1, 3, 5, 7, 9]
    print("Binary search result:",
          binary_search(sorted_numbers, 7))


# =========================================================
# PROJECT 4: SELF-TESTS AND EDGE CASES
# =========================================================

def run_tests():
    """Run built-in assertions for key functions."""
    print("\n--- Running Tests ---")

    assert calculate_percentage(40, 50) == 80
    assert count_topics(["Python", "Python", "SQL"]) == {
        "Python": 2,
        "SQL": 1
    }
    assert word_frequency("Python python SQL") == {
        "python": 2,
        "sql": 1
    }

    assert contains_duplicate([1, 2, 1]) is True
    assert contains_duplicate([1, 2, 3]) is False
    assert contains_duplicate([]) is False

    assert two_sum([2, 7, 11, 15], 9) == [0, 1]
    assert two_sum([1, 2, 3], 10) is None

    assert binary_search([1, 3, 5, 7], 5) == 2
    assert binary_search([1, 3, 5, 7], 4) == -1
    assert binary_search([], 1) == -1

    assert round(correlation([1, 2, 3], [2, 4, 6]), 5) == 1.0

    try:
        calculate_percentage(10, 0)
    except ValueError:
        pass
    else:
        raise AssertionError("Expected invalid maximum to raise ValueError")

    print("All tests passed!")


# =========================================================
# PRACTICE QUESTIONS
# =========================================================

def show_practice_questions():
    """Display practice questions for learners."""
    questions = [
        "Find the second-largest distinct number in a list.",
        "Count word frequencies while ignoring punctuation.",
        "Explain the difference between lists and dictionaries.",
        "Compare linear search and binary search.",
        "Explain the time complexity of the Two Sum solution.",
        "Why does correlation not prove causation?",
    ]

    print("\n--- Practice Questions ---")

    for number, question in enumerate(questions, start=1):
        print(f"{number}. {question}")


# =========================================================
# MAIN PROGRAM
# =========================================================

def main():
    print("=" * 55)
    print("PYTHON LEARNING AND DSA PORTFOLIO")
    print("Python | Data Analysis | DSA | Educational Examples")
    print("=" * 55)

    demonstrate_python_basics()
    analyze_student_performance()
    demonstrate_dsa()
    run_tests()
    show_practice_questions()

    print("\nPortfolio demonstration completed successfully.")


if __name__ == "__main__":
    main()
