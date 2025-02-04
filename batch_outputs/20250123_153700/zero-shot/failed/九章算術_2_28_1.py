"""
今有菽二斗，欲為豉。問︰得幾何？
術曰：以菽求豉，七之，五而一。
荅曰：為豉 a斗 。
"""

"""
To solve this problem, we need to compute the amount of 豉 (fermented beans) obtained from 2 斗 of 菽 (beans). The method described in the problem states: "以菽求豉，七之，五而一," which means for every 7 parts of beans, 5 parts of 豉 are produced.

Here's the Python code to compute the value of `a`:


"""


from fractions import Fraction

# Given data
beans = 2  # in 斗

# Conversion ratio: 7 parts of beans produce 5 parts of 豉
a = beans * Fraction(5, 7)  # amount of 豉 in 斗

# Result
a  # a斗


"""


The variable `a` will hold the amount of 豉 in 斗.
"""


"""
Variable 'a' has wrong value. Expected: 14/5, Actual: 10/7"""
