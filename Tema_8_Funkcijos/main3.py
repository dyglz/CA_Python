# Task 3: Nested List and Dictionary Manipulation with Functions

# Write a function that takes a list of dictionaries, where each dictionary represents 
# a person with their name and a list of their test scores. 
# The function should:
# Return the average score for each person.
# Create and return a new list of dictionaries with each dictionary containing 
# the person's name and their highest test score.
 
from typing import Dict, List


students = [
  {"name": "Alice", "scores": [85, 90, 78]},
  {"name": "Bob", "scores": [88, 92, 95]},
  {"name": "Charlie", "scores": [78, 80, 72]}
]

def process_scores(students: list[Dict[str, List[int]]]) -> tuple[List[float], List[Dict[str, int]]]:
    average_scores: List[float] = []
    for student in students:
        average_score = sum(student["scores"]) / len(student["scores"])
        average_scores.append(float(f"{average_score:.2f}"))

    highest_scores: List[Dict[str, int]] = []
    for student in students:
        highest_score = max(student["scores"])
        highest_scores.append({"name": student["name"], "highest_score": highest_score})

    return average_scores, highest_scores

print(process_scores(students))


