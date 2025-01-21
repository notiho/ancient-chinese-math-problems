"""
今有粟五斗五升，欲為飧。問︰得幾何？
術曰：以粟求飧，九之，五而一。
荅曰：為飧 a斗 。
"""

"""
To solve this problem, we need to translate the ancient Chinese math problem into Python code. The problem states that we have 5斗5升 of 粟 (grain), and we want to calculate how much 飧 (cooked grain) it can produce. The method provided is to multiply the amount of 粟 by 9 and then divide by 5.

In ancient Chinese measurements:
- 1斗 = 10升.

So, 5斗5升 = \( 5 \times 10 + 5 = 55 \) 升.

Now, we calculate the amount of 飧 using the formula: \( 飧 = \frac{\text{粟} \times 9}{5} \).

Here is the Python code:


"""


from fractions import Fraction

# 粟 in 升
粟 = 5 * 10 + 5  # 5斗5升 = 55升

# Calculate 飧
a = Fraction(粟 * 9, 5)  # 飧 = (粟 * 9) / 5

# Result
a  # a斗


"""


The variable `a` will contain the result in terms of 斗.
"""


"""
Variable 'a' has wrong value. Expected: 99/10, Actual: 99"""
