# evaluator.py
# This file contains the core evaluation logic

def evaluate_candidate(answer_text):
    """
    Evaluates a candidate's written answer using simple rubric-based rules.
    Returns a structured score and explanation.
    """

    score = 0
    feedback = []

    # Rule 1: Length check (clarity indicator)
    word_count = len(answer_text.split())
    if word_count >= 80:
        score += 4
        feedback.append("Answer is detailed and well explained.")
    elif word_count >= 40:
        score += 2
        feedback.append("Answer has moderate explanation.")
    else:
        feedback.append("Answer is too short and lacks detail.")

    # Rule 2: Problem-solving keywords
    problem_keywords = ["approach", "steps", "solution", "logic", "design"]
    keyword_hits = sum(1 for word in problem_keywords if word in answer_text.lower())

    if keyword_hits >= 3:
        score += 4
        feedback.append("Good problem-solving structure detected.")
    elif keyword_hits >= 1:
        score += 2
        feedback.append("Some problem-solving intent is visible.")
    else:
        feedback.append("Problem-solving steps are not clear.")

    # Rule 3: Communication clarity
    if "." in answer_text and "," in answer_text:
        score += 2
        feedback.append("Communication is clear and structured.")
    else:
        feedback.append("Communication can be improved.")

    return {
        "total_score": score,
        "feedback": feedback
    }
    # TEMPORARY TEST (Day 1)
if __name__ == "__main__":
    test_answer = """
    This answer explains the approach and solution steps clearly.
    The logic and design are well structured.
    """
    
    result = evaluate_candidate(test_answer)
    print(result)
