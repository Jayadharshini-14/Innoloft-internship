import pandas as pd

# Load the CSV file
df = pd.read_csv("Day 3/student_mat.csv", sep=",")

# Average G3 grade by study time
avg_studytime = df.groupby("studytime")["G3"].mean()

# Average G3 grade by sex
avg_sex = df.groupby("sex")["G3"].mean()

# Top 5 students based on G3
top5 = df.nlargest(5, "G3")[["school", "sex", "studytime", "G3"]]

# Print Summary
print("===== Group & Compare Report =====")

print("\nAverage G3 Grade by Study Time:")
print(avg_studytime)

print("\nAverage G3 Grade by Sex:")
print(avg_sex)

print("\nTop 5 Students by G3:")
print(top5)