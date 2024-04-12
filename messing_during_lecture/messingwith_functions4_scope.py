# Variable Scope
# author: atacan

# don't use global variables

x = 999 # global x
# don't do this - use the variable defined outside of the function

def fun():
    print(x)
# instead 

def fun(num):
    print(num)

fun(x)

def fun2(x):
    print(f"in fun2 x {x}")
    x = 21 # inside the function x - scope variable
    print(f"in fun2 x {x}")

fun2(x)
print(f"after fun2 x is {x}")