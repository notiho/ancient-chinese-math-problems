"""
假令有句股相乘冪四千三十六五分之□，股少於弦六五分之一。問：弦多少？。
術曰：冪自乘，倍少數而一，為實。半少，為廉法，從。開立方除之，即股。加差，即弦。
答曰：弦 a 。
"""

"""
To solve this problem, let's carefully translate the ancient Chinese procedure into Python code step by step.

### Problem Breakdown:
1. **Given:**
   - The product of the "句" (base) and "股" (height) is \( \frac{4036}{5} \).
   - The "股" (height) is less than the hypotenuse ("弦") by \( \frac{6}{5} \).

2. **Procedure:**
   - Square the product ("冪自乘").
   - Double the difference between the "股" and "弦" and add 1 ("倍少數而一").
   - Use this to calculate the "廉法" (a divisor).
   - Solve for the "股" (height) by taking the cube root and dividing.
   - Add the difference to the "股" to get the "弦" (hypotenuse).

### Python Code:


"""


from fractions import Fraction
from math import pow

# Given values
冪 = Fraction(4036, 5)  # The product of "句" and "股"
差 = Fraction(6, 5)    # The difference between "股" and "弦"

# 冪自乘
冪平方 = 冪 ** 2

# 倍少數而一
實 = 2 * 差 + 1

# 半少，為廉法
廉法 = 差 / 2

# Solve for 股 (height)
股 = pow(冪平方 / 實, 1/3) / 廉法

# Add the difference to 股 to get 弦 (hypotenuse)
弦 = 股 + 差

# Result
a = 弦


"""


### Explanation of the Code:
1. **冪自乘:** The square of the given product \( \frac{4036}{5} \).
2. **倍少數而一:** Double the difference \( \frac{6}{5} \) and add 1.
3. **半少，為廉法:** Half the difference is used as the divisor.
4. **Solve for 股:** The cube root of the ratio of \( 冪平方 \) to \( 實 \), divided by \( 廉法 \).
5. **Solve for 弦:** Add the difference \( 差 \) to \( 股 \) to get \( 弦 \).

### Final Answer:
The hypotenuse \( a \) is the value of \( 弦 \).
"""


"""
Variable 'a' has wrong value. Expected: 1147/10, Actual: 97.28963552770584"""
