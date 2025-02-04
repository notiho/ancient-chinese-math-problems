"""
假令有句股相乘冪七百六十五分之一，弦多於句三十六十分之九。問：三事各多少？
術曰：冪自乘，倍多數而一，為實。半多數，為廉法，從。開立方除之，即句。以弦多句加之，即弦。以句除冪，即股。
答曰：句 a ，股 b ，弦 c 。
"""

"""
This is a classic problem involving a right triangle, where the hypotenuse (弦), one leg (句), and the other leg (股) are related by the Pythagorean theorem. The problem provides the following:

1. The product of the two legs (句股相乘) is \( \frac{1}{765} \) (冪).
2. The hypotenuse (弦) exceeds one leg (句) by \( \frac{9}{36} = \frac{1}{4} \) (弦多於句三十六分之九).

We are tasked to find the values of the three sides: 句 (leg), 股 (leg), and 弦 (hypotenuse).

The procedure (術) is as follows:
1. Square the given product of the legs (冪自乘).
2. Multiply the result by twice the excess of the hypotenuse over the leg (\( 2 \times \text{多數} \)) and add 1 (\( 倍多數而一 \)).
3. Take half the excess (\( \frac{\text{多數}}{2} \)) as the divisor (廉法).
4. Extract the cube root of the result and divide by the divisor to find 句 (one leg).
5. Add the excess to 句 to find 弦 (the hypotenuse).
6. Divide the given product of the legs (冪) by 句 to find 股 (the other leg).

Let's translate this into Python code:


"""

#----- content starts here -----

from fractions import Fraction
from sympy import Rational, cbrt

# Given values
冪 = Fraction(1, 765)  # Product of the legs
多數 = Fraction(9, 36)  # Excess of the hypotenuse over one leg

# Step 1: 冪自乘
冪平方 = 冪 ** 2

# Step 2: 倍多數而一
實 = 冪平方 * (2 * 多數 + 1)

# Step 3: 半多數，為廉法
廉法 = 多數 / 2

# Step 4: 開立方除之，即句
句 = cbrt(實) / 廉法

# Step 5: 以弦多句加之，即弦
弦 = 句 + 多數

# Step 6: 以句除冪，即股
股 = 冪 / 句

# Results
a = 句
b = 股
c = 弦

# Print the results
print(f"句 (leg): {a}")
print(f"股 (leg): {b}")
print(f"弦 (hypotenuse): {c}")
#----- content ends here -----


"""


### Explanation of the Code:
1. **冪自乘**: The square of the product of the legs is calculated.
2. **倍多數而一**: The result is multiplied by \( 2 \times \text{多數} + 1 \).
3. **半多數，為廉法**: Half of the excess (\( \frac{\text{多數}}{2} \)) is used as the divisor.
4. **開立方除之，即句**: The cube root of the result is divided by the divisor to find 句.
5. **以弦多句加之，即弦**: The excess is added to 句 to find 弦.
6. **以句除冪，即股**: The product of the legs is divided by 句 to find 股.

### Final Answer:
The values of 句 (leg), 股 (leg), and 弦 (hypotenuse) are represented as `a`, `b`, and `c`, respectively.
"""


"""
Variable 'a' has wrong value. Expected: 287/20, Actual: 4*340**(1/3)/255
Variable 'b' has wrong value. Expected: 246/5, Actual: 14450**(1/3)/2040
Variable 'c' has wrong value. Expected: 205/4, Actual: 4*340**(1/3)/255 + 1/4"""
