"""
今有菽一斗，欲為熟菽。問︰得幾何？
術曰：以菽求熟菽，二十三之，十而一。
荅曰：為熟菽 a斗 。
"""

"""
To solve this problem, we need to calculate the amount of 熟菽 (cooked beans) obtained from 1 斗 (dou) of 菽 (raw beans). The method provided states that for every 10 parts of raw beans, you get 23 parts of cooked beans.

Here is the Python code to compute the value of `a`:


"""


from fractions import Fraction

# Given values
raw_beans = Fraction(1)  # 1 斗 of raw beans
conversion_rate = Fraction(23, 10)  # 23 parts of cooked beans for every 10 parts of raw beans

# Calculation
a = raw_beans * conversion_rate  # Amount of cooked beans in 斗

# Result
a  # a斗 of cooked beans


"""


The value of `a` will represent the amount of cooked beans in 斗.
"""


"""
"""
