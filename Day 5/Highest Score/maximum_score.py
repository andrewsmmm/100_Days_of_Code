# Here is my solution to the problem:
student_scores = [8, 65, 89, 86, 55, 91, 64, 89]
max_score = 0
for num in student_scores:
    if num > max_score:
        max_score = num
print(max_score)