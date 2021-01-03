import matplotlib.pyplot as plot

plot.figure(figsize=(5,5))

labels = ["History", "Maths", "Literature", "History", "English", "Geography", "Biology", "Physics", "Bengali"]
marks = [40, 37, 29, 32, 41, 42, 42, 44, 31]

plot.pie(marks, labels=labels, autopct="%.1f%%", startangle=90)

plot.show()