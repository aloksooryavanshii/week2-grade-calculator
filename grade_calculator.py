# ==========================================
# Name: Alok Kumar
# Project: Student Grade Calculator
# Week 2 - Python Internship
# ==========================================

def calculate_grade(avg):
    if avg >= 90:
        return "A", "Excellent!"
    elif avg >= 80:
        return "B", "Very Good!"
    elif avg >= 70:
        return "C", "Good"
    elif avg >= 60:
        return "D", "Needs Improvement"
    else:
        return "F", "Failed"


def get_marks(subject):
    while True:
        try:
            marks = float(input(f"{subject}: "))
            if 0 <= marks <= 100:
                return marks
            else:
                print("Marks should be between 0 and 100.")
        except ValueError:
            print("Invalid input.")


results = []

while True:
    try:
        total_students = int(input("Enter number of students: "))
        if total_students > 0:
            break
        print("Enter a positive number.")
    except ValueError:
        print("Invalid input.")

for i in range(total_students):

    print(f"\nStudent {i+1}")

    name = input("Student Name: ").strip()

    while name == "":
        name = input("Student Name: ").strip()

    math = get_marks("Math")
    science = get_marks("Science")
    english = get_marks("English")

    average = (math + science + english) / 3

    grade, comment = calculate_grade(average)

    results.append({
        "name": name,
        "average": average,
        "grade": grade,
        "comment": comment
    })

print("\n===============================")
print("RESULT SUMMARY")
print("===============================")

for student in results:

    print(
        f"{student['name']} | "
        f"{student['average']:.2f} | "
        f"{student['grade']} | "
        f"{student['comment']}"
    )

averages = [x["average"] for x in results]

print("\nClass Statistics")

print("Class Average :", round(sum(averages)/len(averages),2))

print("Highest :", max(averages))

print("Lowest :", min(averages))

search = input("\nSearch Student Name: ")

found = False

for student in results:

    if student["name"].lower() == search.lower():

        print(student)

        found = True

if not found:

    print("Student Not Found")

with open("results_sample.txt","w") as file:

    for student in results:

        file.write(
            f"{student['name']} | "
            f"{student['average']:.2f} | "
            f"{student['grade']} | "
            f"{student['comment']}\n"
        )

print("\nResults Saved Successfully!")