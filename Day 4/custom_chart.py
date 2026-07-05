import pandas as pd
import matplotlib.pyplot as plt

# Load the dataset
df = pd.read_csv("Day 4/student_mat.csv")

# Calculate average G3 by study time
avg_grade = df.groupby("studytime")["G3"].mean()

# Overall mean grade
overall_mean = df["G3"].mean()

# Colors for each bar
colors = ["red", "blue", "green", "orange"]

# Create figure
plt.figure(figsize=(7, 5))

# Bar chart
plt.bar(avg_grade.index.astype(str), avg_grade.values,
        color=colors[:len(avg_grade)],
        label="Average G3")

# Horizontal dashed line
plt.axhline(y=overall_mean,
            color="black",
            linestyle="--",
            label=f"Overall Mean = {overall_mean:.2f}")

# Title and labels
plt.title("Average G3 Grade by Study Time")
plt.xlabel("Study Time")
plt.ylabel("Average G3 Grade")

# Legend
plt.legend()

# Save chart
plt.savefig("custom_styled_chart.png")

# Display chart
plt.show()

print("Chart saved as custom_styled_chart.png")