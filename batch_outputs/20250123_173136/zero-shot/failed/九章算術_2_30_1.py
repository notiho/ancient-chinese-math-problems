"""
今有麥一斗，欲為大䵂。問︰得幾何？
術曰：以麥求大䵂，六之，五而一。
荅曰：為大䵂 a斗 。
"""

"""
To solve this problem, we will translate the ancient Chinese math problem into Python code. The problem states that to convert one "斗" of 麥 (wheat) into 大䵂 (a type of processed grain), the conversion rate is given as "六之，五而一". This means that for every 6 parts of wheat, you get 5 parts of 大䵂.

Here is the Python code:


"""


from fractions import Fraction

# Given data
麦 = Fraction(1)  # 1 斗 of wheat

# Conversion rate: 6 parts of wheat yield 5 parts of 大䵂
a = 麦 * Fraction(5, 6)  # Calculate the amount of 大䵂

# The result
a  # 大䵂 in 斗


"""


The variable `a` will contain the result in terms of "斗".
"""


"""
Variable 'a' has wrong value. Expected: 6/5, Actual: 5/6"""
