"""
今有麥一斗，欲為大䵂。問︰得幾何？
術曰：以麥求大䵂，六之，五而一。
荅曰：為大䵂 a斗 。
"""

"""
To solve this problem, we will translate the ancient Chinese math problem into Python code. The problem states that to convert one "斗" of wheat into "大䵂", the conversion factor is "六之，五而一", which means multiplying by \( \frac{5}{6} \).

Here is the Python code:


"""

#----- content starts here -----

from fractions import Fraction

# Given data
wheat = Fraction(1)  # 1 斗 of wheat

# Conversion factor
conversion_factor = Fraction(5, 6)

# Calculate the amount of 大䵂
a = wheat * conversion_factor

# Result
a  # a is the amount of 大䵂 in 斗
#----- content ends here -----


"""


The variable `a` will store the result in terms of "斗".
"""


"""
Variable 'a' has wrong value. Expected: 6/5, Actual: 5/6"""
