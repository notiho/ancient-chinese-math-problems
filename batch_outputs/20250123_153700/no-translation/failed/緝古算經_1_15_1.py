"""
假令有句股相乘冪四千三十六五分之□，股少於弦六五分之一。問：弦多少？。
術曰：冪自乘，倍少數而一，為實。半少，為廉法，從。開立方除之，即股。加差，即弦。
答曰：弦 a 。
"""

"""
To solve this problem, we will carefully follow the procedure described in the problem statement. Let's translate the procedure into Python code step by step.


"""


from fractions import Fraction
from math import isqrt

# Given values
冪 = Fraction(4036, 5)  # 冪四千三十六五分之□
差 = Fraction(6, 5)    # 股少於弦六五分之一

# 冪自乘
冪自乘 = 冪 * 冪

# 倍少數而一，為實
實 = 2 * 差 + 1

# 半少，為廉法，從
廉法 = 差 / 2

# 開立方除之，即股
股 = isqrt(冪自乘 / 實)

# 加差，即弦
弦 = 股 + 差

# Result
a = 弦


"""


### Explanation of the Code:
1. **冪自乘**: The square of the given 冪 is calculated.
2. **倍少數而一，為實**: The value of `實` is calculated as twice the difference (`差`) plus one.
3. **半少，為廉法，從**: The value of `廉法` is calculated as half of the difference (`差`).
4. **開立方除之，即股**: The square root of the division of `冪自乘` by `實` gives the 股.
5. **加差，即弦**: Adding the difference (`差`) to the 股 gives the 弦.

The result `a` represents the value of 弦.
"""


"""
Code error: 'Fraction' object cannot be interpreted as an integer"""
