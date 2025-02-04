"""
假令有股弦相乘冪四千七百三十九五分之三，句少於弦五十四五分之二。問：股多少？
術曰：冪自乘，倍少數而一，為立冪。又少數再自乘，半之，以減立冪，余為實。又少數自乘，倍之，為方法。又置少數，五之，二而一，為廉法，從。開立方除之，即句。加差，即弦。弦除冪，即股。
答曰： a 。
"""

"""
This is a problem involving the Pythagorean theorem and cubic equations. Let's translate the problem and procedure into Python code step by step.

### Problem Breakdown:
- There is a product of the leg (股) and hypotenuse (弦), which is given as \( 4739 \frac{3}{5} \) (or \( \frac{23698}{5} \)).
- The other leg (句) is shorter than the hypotenuse by \( 54 \frac{2}{5} \) (or \( \frac{272}{5} \)).
- We are tasked to find the length of the leg (股).

### Procedure:
1. Square the product (冪自乘), double the difference (倍少數), and add 1 to form the cubic power (立冪).
2. Square the difference (少數再自乘), halve it, and subtract it from the cubic power to get the remainder (實).
3. Square the difference (少數自乘), double it, to form the divisor (方法).
4. Multiply the difference by 5, divide by 2, to form the linear divisor (廉法).
5. Extract the cube root of the remainder, divide it by the divisor, to get the shorter leg (句).
6. Add the difference to get the hypotenuse (弦).
7. Divide the product by the hypotenuse to get the other leg (股).

### Python Code:


"""


from fractions import Fraction
from math import pow

# 冪四千七百三十九五分之三
冪 = Fraction(23698, 5)

# 句少於弦五十四五分之二
少數 = Fraction(272, 5)

# 冪自乘
冪自乘 = 冪 ** 2

# 倍少數而一，為立冪
立冪 = 2 * 少數 + 1

# 又少數再自乘，半之，以減立冪，余為實
少數再自乘 = 少數 ** 2
實 = 立冪 - (少數再自乘 / 2)

# 又少數自乘，倍之，為方法
方法 = 2 * (少數 ** 2)

# 又置少數，五之，二而一，為廉法
廉法 = (5 * 少數) / 2

# 開立方除之，即句
句 = pow(實, 1/3) / 方法

# 加差，即弦
弦 = 句 + 少數

# 弦除冪，即股
股 = 冪 / 弦

a = 股
print(f"股 = {a}")


"""


### Explanation of Variables:
- `冪`: The product of the leg and hypotenuse.
- `少數`: The difference between the hypotenuse and the shorter leg.
- `立冪`: The cubic power calculated from the product and difference.
- `實`: The remainder after subtracting the halved square of the difference from the cubic power.
- `方法`: The divisor for the cube root calculation.
- `廉法`: The linear divisor for the calculation.
- `句`: The shorter leg.
- `弦`: The hypotenuse.
- `股`: The other leg.

### Final Answer:
The value of `a` will be the length of the leg (股).
"""


"""
Code error: math domain error"""
