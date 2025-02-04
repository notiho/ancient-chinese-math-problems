"""
今有粟九斗八升，欲為大䵂。問︰得幾何？
術曰：以粟求大䵂，二十七之，二十五而一。
荅曰：為大䵂 a斗 。
"""

"""
To solve this problem, we need to translate the ancient Chinese math problem into Python code. The problem states that we have 9斗8升 of 粟 (grain) and we want to convert it into 大䵂. The method provided says to multiply the amount of 粟 by 27 and then divide by 25.

In ancient Chinese measurements:
- 1斗 = 10升.

Thus, 9斗8升 = 9 * 10 + 8 = 98升.

The formula to compute the number of 大䵂 is:
```
大䵂 = (粟 * 27) / 25
```

Here is the Python code:


"""


from fractions import Fraction

# Given 粟 in 斗 and 升
粟_in_斗 = 9
粟_in_升 = 8

# Convert 粟 to 升
粟_total_升 = 粟_in_斗 * 10 + 粟_in_升

# Compute 大䵂
a = Fraction(粟_total_升 * 27, 25)

# Result
a  # 大䵂 in 斗


"""


The variable `a` will contain the result in terms of 大䵂.
"""


"""
Variable 'a' has wrong value. Expected: 1323/125, Actual: 2646/25"""
