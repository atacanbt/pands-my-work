# messingwithboolean
# booleans can be True or False
# boolean is the return type of the mathematical operators  
# == , < , > , <= , >= , !=
#
# flipped with the not keyword
# be careful using And and Or
#
# author: Atacan Buyuktalas

is_alive = True
print(f"is alive = {is_alive}")

var = (2 <= 4)
print(f"var is {var}")

logic = (2 <= 100) and (3 >= 100)
print(f"logic is {logic}")
# True and False = False

grade= 400
invalid = (grade < 0) or (grade > 100)
print(f"invalid is {invalid}")
# True or False = True