"""
今有凡醬二升飼五人，有醬三百二十斛。問：人㡬何？
術曰：列三百二十斛，每上十之得三萬二千升，以五人乘之得一十六萬升，以二升除之即得。
答曰： a人 。
"""

"""
To solve this problem, we will translate the ancient Chinese math problem into Python code. Here's the solution:


"""

#----- content starts here -----

from fractions import Fraction

# Given values
醬_per_person = Fraction(2)  # 2 升 per 5 people
total_醬 = Fraction(320)  # 320 斛
升_per_斛 = Fraction(10)  # 10 升 per 1 斛

# Convert total 醬 from 斛 to 升
total_醬_in_升 = total_醬 * 升_per_斛

# Calculate the total number of people
a = total_醬_in_升 / 醬_per_person

# The answer is stored in variable 'a'
a
#----- content ends here -----


"""


The variable `a` will contain the number of people.
"""


"""
Variable 'a' has wrong value. Expected: 80000, Actual: 1600"""
