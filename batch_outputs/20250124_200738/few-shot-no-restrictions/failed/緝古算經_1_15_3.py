"""
假令有句股相乘冪四千三十六五分之□，股少於弦六五分之一。問：弦多少？。
術曰：冪自乘，倍少數而一，為實。半少，為廉法，從。開立方除之，即股。加差，即弦。
答曰：弦 a 。
"""

"""
This is a classic problem involving the Pythagorean theorem in ancient Chinese mathematics. Here's how we can solve it step by step using Python:

### Problem Breakdown:
1. **Given:**
   - The product of the legs (句 and 股) of a right triangle is \( 4036 \frac{1}{5} \) (or \( 4036 + \frac{1}{5} \)).
   - The shorter leg (股) is less than the hypotenuse (弦) by \( 6 \frac{1}{5} \) (or \( 6 + \frac{1}{5} \)).

2. **Find:**
   - The hypotenuse (弦).

3. **Procedure:**
   - Multiply the given product of the legs (冪) by itself.
   - Double the difference between the hypotenuse and the shorter leg, then add 1. This becomes the "實" (dividend).
   - Half the difference becomes the "廉法" (divisor).
   - Divide the dividend by the divisor, then take the cube root to find the shorter leg (股).
   - Add the difference to the shorter leg to find the hypotenuse (弦).

---

### Python Code:


"""

#----- content starts here -----

from fractions import Fraction
from sympy import cbrt

# Given values
冪 = Fraction(4036, 1) + Fraction(1, 5)  # 冪 = 4036 + 1/5
差 = Fraction(6, 1) + Fraction(1, 5)     # 差 = 6 + 1/5

# Step 1: 冪自乘
冪自乘 = 冪 * 冪

# Step 2: 倍少數而一，為實
實 = 2 * 差 + 1

# Step 3: 半少，為廉法
廉法 = 差 / 2

# Step 4: From 冪自乘 and 實, find 股 (shorter leg)
股 = cbrt(冪自乘 / 實)

# Step 5: Add 差 to 股 to find 弦 (hypotenuse)
弦 = 股 + 差

# Output the result
a = 弦
print(f"弦 = {a}")
#----- content ends here -----


"""


---

### Explanation of the Code:
1. **冪自乘:** The product of the legs is squared.
2. **實:** The dividend is calculated by doubling the difference between the hypotenuse and the shorter leg, then adding 1.
3. **廉法:** The divisor is half the difference.
4. **股:** The shorter leg is found by dividing the dividend by the divisor and taking the cube root.
5. **弦:** The hypotenuse is the shorter leg plus the difference.

---

### Final Answer:
The value of the hypotenuse (弦) will be printed as a fraction or a decimal, depending on the output format.
"""


"""
Variable 'a' has wrong value. Expected: 1147/10, Actual: 31/5 + 31*13671**(1/3)*335**(2/3)/335"""
