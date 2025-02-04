"""
今有麥一斗，欲為大䵂。問︰得幾何？
術曰：以麥求大䵂，六之，五而一。
荅曰：為大䵂 a斗 。
"""

"""
To solve this problem, we need to translate the ancient Chinese math problem into Python code. The problem states that for every 6 parts of 麥 (wheat), we get 5 parts of 大䵂 (a type of processed grain). The question asks how much 大䵂 can be obtained from 1 斗 of 麥.

Here is the Python code:


"""


from fractions import Fraction

# Given: 麥 = 1 斗
麦 = Fraction(1)

# Conversion ratio: 6 parts of 麥 produce 5 parts of 大䵂
# 大䵂 = 麥 * (5/6)
a = 麦 * Fraction(5, 6)

# Result
a斗 = a  # 大䵂 in 斗


"""


The solution is stored in the variable `a斗`.
"""


"""
Variable 'a' has wrong value. Expected: 6/5, Actual: 5/6"""
