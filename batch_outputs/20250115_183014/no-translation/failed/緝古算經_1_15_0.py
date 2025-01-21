"""
假令有句股相乘冪四千三十六五分之□，股少於弦六五分之一。問：弦多少？。
術曰：冪自乘，倍少數而一，為實。半少，為廉法，從。開立方除之，即股。加差，即弦。
答曰：弦 a 。
"""

"""
To solve this problem, let's carefully translate the procedure into Python code step by step.

### Problem Breakdown:
1. **Given:**
   - The product of the leg (句) and the other leg (股) is \( \frac{4036}{5} \).
   - The difference between the hypotenuse (弦) and the longer leg (股) is \( \frac{6}{5} \).

2. **Procedure:**
   - Square the given product (冪自乘).
   - Double the smaller number and add one (倍少數而一).
   - Half the smaller number (半少).
   - Use these to calculate the hypotenuse (弦).

---

### Python Code:


"""


from fractions import Fraction
from math import isqrt

# 冪四千三十六五分之□
冪 = Fraction(4036, 5)

# 股少於弦六五分之一
差 = Fraction(6, 5)

# 冪自乘
冪平方 = 冪 * 冪

# 倍少數而一
實 = 2 * 差 + 1

# 半少，為廉法
廉法 = 差 / 2

# 開立方除之，即股
股 = isqrt(冪平方 / 實)

# 加差，即弦
弦 = 股 + 差

# Answer
a = 弦


"""


### Explanation:
- The **冪** is squared to get \( 冪平方 \).
- The **實** is calculated by doubling the difference \( 差 \) and adding one.
- The **廉法** is half of the difference \( 差 \).
- The **股** is calculated by dividing \( 冪平方 \) by \( 實 \), and then taking the square root (interpreted as "開立方").
- Finally, the **弦** is obtained by adding the difference \( 差 \) to the longer leg \( 股 \).

The result \( a \) is the hypotenuse (弦).
"""


"""
Code error: 'Fraction' object cannot be interpreted as an integer"""
