# convert.py
# this program prompts the amount of a 'debt' in euro and prints it out in cent
# author: atacan buyuktalas

debt = float(input("Enter the amount of debt: "))
debt_in_cent = abs(debt) * 100
print('That amount in cent is {}'.format(int(debt_in_cent)))
# set the "debt_in_cent" as int in the print command to get the result in cent as integer 
