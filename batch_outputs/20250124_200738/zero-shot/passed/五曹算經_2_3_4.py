"""
今有兵三千八百三十七人，人給錢五百五十六文。問：計㡬何？
術曰：列兵三千八百三十七人，以五百五十六文乘之即得。
答曰： a貫 。
"""

"""
To solve this problem, we are calculating the total amount of money required to pay 3,837 soldiers, where each soldier is given 556 "文". The result is expressed in "貫", where 1 貫 = 1,000 文.

Here is the Python code to compute the solution:


"""

#----- content starts here -----

from fractions import Fraction

# Given data
soldiers = 3837  # Number of soldiers
money_per_soldier = 556  # Money per soldier in 文

# Total money in 文
total_money_in_wen = soldiers * money_per_soldier

# Convert 文 to 貫 (1 貫 = 1000 文)
a = Fraction(total_money_in_wen, 1000)

# The result is stored in variable 'a'
#----- content ends here -----


"""


The value of `a` will represent the total amount of money in 貫.
"""


"""
"""
