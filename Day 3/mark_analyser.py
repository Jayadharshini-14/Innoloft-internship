import numpy as np

# Create a NumPy array of 10 student marks
marks = np.array([85, 67, 45, 90, 72, 38, 55, 61, 49, 80])

# Calculate statistics
mean_marks = np.mean(marks)
highest = np.max(marks)
lowest = np.min(marks)
std_dev = np.std(marks)

# Count students who passed (marks >= 50)
passed = marks[marks >= 50]
pass_count = len(passed)

# Print summary report
print("===== NumPy Marks Analyser =====")
print("Marks:", marks)
print("Mean Marks:", mean_marks)
print("Highest Mark:", highest)
print("Lowest Mark:", lowest)
print("Standard Deviation:", round(std_dev, 2))
print("Students Passed (>=50):", pass_count)