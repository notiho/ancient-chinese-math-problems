"""
今有稻一十二斗六升、一十五分升之一十四，欲為粟。問︰得幾何？
術曰：以稻求粟，五之，六而一。
荅曰：為粟 a斗 。
"""

"""
To solve this problem, we will translate the ancient Chinese math problem into Python code. The problem involves converting a given amount of rice ("稻") into millet ("粟") using the ratio provided: multiply by 5, then divide by 6.

Here is the Python code:


"""


from fractions import Fraction

# Given amount of rice in dou, sheng, and fen sheng
rice = Fraction(12, 1) + Fraction(6, 10) + Fraction(1, 14 * 150)

# Conversion ratio: multiply by 5, then divide by 6
a = rice * Fraction(5, 6)

# Result in dou
a


"""


The variable `a` represents the amount of millet ("粟") in dou.
"""


"""
Variable 'a' has wrong value. Expected: 476/45, Actual: 26461/2520"""
