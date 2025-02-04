"""
今有兵三千八百三十七人，人給錢五百五十六文。問：計㡬何？
術曰：列兵三千八百三十七人，以五百五十六文乘之即得。
答曰： a貫 。
"""

"""
To solve this problem, we need to calculate the total amount of money required to pay 3,837 soldiers, where each soldier is given 556 wen. The result will be expressed in "貫" (1 貫 = 1,000 wen).

Here is the Python code:


"""

#----- content starts here -----

from fractions import Fraction

# Given data
soldiers = 3837  # number of soldiers
money_per_soldier = 556  # wen per soldier

# Total money in wen
total_money_wen = soldiers * money_per_soldier

# Convert wen to 貫 (1 貫 = 1000 wen)
a = Fraction(total_money_wen, 1000)

# Result
a  # in 貫
#----- content ends here -----


"""


The variable `a` will contain the total amount in 貫.
"""


"""
"""
