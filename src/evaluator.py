# evaluator.py
# This file contains the core evaluation logic

def evaluate_candidate(answer_text):
    scores = {
        "technical_clarity": 0,
        "problem_solving": 0,
        "communication": 0
    }

    feedback = []

    # Technical clarity (length-based)
    word_count = len(answer_text.split())
    if word_count >= 80:
        scores["technical_clarity"] = 5
        feedback.append("Answer is detailed and technically clear.")
    elif word_count >= 40:
        scores["technical_clarity"] = 3
        feedback.append("Answer has basic technical clarity.")
    else:
        scores["technical_clarity"] = 1
        feedback.append("Answer lacks sufficient technical detail.")

    # Problem solving
    keywords = ["approach", "steps", "solution", "logic", "design"]
    hits = sum(1 for k in keywords if k in answer_text.lower())
    if hits >= 3:
        scores["problem_solving"] = 5
        feedback.append("Strong problem-solving approach.")
    elif hits >= 1:
        scores["problem_solving"] = 3
        feedback.append("Some problem-solving intent shown.")
    else:
        scores["problem_solving"] = 1
        feedback.append("Problem-solving approach not clear.")

    # Communication
    if "." in answer_text and "," in answer_text:
        scores["communication"] = 5
        feedback.append("Communication is clear and structured.")
    else:
        scores["communication"] = 2
        feedback.append("Communication can be improved.")

    total_score = sum(scores.values())

    return {
        "scores": scores,
        "total_score": total_score,
        "feedback": feedback
    }