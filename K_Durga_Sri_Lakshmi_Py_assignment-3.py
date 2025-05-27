import datetime

def log_activity(func):
    def wrapper(*args, **kargs):
        print(f"\n LOG Function '{func.__name__}' called at {datetime.datetime.now()}")
        result = func(*args, **kargs)
        print(f" LOG Function '{func.__name__}' finished\n")
        return result
    return wrapper

students = []


@log_activity
def add_student(*args, **kargs):
    student = {}
    student['name'] = kargs.get('name')
    student['id'] = kargs.get('id')
    student['grades'] = list(args)  
    students.append(student)
    print(f"Student '{student['name']}' added successfully.")


@log_activity
def display_students():
    if not students:
        print("No student records to display.")
        return
    
    for i in students:
        print(f"\nStudent ID: {i['id']}")
        print(f"Name: {i['name']}")
        print(f"Grades: {i['grades']}")

        if i['grades']:
            avg = sum(i['grades']) / len(i['grades'])
            print(f"Average: {avg:.2f}")
            if avg >= 90:
                print("Result   : Outstanding")
            elif avg >= 75:
                print("Result   : Good")
            elif avg >= 50:
                print("Result   : Pass")
            else:
                print("Result   : Fail")
        else:
            print("No grade.")


add_student(85, 90, 78, name="Alice", id="S001")
add_student(60, 55, 70, name="Bob", id="S002")
add_student(45, 40, 35, name="Charlie", id="S003")

display_students()
