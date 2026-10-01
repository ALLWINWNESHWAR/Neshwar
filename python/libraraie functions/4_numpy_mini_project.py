#Lesson 19 — NumPy Mini Project

#Student Performance Analysis System using the NumPy

import numpy as np

marks = np.array([
    [85, 90, 78],
    [72, 88, 95],
    [60, 75, 70],
    [92, 96, 89],
    [55, 65, 58]
])


#Q1 — Overall average
avg = np.mean(marks)
print(avg)

#Q2 — Subject-wise average
avg_sub = np.mean(marks, axis=0)
print(avg_sub)

#Q3 — Student-wise average
avg_std = np.mean(marks, axis = 1)
print(avg_std)

#Q4 — Highest mark
high = np.max(marks)
print("max mark: ", high)

#Q5 — Lowest mark
low = np.min(marks)
print(low)

#Q6 — Students with average ≥ 80
avg = np.mean(marks, axis=1)
abov = avg[avg >= 80]
print(abov)

#Q7 — Pass/Fail
print("P/F:", np.where(marks >=60, "Pass", "Fail"))

result = np.where(avg_std >= 60, "Pass", "Fail")
print("p/f: ", result)

#Q8 — Find the top student
top_student = np.argmax(avg_std)
print("Top student index:", top_student)
print("Top student average:", avg_std[top_student])


