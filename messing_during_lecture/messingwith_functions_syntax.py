# messingwith_functions
# materials written druing the lecture
# author : atacan

# x, y, z = (1, 2, 3)
# print (x, y, z, sep="", end=" ")
# print(f"{x} {y} {z}")
# print ("{} {} {}".format(x,y,z)) # old way of doing

def topower(number, power=3):
    #print(number) - for debugging purposes
    return (number ** power)


# ans = cube(23)
# print(f"we got {ans}")
num = 45

print(f"and {num} is {topower(num, 2)}")