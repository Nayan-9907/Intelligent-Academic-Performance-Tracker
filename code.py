print("MODULE 2: DATA VALIDATION")

name = input("Enter student name: ")
n = int(input("Enter number of subjects: "))

subjects = []
marks = []

if name.strip() == "" or n <= 0:
    print("Invalid student details")

else:
    for i in range(n):
        subject = input("Enter subject name: ")
        mark = float(input("Enter marks out of 100: "))

        if subject.strip() == "":
            print("Invalid subject name")
        elif mark < 0 or mark > 100:
            print("Invalid marks")
        else:
            subjects.append(subject)
            marks.append(mark)

    print("\nVALIDATION REPORT")
    print("Student:", name)
    print("Valid Subjects:", len(subjects))

    for i in range(len(subjects)):
        print(subjects[i], ":", marks[i], "marks")

    print("Data Validation Completed!")