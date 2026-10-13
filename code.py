import pandas as pd
import numpy as np

print("====================================")
print("   ACADEMIC PERFORMANCE TRACKER")
print("====================================")

name = input("Enter student name: ")

total_classes = int(input("Enter total number of classes: "))
attended_classes = int(input("Enter classes attended: "))

if total_classes <= 0 or attended_classes < 0 or attended_classes > total_classes:
    print("Invalid class details. Please enter valid numbers.")

else:
    attendance = (attended_classes / total_classes) * 100

    n = int(input("How many subjects do you have? "))

    if n <= 0:
        print("Please enter at least one subject.")

    else:
        subjects = []
        marks = []

        for i in range(n):
            print("\nSubject", i + 1)

            subject = input("Enter subject name: ")
            mark = float(input("Enter marks out of 100: "))

            subjects.append(subject)
            marks.append(mark)

        data = {
            "Subject": subjects,
            "Marks": marks
        }

        df = pd.DataFrame(data)

        total = np.sum(marks)
        average = np.mean(marks)
        highest = np.max(marks)
        lowest = np.min(marks)

        if average >= 90:
            grade = "A+"
        elif average >= 80:
            grade = "A"
        elif average >= 70:
            grade = "B"
        elif average >= 60:
            grade = "C"
        elif average >= 40:
            grade = "D"
        else:
            grade = "F"

        print("\n====================================")
        print("           STUDENT REPORT")
        print("====================================")

        print("Student Name:", name)

        print("\nSubject-wise Marks:")
        print(df.to_string(index=False))

        print("\nTotal Marks:", total, "/", n * 100)
        print("Average Marks:", round(average, 2))
        print("Percentage:", round(average, 2), "%")
        print("Grade:", grade)
        print("Estimated GPA:", round(average / 10, 2))

        print("\nClasses Attended:", attended_classes, "/", total_classes)
        print("Attendance Percentage:", round(attendance, 2), "%")

        if attendance < 75:
            print("Attendance Status: FAIL - Detention")
        elif attendance < 80:
            print("Attendance Status: Low")
        elif attendance < 85:
            print("Attendance Status: Average")
        elif attendance < 90:
            print("Attendance Status: Good")
        else:
            print("Attendance Status: Excellent")

        max_index = df["Marks"].idxmax()
        min_index = df["Marks"].idxmin()

        print("\n----- SUBJECT ANALYSIS -----")

        print("Highest Marks:", highest)
        print("Lowest Marks:", lowest)

        print("\nStrongest Subject:")
        print("Subject:", df.loc[max_index, "Subject"])
        print("Marks:", highest)

        print("\nSubject Needing Improvement:")
        print("Subject:", df.loc[min_index, "Subject"])
        print("Marks:", lowest)

        print("\n----- PERFORMANCE ANALYSIS -----")
        print(df.describe().round(2))

        df.to_csv("student_marks.csv", index=False)

        print("\nStudent marks saved to student_marks.csv")

        print("\n====================================")
        print("Thank you for using the tracker!")
        print("====================================")
