"""
今有菽一斗，欲為熟菽。問︰得幾何？
術曰：以菽求熟菽，二十三之，十而一。
荅曰：為熟菽 a斗 。
"""

"""
To solve this problem, we need to calculate the amount of 熟菽 (cooked beans) obtained from 1 斗 (1 unit) of 菽 (raw beans). The method provided states that for every 10 parts of raw beans, you get 23 parts of cooked beans.

Here is the Python code to compute the value of `a`:


"""

#----- content starts here -----

from fractions import Fraction

# Given data
raw_beans = Fraction(1)  # 1 斗 of raw beans
conversion_ratio = Fraction(23, 10)  # 23 parts cooked beans for every 10 parts raw beans

# Calculation
a = raw_beans * conversion_ratio  # Amount of cooked beans

# Result
a  # a斗 of cooked beans
#----- content ends here -----


"""


The value of `a` will represent the amount of cooked beans in 斗.
"""


"""
"""
