"""
今有凡醬二升飼五人，有醬三百二十斛。問：人㡬何？
術曰：列三百二十斛，每上十之得三萬二千升，以五人乘之得一十六萬升，以二升除之即得。
答曰： a人 。
"""

"""
To solve this problem, we need to calculate the number of people ("a") that can be fed with 320 hu (斛) of sauce, given that 2 sheng (升) of sauce can feed 5 people.

Here is the Python code:


"""


from fractions import Fraction

# Conversion factor: 1 hu = 10 sheng
hu_to_sheng = 10

# Given values
sauce_in_hu = 320  # 320 hu
sauce_per_person = Fraction(2, 5)  # 2 sheng feeds 5 people

# Convert sauce from hu to sheng
sauce_in_sheng = sauce_in_hu * hu_to_sheng

# Calculate the number of people
a = sauce_in_sheng / sauce_per_person

# Result
a  # Number of people


"""


The variable `a` will contain the number of people that can be fed.
"""


"""
Variable 'a' has wrong value. Expected: 80000, Actual: 8000"""
