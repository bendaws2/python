def new_student(name, age, grades=None):
    if grades is None:
        grades = []
    return {
        'name': name,
        'age': age,
        'grades': grades
    }

def add_grade(student, assignment_name="Unnamed assignment", assignment_grade=100):
    student['grades'].append([assignment_name, assignment_grade])