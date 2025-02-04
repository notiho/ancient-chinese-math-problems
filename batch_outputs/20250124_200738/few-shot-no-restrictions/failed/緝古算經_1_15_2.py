"""
假令有句股相乘冪四千三十六五分之□，股少於弦六五分之一。問：弦多少？。
術曰：冪自乘，倍少數而一，為實。半少，為廉法，從。開立方除之，即股。加差，即弦。
答曰：弦 a 。
"""

"""
This problem involves solving a classic right triangle problem using ancient Chinese mathematical methods. The problem is essentially about finding the hypotenuse (弦) of a right triangle when given the product of the legs (句 and 股) and the relationship between one leg (股) and the hypotenuse.

### Problem Breakdown:
- The product of the legs (句股相乘) is given as \( 4036 \frac{□}{5} \), which is \( \frac{4036}{5} \).
- The shorter leg (股) is less than the hypotenuse (弦) by \( \frac{6}{5} \).
- The goal is to find the hypotenuse (弦).

### Solution Procedure:
1. **冪自乘**: Square the given product of the legs.
2. **倍少數而一，為實**: Multiply the squared product by twice the difference between the hypotenuse and the shorter leg, plus 1.
3. **半少，為廉法，從**: Take half of the difference between the hypotenuse and the shorter leg as the divisor (廉法).
4. **開立方除之，即股**: Take the cube root of the result and divide it by the divisor to find the shorter leg (股).
5. **加差，即弦**: Add the difference to the shorter leg to find the hypotenuse.

### Python Code Implementation:


"""

#----- content starts here -----

from fractions import Fraction
from sympy import symbols, solve, Eq

# Given values
冪 = Fraction(4036, 5)  # The product of the legs
差 = Fraction(6, 5)    # The difference between the hypotenuse and the shorter leg

# Step 1: 冪自乘
冪平方 = 冪 ** 2

# Step 2: 倍少數而一，為實
實 = 冪平方 * (2 * 差 + 1)

# Step 3: 半少，為廉法，從
廉法 = 差 / 2

# Step 4: 開立方除之，即股
# Solve for 股 using the equation 股 = cube_root(實) / 廉法
股 = symbols('股')
equation = Eq(股 ** 3 / 廉法, 實)
股_value = solve(equation, 股)[0]

# Step 5: 加差，即弦
弦 = 股_value + 差

# Output the result
a = 弦
print(f"弦 = {a}")
#----- content ends here -----


"""


### Explanation of the Code:
1. **冪平方**: The product of the legs is squared.
2. **實**: The squared product is multiplied by \( 2 \times 差 + 1 \).
3. **廉法**: Half of the difference between the hypotenuse and the shorter leg is calculated.
4. **股**: The shorter leg is solved using the cube root of the result divided by the divisor.
5. **弦**: The hypotenuse is calculated by adding the difference to the shorter leg.

### Final Answer:
The hypotenuse \( a \) is the value of \( 弦 \) obtained from the calculation.
"""


"""
Variable 'a' has wrong value. Expected: 1147/10, Actual: 6/5 + 2*103844262**(1/3)*5**(2/3)/25"""
