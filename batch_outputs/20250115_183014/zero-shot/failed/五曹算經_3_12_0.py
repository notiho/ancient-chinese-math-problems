"""
今有凡醬二升飼五人，有醬三百二十斛。問：人㡬何？
術曰：列三百二十斛，每上十之得三萬二千升，以五人乘之得一十六萬升，以二升除之即得。
答曰： a人 。
"""

"""
To solve this problem, we will translate the ancient Chinese math problem into Python code. The problem states that 2 sheng (升) of sauce can feed 5 people. Given 320 hu (斛) of sauce, we need to calculate how many people can be fed.

1 hu (斛) = 10 sheng (升).


"""


from fractions import Fraction

# Given data
sauce_per_person = Fraction(2, 5)  # 2 sheng feeds 5 people
total_sauce_hu = 320  # 320 hu
sheng_per_hu = 10  # 1 hu = 10 sheng

# Convert total sauce to sheng
total_sauce_sheng = total_sauce_hu * sheng_per_hu

# Calculate the number of people
a = total_sauce_sheng / sauce_per_person

# Result
a  # Number of people


"""


The variable `a` will hold the number of people that can be fed.
"""


"""
Variable 'a' has wrong value. Expected: 80000, Actual: 8000"""
