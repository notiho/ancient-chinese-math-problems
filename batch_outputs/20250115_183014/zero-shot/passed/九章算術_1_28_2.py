"""
今有箕田，舌廣二十步，踵廣五步，正從三十步。問：為田幾何？
術曰：并踵、舌而半之，以乘正從。畝法而一。
荅曰： a畝 。
"""

"""
To solve this problem, we will translate the ancient Chinese math problem into Python code. Here's the solution:


"""


from fractions import Fraction

# Given values
舌廣 = 20  # steps
踵廣 = 5   # steps
正從 = 30  # steps

# Calculation
a = Fraction((舌廣 + 踵廣) * 正從, 2) / 240  # Convert to 畝 (1 畝 = 240 square steps)

# The result is stored in variable 'a'
a


"""


The variable `a` will contain the area of the field in 畝.
"""


"""
"""
