def get_student_marks():
    """
    Creates a dictionary of student marks, takes user input for a student's name,
    and displays their marks or a message if the student is not found.
    """
    student_marks = {
        "Alice": 85,
    }

    student_name = input("Enter the student's name: ")

    if student_name in student_marks:
        marks = student_marks[student_name]
        print(f"{student_name}'s marks: {marks}")
        print()
        print("if the student does not exist in the dictionary:")
        print()
        student_name = input("Enter the student's name: ")
        print(f"Student  not found.")

if __name__ == "__main__":
    get_student_marks()