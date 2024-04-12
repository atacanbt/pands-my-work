# messingwith_functions2
# materials written druing the lecture
# author : atacan

print (1,2,3, end="\t", sep="") # sep and end's order doesn't matter end, sep or sep, end
print ("hi")

# unnamed arguments
def fun1(*args):
    print(type(args))
    for val in args:
        print(val)

fun1("a", "b", "c")

# keyword arguments
def fun2(**kwargs):
    print(type(kwargs))
    print(kwargs)
    #for val in kwargs:
    #    print(val)

fun2(name="joe", age=21, gender="M")

# sample code for average

# here we are defining the function called 'ave', *values is where all the arguments are packed
def ave(*values):
    # number_of_values is the length of ave (tuple)
    number_of_values = len(values)
    # sum - will be used to accumulate the sum of all the values passed to the function.
    sum = 0
    # starts a loop that iterates over each value in the values tuple
    for value in values:
        # adds the current value to the sum variable. It accumulates the total sum of all values
        sum += value
    # calculates the average of all the values 
    # by dividing the total sum (sum) by the number of values (number_of_values)
    average = sum / number_of_values
    # returns two values from the function: the calculated average and the total sum. 
    # The function returns these values as a tuple.
    return average, sum

av1, sum_of_numbers = ave(1,2,3,4,5,6)
print(f"{av1} and sum is {sum_of_numbers}")