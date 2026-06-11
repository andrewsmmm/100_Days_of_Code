# student_scores = [150, 142, 185, 120, 171, 184, 149, 24, 59, 68, 199, 78, 65, 89, 86, 55, 91, 64, 89]
# print(range(1, 10))

# Here is my solution to the problem:
student_scores2 = [8, 65, 89, 86, 55, 91, 64, 89]
max_score = 0
for num in student_scores2:
    if num > max_score:
        max_score = num
print(max_score)