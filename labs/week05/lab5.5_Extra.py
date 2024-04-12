# extra.py
# this program reads students name, modules they are taking and the grades until the user enters blank input
# author: atacan buyuktalas


student = {}
# student's name and her modules and grades will be stored in this dictionary 

student["name"] = input("Enter student's name: ")
# here we prompt user the enter her name and store it in student{} under the 'name' key

modules = []
# modules name and grades that prompted from user will be stored in this list

while True:
    modules_name = input("Enter module name (or leave blank to stop): ")
    if not modules_name:
        break
# here, the program prompts user to enter modules name until they enter blank input
# while True: is an indefinite loop, 'if not' command checks if modules_name variable is empty
    # in python, empty string always evaluates False in boolean context
    # if prompt returns with empty string, the loop will be terminated

    modules_grade = int(input("Enter grade for {} module: ".format(modules_name)))
# here the program prompts user to enter grade for the respective modules
    
    modules.append({"course_name": modules_name, "grades": modules_grade})
# here, the program crates a dictionary representing modules information with keys "course_name" and "grades"
# and it will be appended into modules[]
# each iteration of the loop adds a new module information into the module[]
    
student["modules"] = modules
# modules[] list will be assigned to "modules" key in student{}, so student{} will store both student's name and modules information

print('Student: {}'.format(student["name"]))
for module in student["modules"]:
    print("\t{} \t{}".format(module["course_name"], module["grades"]))
# to print out each module prompted, 'for' loop is used