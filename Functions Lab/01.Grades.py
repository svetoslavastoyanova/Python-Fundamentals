def grades(score):
    if 2.0 <= score < 3.0:
        return "Fail"
    if 3.0 <= score < 3.5:
        return "Poor"
    if 3.5 <= score < 4.5:
        return "Good"
    if 4.5 <= score < 5.5:
        return "Very good"
    if 5.50 <= score < 6.0:
        return "Excellent"


score = float(input())
print(grades(score))