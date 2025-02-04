"""
今有御米十四斗，欲為粟。問︰得幾何？
術曰：以御米求粟，五十之，二十一而一。
荅曰：為粟 a斗 。
"""

"""
To solve this problem, we need to translate the ancient Chinese math problem into Python code. The problem states that there are 14斗 (dou) of 御米 (imperial rice), and we want to convert it into 粟 (millet). The conversion rule is given as "五十之，二十一而一," which means for every 50 units of 御米, you get 21 units of 粟.

Here's the Python code:


"""


from fractions import Fraction

# Given data
御米 = 14  # in 斗

# Conversion rule: 50 units of 御米 produce 21 units of 粟
conversion_rate = Fraction(21, 50)

# Calculate the amount of 粟
a = 御米 * conversion_rate  # in 斗

# Result
a  # This is the amount of 粟 in 斗


"""


The variable `a` will contain the result in terms of 粟 (斗).
"""


"""
Variable 'a' has wrong value. Expected: 100/3, Actual: 147/25"""
