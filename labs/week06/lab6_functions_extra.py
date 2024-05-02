# funtions_extra.py
# this is a demonstration of Variables as a type of function
# author: atacan

# defining the functions 'fun1' and 'fun2'
def fun1():
    print("this is fun1")
def fun2():
    print("this is fun2")

# assigning them to a variable
whichFun = fun1
# when we call the variable, the function will be executed
whichFun()
whichFun = fun2
whichFun()