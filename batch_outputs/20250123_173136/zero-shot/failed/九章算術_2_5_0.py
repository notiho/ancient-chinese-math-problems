"""
今有粟九斗八升，欲為大䵂。問︰得幾何？
術曰：以粟求大䵂，二十七之，二十五而一。
荅曰：為大䵂 a斗 。
"""

"""
To solve this problem, we will translate the ancient Chinese math problem into Python code. The problem states that there are 9斗8升 of 粟 (grain), and we want to convert it into 大䵂. The method provided is to multiply the amount of 粟 by 27 and then divide by 25. 

In ancient Chinese measurements:
- 1斗 = 10升.

Thus, 9斗8升 = \( 9 \times 10 + 8 = 98 \)升.

Now, let's compute the value of \( a \) (大䵂) using the given formula.


"""


from fractions import Fraction

# Given values
粟_in_升 = 9 * 10 + 8  # 9斗8升 converted to 升

# Formula: 大䵂 = 粟 × 27 ÷ 25
a = Fraction(粟_in_升 * 27, 25)

# Result
a  # 大䵂 in terms of 斗


"""


The variable `a` will contain the result in terms of 斗 as a fraction.
"""


"""
Variable 'a' has wrong value. Expected: 1323/125, Actual: 2646/25"""
