"""
今有菽一斗，欲為熟菽。問︰得幾何？
術曰：以菽求熟菽，二十三之，十而一。
荅曰：為熟菽 a斗 。
"""

"""
To solve this problem, we need to calculate the amount of 熟菽 (cooked beans) obtained from 1 斗 (a unit of volume) of 菽 (raw beans). The method described in the problem states that for every 10 parts of raw beans, you get 1 part of cooked beans, and then multiply the result by 23.

Here is the Python code to compute the value of `a`:


"""

#----- content starts here -----

from fractions import Fraction

# Given data
raw_beans = Fraction(1)  # 1 斗 of raw beans

# Calculation
a = raw_beans * Fraction(1, 10) * 23  # Cooked beans

# Result
a  # a斗 of cooked beans
#----- content ends here -----


"""


The value of `a` will represent the amount of cooked beans in 斗.
"""


"""
"""
