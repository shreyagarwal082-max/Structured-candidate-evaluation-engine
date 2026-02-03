# app.py
from src.evaluator import evaluate_candidate

sample_answer = """
I would first understand the problem clearly and break it down into steps.
My approach would involve designing a clean solution, considering edge cases,
and then implementing the logic in a structured way.
"""

result = evaluate_candidate(sample_answer)

print("Evaluation Result:")
print(result)
