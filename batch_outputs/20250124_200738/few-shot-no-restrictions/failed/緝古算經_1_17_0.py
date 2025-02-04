"""
假令有股弦相乘冪四千七百三十九五分之三，句少於弦五十四五分之二。問：股多少？
術曰：冪自乘，倍少數而一，為立冪。又少數再自乘，半之，以減立冪，余為實。又少數自乘，倍之，為方法。又置少數，五之，二而一，為廉法，從。開立方除之，即句。加差，即弦。弦除冪，即股。
答曰： a 。
"""

"""
This is a classic problem involving the Pythagorean theorem and ancient Chinese mathematical techniques. Let's break it down step by step and translate it into Python code.

### Problem Breakdown:
1. **Given:**
   - The product of the leg (股) and hypotenuse (弦) is \( 4739 \frac{3}{5} \) (or \( \frac{23696}{5} \)).
   - The difference between the hypotenuse (弦) and the other leg (句) is \( 54 \frac{2}{5} \) (or \( \frac{272}{5} \)).
   - We are tasked to find the length of the other leg (股).

2. **Procedure:**
   - Compute the cube of the product (冪自乘).
   - Double the difference (倍少數) and add 1 to form the cubic power (立冪).
   - Subtract half the square of the difference from the cubic power to get the "real" value (實).
   - Compute the square of the difference, double it, and use it as the divisor (方法).
   - Solve for the other leg (句) using the cubic root and division.
   - Add the difference to the leg (句) to get the hypotenuse (弦).
   - Divide the product (冪) by the hypotenuse to get the leg (股).

### Python Code:


"""

#----- content starts here -----

from fractions import Fraction
from sympy import symbols, solve, Eq

# Given values
冪 = Fraction(23696, 5)  # 股弦相乘冪
少數 = Fraction(272, 5)  # 弦 - 句

# Step 1: 冪自乘，倍少數而一，為立冪
立冪 = 冪**2 + 2 * 冪 * 少數 + 少數**2

# Step 2: 少數再自乘，半之，以減立冪，余為實
實 = 立冪 - (少數**2 / 2)

# Step 3: 少數自乘，倍之，為方法
方法 = 2 * 少數**2

# Step 4: 置少數，五之，二而一，為廉法，從
廉法 = Fraction(5, 2) * 少數

# Step 5: 開立方除之，即句
句 = solve(Eq(symbols('x')**3 / 方法, 實), symbols('x'))[0]

# Step 6: 加差，即弦
弦 = 句 + 少數

# Step 7: 弦除冪，即股
股 = 冪 / 弦

# Final Answer
a = 股
print(f"股 = {a}")
#----- content ends here -----


"""


### Explanation of the Code:
1. **冪自乘**: This computes the square of the product \( 冪^2 \).
2. **倍少數而一**: This adds the doubled difference and 1 to form the cubic power.
3. **減立冪**: Subtract half the square of the difference to get the "real" value.
4. **方法**: Compute the divisor by doubling the square of the difference.
5. **句**: Solve for the leg (句) using the cubic root and division.
6. **弦**: Add the difference to the leg to get the hypotenuse.
7. **股**: Divide the product by the hypotenuse to get the other leg.

### Final Answer:
The value of \( a \) (股) is the result of the computation.
"""


"""
Variable 'a' has wrong value. Expected: 68, Actual: 23696/(5*(272/5 + 32*2593901582**(1/3)*5**(2/3)/25))"""
