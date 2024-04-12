# Anonymous Functions - LAMBDA functions
# author: atacan

'''
x = lambda arg1: arg1 ** 2

answer = x(4)

print(answer)
'''
#businesstype = "standart"
businesstype = "reduced"

vatcalc = lambda amount: amount * 0.23

if businesstype == "reduced":
    vatcalc = lambda amount: amount* 0.135

cash = 10
print(vatcalc(cash))


# Sort a List - with a built-in function colled 'sorted()'
numbers = [2, 33, 55, 1, 4]
sortednumbers = sorted(numbers)

print(f"{numbers} sorted is {sortednumbers}")

# sort a dictionary - distionary doesn't supported with built-in function 'sorted()'

data = [{'first': 'Guido', 'last': 'Van Rossum', 'YOB': 1956},
        {'first': 'Grace', 'last': 'Hopper',     'YOB': 1906},
        {'first': 'Alan',  'last': 'Turing',     'YOB': 1912}]

# sorteddata = sorted(data) - this doesn't work
sorteddata = sorted(data, key=lambda x: x["YOB"])
# print(f'{data} sorted it {sorteddata}') - this looks ugly as print

for item in sorteddata:
    print(item)
