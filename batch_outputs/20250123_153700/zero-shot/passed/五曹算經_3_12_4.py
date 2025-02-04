"""
今有凡醬二升飼五人，有醬三百二十斛。問：人㡬何？
術曰：列三百二十斛，每上十之得三萬二千升，以五人乘之得一十六萬升，以二升除之即得。
答曰： a人 。
"""

"""
To solve this problem, we translate the ancient Chinese math problem into Python code. Here's the solution:


"""


from fractions import Fraction

# Given data
醬_total = 320  # in 斛
醬_per_person = Fraction(2, 1)  # 2 升 per person
people_per_醬 = 5  # 5 people per 2 升

# Convert 醬_total from 斛 to 升 (1 斛 = 100 升)
醬_total_in_升 = 醬_total * 100  # 320 斛 * 100 升/斛 = 32000 升

# Calculate the total number of people
a = 醬_total_in_升 * people_per_醬 / 醬_per_person

# The answer
a  # a人


"""


The variable `a` will hold the total number of people.
"""


"""
"""
