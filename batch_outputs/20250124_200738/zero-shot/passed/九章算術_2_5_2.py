"""
今有粟九斗八升，欲為大䵂。問︰得幾何？
術曰：以粟求大䵂，二十七之，二十五而一。
荅曰：為大䵂 a斗 。
"""

"""
To solve this problem, we will translate the ancient Chinese math problem into Python code. The problem involves converting a given amount of 粟 (grain) into 大䵂 (a larger unit of measurement). The method described in the problem states that we multiply the amount of 粟 by 27 and then divide by 25 to find the equivalent amount in 大䵂.

Here is the Python code:


"""

#----- content starts here -----

from fractions import Fraction

# Given values
grain = Fraction(9, 1) + Fraction(8, 10)  # 9斗8升 (1斗 = 10升)

# Conversion formula: 大䵂 = (grain * 27) / 25
a = (grain * 27) / 25

# Result
a  # 大䵂 in terms of 斗
#----- content ends here -----


"""


### Explanation:
1. The input grain is given as 9斗8升. Since 1斗 = 10升, this is converted into a fraction: `9 + 8/10`.
2. The formula provided in the problem is applied: multiply the grain by 27 and divide by 25.
3. The result is stored in the variable `a`, which represents the amount of 大䵂 in 斗.

Let me know if you need further clarification!
"""


"""
"""
