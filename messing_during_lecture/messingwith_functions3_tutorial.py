# read in two numbers and multiple them
# author: atacan buyuktalas
'''
num1 = False

while (num1 == False):
    try:
        num1 = int(input("enter a number: "))
    except ValueError:
        print ("That was not a number ", end="")

num2 = False

while (num2 == False):
    try:
        num2 = int(input("enter a another number: "))
    except ValueError:
        print ("That was not a number ", end="")

answer = num1 * num2

print(f"answer is {answer}")
'''
# this way we are genarating 2 numbers with separately, it's not an efficient way if the number of input increases

# defininf the function readNum here with a default messaging "Enter a number: "
def readNum(message = "Enter a number: "):
    # In this case, num is initially set to False, which serves as a flag indicating 
    # whether a valid number has been obtained from the user input yet.

    # The purpose of setting num to False here is to establish a condition for the while loop that follows. 
    # The loop is set up to continue until num becomes a non-false value, 
    # indicating that a valid number has been successfully obtained from the user.

    # So, in summary, step 2 initializes the num variable to False as a starting point before entering the loop, 
    # where it will be reassigned based on user input until a valid number is obtained.
    num = False # num is falsy
    # start of the while loop until num becomes truthy value
    while not num:
        # try block is starts here if there is a ValueError, it executes the block again
        try:
            # promting an input and converts it to integer
            num = int(input(message))
        except ValueError:
            # The end="" argument is used to prevent the print function from adding a newline character at the end of the message.
            print ("That was not a number ", end="")
    # returns the variable 'num' once it has been successfully assigned to a numeric value
    return num

num1 = readNum()
num2 = readNum("Enter a second number")

answer = num1 * num2
print(f"Answer is {answer}")