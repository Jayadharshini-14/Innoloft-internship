import pandas as pd
import matplotlib.pyplot as plt

# Load the dataset
df = pd.read_csv("Day 4/student_mat.csv")   # Use your file path if needed

# -------------------------------
# 1. Bar Chart - Average G3 by School
# -------------------------------
plt.figure(figsize=(6, 4))
df.groupby("school")["G3"].mean().plot(kind="bar")
plt.title("Average G3 Grade by School")
plt.xlabel("School")
plt.ylabel("Average G3")
plt.tight_layout()
plt.savefig("bar_chart.png")
plt.close()

# -------------------------------
# 2. Scatter Plot - G1 vs G3
# -------------------------------
plt.figure(figsize=(6, 4))
plt.scatter(df["G1"], df["G3"])
plt.title("G1 vs G3")
plt.xlabel("G1")
plt.ylabel("G3")
plt.tight_layout()
plt.savefig("scatter_plot.png")
plt.close()

# -------------------------------
# 3. Histogram - Age Distribution
# -------------------------------
plt.figure(figsize=(6, 4))
plt.hist(df["age"], bins=5)
plt.title("Age Distribution")
plt.xlabel("Age")
plt.ylabel("Number of Students")
plt.tight_layout()
plt.savefig("histogram.png")
plt.close()

# -------------------------------
# 4. Line Chart - Average G1, G2, G3
# -------------------------------
plt.figure(figsize=(6, 4))

avg_marks = [
    df["G1"].mean(),
    df["G2"].mean(),
    df["G3"].mean()
]

plt.plot(["G1", "G2", "G3"], avg_marks, marker="o")
plt.title("Average Grades Trend")
plt.xlabel("Exam")
plt.ylabel("Average Marks")
plt.tight_layout()
plt.savefig("line_chart.png")
plt.close()

print("All charts have been created and saved successfully!")