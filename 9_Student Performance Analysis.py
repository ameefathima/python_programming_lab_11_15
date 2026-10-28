def total(marks):
    return sum(marks)


def average(marks):
    return sum(marks) / len(marks)


def highest(marks):
    return max(marks)


def lowest(marks):
    return min(marks)


def grade(avg):
    if avg >= 90:
        return "A+"
    elif avg >= 80:
        return "A"
    elif avg >= 70:
        return "B+"
    elif avg >= 60:
        return "B"
    elif avg >= 50:
        return "C"
    else:
        return "F"


students = []

n = int(input("Enter number of students: "))

for i in range(n):
    name = input("\nEnter student name: ")

    marks = []
    for j in range(3):
        mark = int(input("Enter mark: "))
        marks.append(mark)

    total_marks = total(marks)
    avg = average(marks)

    student = {
        "name": name,
        "marks": marks,
        "total": total_marks,
        "average": avg,
        "highest": highest(marks),
        "lowest": lowest(marks),
        "grade": grade(avg)
    }

    students.append(student)


students.sort(key=lambda x: x["total"], reverse=True)

print("\nStudent Performance")

for student in students:
    print("\nName:", student["name"])
    print("Total:", student["total"])
    print("Average:", student["average"])
    print("Highest:", student["highest"])
    print("Lowest:", student["lowest"])
    print("Grade:", student["grade"])