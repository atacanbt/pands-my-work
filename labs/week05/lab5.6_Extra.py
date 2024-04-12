# extra.py
# this program reads students name, modules they are taking and the grades until the user enters blank input
# I couldn't figure out to prompt more than one sutudents name so I used AI to write this

students = []

while True:
    student = {}
    student["name"] = input("Enter student's name (or leave blank to stop): ")
    if not student["name"]:
        break
    
    student["modules"] = []
    while True:
        module_name = input("Enter module name (or leave blank to stop): ")
        if not module_name:
            break
        module_grade = int(input("Enter grade for {} module: ".format(module_name)))
        student["modules"].append({"course_name": module_name, "grade": module_grade})
    
    students.append(student)

for student in students:
    print("Student: {}".format(student["name"]))
    for module in student["modules"]:
        print("\t{} \t{}".format(module["course_name"], module["grade"]))

