"""
假令有句股相乘冪四千三十六五分之□，股少於弦六五分之一。問：弦多少？。
術曰：冪自乘，倍少數而一，為實。半少，為廉法，從。開立方除之，即股。加差，即弦。
答曰：弦 a 。
"""

"""
This is a classic problem involving the Pythagorean theorem and ancient Chinese mathematical techniques. Let's break it down step by step and translate it into Python code.

### Problem Description:
- The product of the leg lengths (句 and 股) is given as \( 4036 \frac{1}{5} \) (or \( 4036 + \frac{1}{5} \)).
- The shorter leg (股) is less than the hypotenuse (弦) by \( 6 \frac{1}{5} \) (or \( 6 + \frac{1}{5} \)).
- We are tasked with finding the hypotenuse (弦).

### Procedure:
1. **冪自乘**: Square the given product of the legs.
2. **倍少數而一**: Multiply the squared value by twice the difference between the hypotenuse and the shorter leg, plus 1.
3. **為實**: This gives the dividend (實).
4. **半少，為廉法，從**: Half the difference between the hypotenuse and the shorter leg becomes the divisor (廉法).
5. **開立方除之，即股**: Take the cube root of the dividend divided by the divisor to find the shorter leg (股).
6. **加差，即弦**: Add the difference to the shorter leg to find the hypotenuse.

### Python Code:


"""

#----- content starts here -----

from fractions import Fraction
from sympy import symbols, solve, Eq

# Given values
冪 = Fraction(4036, 1) + Fraction(1, 5)  # 冪 = 4036 + 1/5
差 = Fraction(6, 1) + Fraction(1, 5)    # 差 = 6 + 1/5

# Step 1: 冪自乘
冪平方 = 冪 ** 2

# Step 2: 倍少數而一
實 = 冪平方 * (2 * 差 + 1)

# Step 3: 半少，為廉法
廉法 = 差 / 2

# Step 4: 開立方除之，即股
股 = (實 / 廉法) ** (1 / 3)

# Step 5: 加差，即弦
弦 = 股 + 差

# Output the result
a = 弦
print(f"弦 = {a}")
#----- content ends here -----


"""


### Explanation of the Code:
1. **冪自乘**: The product of the legs is squared.
2. **倍少數而一**: The squared value is multiplied by \( 2 \times 差 + 1 \), as per the procedure.
3. **半少，為廉法**: Half the difference becomes the divisor.
4. **開立方除之，即股**: The cube root of the dividend divided by the divisor gives the shorter leg.
5. **加差，即弦**: Adding the difference to the shorter leg gives the hypotenuse.

### Final Answer:
The hypotenuse \( a \) will be computed and printed as a fraction.
"""


"""
Variable 'a' has wrong value. Expected: 1147/10, Actual: 419.1487478294179"""
