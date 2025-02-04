"""
今有麥一斗，欲為大䵂。問︰得幾何？
術曰：以麥求大䵂，六之，五而一。
荅曰：為大䵂 a斗 。
"""

"""
To solve this problem, we will translate the ancient Chinese math problem into Python code. The problem states that to convert one "斗" of wheat into "大䵂", the conversion factor is "六之，五而一". This means multiplying by 6 and then dividing by 5. Let's compute the value of "a" (the amount of "大䵂" obtained).

Here is the Python code:


"""


from fractions import Fraction

# Given data
wheat = Fraction(1)  # 1斗 of wheat

# Conversion factor: multiply by 6, then divide by 5
a = wheat * Fraction(6, 5)

# Output the result
a  # a斗 of 大䵂


"""


The variable `a` will hold the result in terms of "斗".
"""


"""
"""
