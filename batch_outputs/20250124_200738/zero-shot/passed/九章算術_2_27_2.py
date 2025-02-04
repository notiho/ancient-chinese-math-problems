"""
今有菽一斗，欲為熟菽。問︰得幾何？
術曰：以菽求熟菽，二十三之，十而一。
荅曰：為熟菽 a斗 。
"""

"""
To solve this problem, we need to calculate the amount of cooked beans ("熟菽") obtained from one "斗" of raw beans ("菽"). The method provided in the problem states that for every 10斗 of raw beans, you get 23斗 of cooked beans. Thus, the conversion ratio is 23/10.

Here is the Python code to compute the value of "a" (the amount of cooked beans):


"""

#----- content starts here -----

from fractions import Fraction

# Given data
raw_beans = Fraction(1)  # 1斗 of raw beans
conversion_ratio = Fraction(23, 10)  # 23斗 cooked beans per 10斗 raw beans

# Calculation
a = raw_beans * conversion_ratio  # Amount of cooked beans

# Result
a  # a斗 of cooked beans
#----- content ends here -----


"""


The value of `a` will represent the amount of cooked beans in "斗".
"""


"""
"""
