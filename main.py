

def get_student_details():
    print("\n===== STUDENT DETAILS =====")

    name = input("Enter student name: ")
    roll_no = input("Enter roll number: ")

    return name, roll_no


def calculate_grade(marks):
    if marks >= 90:
        return "A+"
    elif marks >= 80:
        return "A"
    elif marks >= 70:
        return "B"
    elif marks >= 60:
        return "C"
    elif marks >= 50:
        return "D"
    elif marks >= 40:
        return "E"
    else:
        return "F"


def check_attendance(attendance):
    if attendance >= 75:
        return "Eligible"
    else:
        return "Low Attendance"


def get_subject_details():
    subjects = []

    print("\n===== SUBJECT DETAILS =====")

    number = int(input("Enter number of subjects: "))

    for i in range(number):
        print("\nSubject", i + 1)

        name = input("Enter subject name: ")

        marks = float(input("Enter marks out of 100: "))
        while marks < 0 or marks > 100:
            print("Invalid marks! Enter marks between 0 and 100.")
            marks = float(input("Enter marks out of 100: "))

        attendance = float(input("Enter attendance percentage: "))
        while attendance < 0 or attendance > 100:
            print("Invalid attendance! Enter value between 0 and 100.")
            attendance = float(input("Enter attendance percentage: "))

        subject = {
            "name": name,
            "marks": marks,
            "attendance": attendance
        }

        subjects.append(subject)

    return subjects


def display_report(name, roll_no, subjects):
    print("\n")
    print("=" * 55)
    print("       ACADEMIC PERFORMANCE REPORT")
    print("=" * 55)

    print("Student Name :", name)
    print("Roll Number  :", roll_no)

    print("\nSubject-wise Performance")
    print("-" * 55)
    print(f"{'Subject':<20}{'Marks':<10}{'Grade':<10}{'Attendance'}")
    print("-" * 55)

    total_marks = 0

    for subject in subjects:
        grade = calculate_grade(subject["marks"])
        attendance_status = check_attendance(subject["attendance"])

        print(
            f"{subject['name']:<20}"
            f"{subject['marks']:<10}"
            f"{grade:<10}"
            f"{subject['attendance']}%"
        )

        total_marks += subject["marks"]

    overall_percentage = total_marks / len(subjects)
    overall_grade = calculate_grade(overall_percentage)

    print("-" * 55)
    print("Overall Percentage :", round(overall_percentage, 2), "%")
    print("Overall Grade      :", overall_grade)

    print("\nAttendance Status")
    print("-" * 55)

    for subject in subjects:
        status = check_attendance(subject["attendance"])
        print(subject["name"], ":", status)

    print("=" * 55)
    print("Report generated successfully!")
    print("=" * 55)


def main():
    print("=" * 55)
    print(" INTELLIGENT ACADEMIC PERFORMANCE TRACKER")
    print("=" * 55)

    name, roll_no = get_student_details()

    subjects = get_subject_details()

    display_report(name, roll_no, subjects)


main()