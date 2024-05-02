


def doAdd(students):
    currentStudent = {}
    currentStudent["name"] = input("Enter name: ")
    currentStudent["modules"] = readModules()

    students.append(currentStudent)

def readModules():
    modules = []
    moduleName = input("\t Enter the first module name (blank to quit): ").strip()
    while moduleName != "":
        module = {}
        module["name"] = moduleName
        module["grade"] = int(input("\t\tEnter the grade: "))
        modules.append(module)
        moduleName = input("Enter the next module name (blank to quit): ").strip()

    return modules


