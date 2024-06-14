import pandas as pd

# Given data
students = ['Alice', 'Bob', 'Charlie', 'David', 'Eve', 'Frank', 'Grace', 'Hannah', 'Ivy', 'Jack']
exam_scores = [92, 88, 76, 94, 82, 90, 85, 89, 78, 91]

# Creating a Pandas Series
exam_scores_series = pd.Series(exam_scores, index=students, name='Exam Scores')

# Displaying the Series
print(exam_scores_series)
