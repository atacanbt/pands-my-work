# student_grade.py
# this program stores student courses and grades
# author: atacan

student = {
    "name" : "Marry",
    "modules" : [
        {
            "course_name" : "Programming",
            "grade" : 45
        },
        {
            "course_name" : "History",
            "grade" : 99
        }
    ]
}
print ("Student: {}".format(student["name"]))
for module in student["modules"]:
    print ("\t {} \t {}".format(module["course_name"], module["grade"]))
