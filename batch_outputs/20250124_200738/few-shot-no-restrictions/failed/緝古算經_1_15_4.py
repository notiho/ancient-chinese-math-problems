"""
假令有句股相乘冪四千三十六五分之□，股少於弦六五分之一。問：弦多少？。
術曰：冪自乘，倍少數而一，為實。半少，為廉法，從。開立方除之，即股。加差，即弦。
答曰：弦 a 。
"""

"""
This problem involves solving a right triangle where the hypotenuse (弦), the base (股), and the height (句) are related through the Pythagorean theorem. The given information is:

1. The product of the base (股) and the height (句) is \( \frac{4036}{5} \).
2. The base (股) is shorter than the hypotenuse (弦) by \( \frac{1}{5} \).

The procedure involves solving for the hypotenuse (弦) using the given relationships. Let's translate this into Python code:


"""

#----- content starts here -----

from fractions import Fraction
from sympy import symbols, Eq, solve

# Given values
冪 = Fraction(4036, 5)  # 股句相乘冪
差 = Fraction(1, 5)     # 股少於弦六五分之一

# Symbols for 股 (base) and 弦 (hypotenuse)
股 = symbols('股')
弦 = symbols('弦')

# 股少於弦六五分之一: 弦 = 股 + 差
弦_eq = Eq(弦, 股 + 差)

# 冪自乘，倍少數而一，為實
實 = 2 * 冪

# 半少，為廉法，從
廉法 = 差 / 2

# 開立方除之，即股
股_eq = Eq(股**2, 實 / 弦)

# Solve the equations
solution = solve([弦_eq, 股_eq], (股, 弦))

# Extract the hypotenuse (弦)
a = solution[0][1]
print(f"弦 a = {a}")
#----- content ends here -----


"""


### Explanation of the Code:
1. **冪**: The product of the base (股) and height (句) is given as \( \frac{4036}{5} \).
2. **差**: The base (股) is shorter than the hypotenuse (弦) by \( \frac{1}{5} \).
3. **Equations**:
   - \( \text{弦} = \text{股} + \text{差} \)
   - \( \text{股}^2 = \frac{\text{實}}{\text{弦}} \), where \( \text{實} = 2 \times \text{冪} \).
4. **Solve**: The equations are solved simultaneously to find the values of 股 and 弦.
5. **Output**: The hypotenuse (弦) is extracted and printed.

This code uses the `sympy` library to solve the equations symbolically. The result will give the value of the hypotenuse (弦).
"""


"""
Variable 'a' has wrong value. Expected: 1147/10, Actual: 2/15 + (-1/2 - sqrt(3)*I/2)*(2*sqrt(8246450046)/225 + 2724299/3375)**(1/3) + 1/(225*(-1/2 - sqrt(3)*I/2)*(2*sqrt(8246450046)/225 + 2724299/3375)**(1/3))"""
