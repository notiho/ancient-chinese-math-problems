"""
今有粺米二斗，欲為粟。問︰得幾何？
術曰：以粺米求粟，五十之，二十七而一。
荅曰：為粟 a斗 。
"""

"""
To solve this problem, we need to convert 粺米 (white rice) into 粟 (unhusked rice). The conversion ratio is given as: for every 50 units of 粺米, we get 27 units of 粟.

Here is the Python code to compute the value of `a`:


"""


from fractions import Fraction

# Given data
粺米 = 2  # in 斗

# Conversion ratio: 50 粺米 -> 27 粟
a = Fraction(粺米 * 27, 50)  # 粟 in 斗

# Result
a  # 粟 in 斗


"""


The value of `a` will represent the amount of 粟 (unhusked rice) in 斗.
"""


"""
Variable 'a' has wrong value. Expected: 100/27, Actual: 27/25"""
