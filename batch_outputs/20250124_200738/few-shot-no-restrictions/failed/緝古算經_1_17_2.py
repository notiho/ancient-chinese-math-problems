"""
假令有股弦相乘冪四千七百三十九五分之三，句少於弦五十四五分之二。問：股多少？
術曰：冪自乘，倍少數而一，為立冪。又少數再自乘，半之，以減立冪，余為實。又少數自乘，倍之，為方法。又置少數，五之，二而一，為廉法，從。開立方除之，即句。加差，即弦。弦除冪，即股。
答曰： a 。
"""

"""
This is a classic problem involving the Pythagorean theorem and cubic equations. Let's break it down step by step and encode it in Python. The problem involves solving for the "leg" (股) of a right triangle given the relationship between the hypotenuse (弦), the other leg (句), and the square of the hypotenuse (冪).

### Problem Explanation:
- The square of the hypotenuse (冪) is given as \( 4739 \frac{3}{5} \).
- The difference between the hypotenuse (弦) and the other leg (句) is \( 54 \frac{2}{5} \).
- We are tasked with finding the length of the remaining leg (股).

The procedure involves:
1. Calculating the "立冪" (cubed power) based on the given difference.
2. Using the difference to calculate intermediate values.
3. Solving for the hypotenuse (弦), the other leg (句), and finally the remaining leg (股).

Here is the Python implementation:


"""

#----- content starts here -----

from fractions import Fraction
from sympy import symbols, solve, Eq

# Given values
冪 = Fraction(4739 * 5 + 3, 5)  # 4739 3/5
少數 = Fraction(54 * 5 + 2, 5)  # 54 2/5

# Step 1: 冪自乘，倍少數而一，為立冪
立冪 = 冪 * 冪 * 2 * 少數 + 1

# Step 2: 少數再自乘，半之，以減立冪，余為實
實 = 立冪 - (少數 * 少數 / 2)

# Step 3: 少數自乘，倍之，為方法
方法 = 2 * (少數 * 少數)

# Step 4: 置少數，五之，二而一，為廉法，從
廉法 = 少數 * 5 / 2

# Step 5: 開立方除之，即句
句 = (實 / 方法) ** (1 / 3)

# Step 6: 加差，即弦
弦 = 句 + 少數

# Step 7: 弦除冪，即股
股 = 冪 / 弦

# Final answer
a = 股
print(f"股 = {a}")
#----- content ends here -----


"""


### Explanation of the Code:
1. **冪自乘，倍少數而一，為立冪**: This calculates the "cubed power" based on the given difference (少數).
2. **少數再自乘，半之，以減立冪，余為實**: This calculates the intermediate value "實" by subtracting half the square of the difference from the cubed power.
3. **少數自乘，倍之，為方法**: This calculates the divisor "方法" by doubling the square of the difference.
4. **置少數，五之，二而一，為廉法，從**: This calculates the divisor "廉法" for the next step.
5. **開立方除之，即句**: This solves for the other leg (句) by taking the cube root of the ratio of "實" to "方法".
6. **加差，即弦**: The hypotenuse (弦) is obtained by adding the difference (少數) to the other leg (句).
7. **弦除冪，即股**: Finally, the remaining leg (股) is calculated by dividing the square of the hypotenuse (冪) by the hypotenuse (弦).

### Final Answer:
The value of 股 (the remaining leg) is stored in `a`. You can run the code to compute the exact value.
"""


"""
Variable 'a' has wrong value. Expected: 68, Actual: 36.779124688883876"""
