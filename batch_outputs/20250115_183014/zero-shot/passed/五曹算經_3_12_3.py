"""
今有凡醬二升飼五人，有醬三百二十斛。問：人㡬何？
術曰：列三百二十斛，每上十之得三萬二千升，以五人乘之得一十六萬升，以二升除之即得。
答曰： a人 。
"""

"""
To solve this problem, we will translate the ancient Chinese math problem into Python code. Here's the solution:


"""


from fractions import Fraction

# Given data
total_sauce = 320  # in hu (斛)
sauce_per_person = Fraction(2)  # in sheng (升)
people_per_2_sheng = 5  # people fed by 2 sheng

# Convert total sauce from hu to sheng (1 hu = 100 sheng)
total_sauce_in_sheng = total_sauce * 100  # 320 hu * 100 sheng/hu = 32000 sheng

# Calculate the total number of people
a = total_sauce_in_sheng * people_per_2_sheng / sauce_per_person  # a = (32000 * 5) / 2

# Result
a  # a is the total number of people


"""


The variable `a` will contain the total number of people that can be fed.
"""


"""
"""
