# funtions_extra.py
# this program is another way of lab6.2_functions - this is with variables as a function
# author: atacan

def displayMenu():
    print("What would you like to do?")
    print("\t(a) Add new student")
    print("\t(v) View students")
    print("\t(q) Quit")
    choice = input("Type one letter (a/v/q): ").strip()
    return choice

def doAdd(students):
    print("do add")
def doView(students):
    print("do view")
def doNothing(dumby):
    pass

# the dict that maps a letter to a function
choiceMap = {
    'a': doAdd,
    'v': doView,
    'q': doNothing # this is a valid choice
}

students = []
choice = displayMenu()
while (choice != 'q'):
    if choice in choiceMap:
        # run the function
        choiceMap[choice](students)
    else: # used for just in case if they submit something invalid
        print("\n\nPlease select either a,v or q: ")
    
    choice = displayMenu()