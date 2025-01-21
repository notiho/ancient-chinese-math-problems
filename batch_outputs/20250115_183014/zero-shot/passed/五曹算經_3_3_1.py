"""
今有粟三百六十二斛。問：為御米㡬何？
術曰：列粟三百六十二斛，以二十一升乘之得七千六百二斛，以五十除之即得。
答曰： a斛 。
"""

"""
To solve this problem, we will translate the ancient Chinese math problem into Python code. The problem involves converting a given amount of 粟 (millet) into 御米 (imperial rice) using the given ratios.

Here is the Python code:


"""


from fractions import Fraction

# Given values
粟 = 362  # in 斛
conversion_factor = Fraction(21, 1)  # 21 升 per 1 斛
御米_conversion = Fraction(1, 50)  # 1 御米 per 50 升

# Calculate the total amount of 御米
total_升 = 粟 * conversion_factor  # Convert 粟 to 升
a = total_升 * 御米_conversion  # Convert 升 to 御米

# Result
a  # in 斛


"""


The variable `a` will contain the amount of 御米 in 斛.
"""


"""
"""
