"""
今有粟九斗八升，欲為大䵂。問︰得幾何？
術曰：以粟求大䵂，二十七之，二十五而一。
荅曰：為大䵂 a斗 。
"""

"""
To solve the problem, we will translate the ancient Chinese math problem into Python code. The problem states that we have 9斗8升 of 粟 (grain) and want to convert it into 大䵂 (a larger unit). The method provided is to multiply the amount of 粟 by 27 and then divide by 25.

Here is the Python code:


"""


from fractions import Fraction

# Given amount of 粟 in 斗 and 升
粟_斗 = 9
粟_升 = 8

# Convert 升 to 斗 (1斗 = 10升)
粟_total_斗 = 粟_斗 + Fraction(粟_升, 10)

# Conversion formula: multiply by 27 and divide by 25
a = 粟_total_斗 * Fraction(27, 25)

# The result is stored in variable 'a'
a


"""


Explanation:
1. We first convert the given amount of 粟 into a single unit (斗). Since 1斗 = 10升, we add the fractional part `8/10` to the 9斗.
2. We then apply the formula: multiply the total 粟 in 斗 by 27 and divide by 25.
3. The result is stored in the variable `a`, which represents the amount of 大䵂 in 斗.

The value of `a` will be the answer.
"""


"""
"""
