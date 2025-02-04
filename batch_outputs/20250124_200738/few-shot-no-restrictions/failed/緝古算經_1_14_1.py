"""
假令有句股相乘冪七百六十五分之一，弦多於句三十六十分之九。問：三事各多少？
術曰：冪自乘，倍多數而一，為實。半多數，為廉法，從。開立方除之，即句。以弦多句加之，即弦。以句除冪，即股。
答曰：句 a ，股 b ，弦 c 。
"""

"""
This is a classic problem involving the Pythagorean theorem, where the hypotenuse (弦), one leg (句), and the other leg (股) of a right triangle are related. The problem provides the square of the hypotenuse (冪) and the relationship between the hypotenuse and one leg, and asks for the values of the three sides.

### Problem Breakdown:
1. The square of the hypotenuse (冪) is given as \( \frac{1}{765} \).
2. The hypotenuse (弦) exceeds one leg (句) by \( \frac{9}{36} = \frac{1}{4} \).
3. The goal is to find the values of the three sides: 句 (leg), 股 (other leg), and 弦 (hypotenuse).

### Solution Procedure:
1. **冪自乘**: Square the given \( \frac{1}{765} \).
2. **倍多數而一**: Multiply the excess (\( \frac{1}{4} \)) by 2 and add 1.
3. **為實**: This becomes the "實" (dividend).
4. **半多數**: Take half of the excess (\( \frac{1}{4} \)).
5. **為廉法，從**: This becomes the "廉法" (divisor).
6. **開立方除之，即句**: Take the cube root of the division result to find 句 (one leg).
7. **以弦多句加之，即弦**: Add the excess (\( \frac{1}{4} \)) to 句 to find 弦 (hypotenuse).
8. **以句除冪，即股**: Divide the square of the hypotenuse (冪) by 句 to find 股 (the other leg).

### Python Code:


"""

#----- content starts here -----

from fractions import Fraction
from sympy import Rational, cbrt

# Given values
冪 = Fraction(1, 765)  # Square of the hypotenuse
弦多句 = Fraction(9, 36)  # Excess of hypotenuse over one leg

# Step 1: 冪自乘
冪平方 = 冪 ** 2

# Step 2: 倍多數而一
倍多數 = 2 * 弦多句
實 = 倍多數 + 1

# Step 3: 半多數
廉法 = 弦多句 / 2

# Step 4: 開立方除之，即句
句 = cbrt(冪平方 / 實)

# Step 5: 以弦多句加之，即弦
弦 = 句 + 弦多句

# Step 6: 以句除冪，即股
股 = 冪 / 句

# Results
a = 句
b = 股
c = 弦

print(f"句 (leg): {a}")
print(f"股 (other leg): {b}")
print(f"弦 (hypotenuse): {c}")
#----- content ends here -----


"""


### Explanation of the Code:
1. **冪平方**: The square of the hypotenuse is squared again.
2. **實**: The dividend is calculated by doubling the excess and adding 1.
3. **廉法**: The divisor is half of the excess.
4. **句**: The cube root of the division of \( 冪平方 \) by \( 實 \) gives the value of one leg.
5. **弦**: Adding the excess to \( 句 \) gives the hypotenuse.
6. **股**: Dividing \( 冪 \) by \( 句 \) gives the other leg.

### Final Answer:
The values of the three sides are:
- \( 句 = a \)
- \( 股 = b \)
- \( 弦 = c \)
"""


"""
Variable 'a' has wrong value. Expected: 287/20, Actual: 510**(1/3)/765
Variable 'b' has wrong value. Expected: 246/5, Actual: 510**(2/3)/510
Variable 'c' has wrong value. Expected: 205/4, Actual: 510**(1/3)/765 + 1/4"""
