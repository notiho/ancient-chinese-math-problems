"""
今有御米十四斗，欲為粟。問︰得幾何？
術曰：以御米求粟，五十之，二十一而一。
荅曰：為粟 a斗 。
"""

"""
To solve this problem, we will follow the given method. The problem states that we have 14斗 of 御米 and want to convert it to 粟. The conversion ratio is given as "五十之，二十一而一," which means for every 50 units of 御米, you get 21 units of 粟.

Here is the Python code:


"""


from fractions import Fraction

# Given data
御米 = 14  # in 斗

# Conversion ratio
conversion_ratio = Fraction(21, 50)

# Calculate 粟
a = 御米 * conversion_ratio

# Result
a  # in 斗


"""


The variable `a` will hold the value of 粟 in 斗.
"""


"""
Variable 'a' has wrong value. Expected: 100/3, Actual: 147/25"""
