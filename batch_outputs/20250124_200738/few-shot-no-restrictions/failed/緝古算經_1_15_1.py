"""
假令有句股相乘冪四千三十六五分之□，股少於弦六五分之一。問：弦多少？。
術曰：冪自乘，倍少數而一，為實。半少，為廉法，從。開立方除之，即股。加差，即弦。
答曰：弦 a 。
"""

"""
This problem involves solving a right triangle where the hypotenuse (弦), the base (股), and the height (句) are related by the Pythagorean theorem. The problem provides the area of the square of the hypotenuse (冪), and the relationship between the hypotenuse and the base. Let's break it down step by step and translate it into Python code.

---

### Problem Breakdown:
1. **Given:**
   - The square of the hypotenuse (冪) is \( 4036 \frac{□}{5} \).
   - The base (股) is less than the hypotenuse (弦) by \( \frac{6}{5} \).

2. **Procedure:**
   - Multiply the square of the hypotenuse (冪) by itself.
   - Double the smaller difference (差) and add 1 to get the dividend (實).
   - Halve the smaller difference (差) to get the divisor (廉法).
   - Divide the dividend by the divisor to find the base (股).
   - Add the difference (差) to the base to find the hypotenuse (弦).

3. **Answer:**
   - The hypotenuse (弦) is \( a \).

---

### Python Code Implementation:


"""

#----- content starts here -----

from fractions import Fraction
from sympy import symbols, solve

# Given values
冪 = Fraction(4036, 5)  # Square of the hypotenuse
差 = Fraction(6, 5)    # Difference between hypotenuse and base

# Step 1: 冪自乘 (冪 squared)
冪_squared = 冪 * 冪

# Step 2: 倍少數而一 (Double the difference and add 1)
實 = 2 * 差 + 1

# Step 3: 半少 (Half the difference)
廉法 = 差 / 2

# Step 4: Solve for 股 (base)
股 = 冪_squared / 廉法

# Step 5: Add the difference to the base to get the hypotenuse
弦 = 股 + 差

# Output the result
a = 弦
print(f"弦 = {a}")
#----- content ends here -----


"""


---

### Explanation of the Code:
1. **冪 (Square of the hypotenuse):** The value \( 4036 \frac{□}{5} \) is represented as a `Fraction` to ensure precision in calculations.
2. **差 (Difference):** The difference between the hypotenuse and the base is \( \frac{6}{5} \).
3. **冪自乘:** The square of the hypotenuse is multiplied by itself.
4. **實 and 廉法:** These are calculated according to the procedure described in the problem.
5. **Solve for 股 (Base):** Using the relationship provided, the base is calculated.
6. **Solve for 弦 (Hypotenuse):** Adding the difference to the base gives the hypotenuse.

---

### Final Answer:
The hypotenuse \( a \) will be printed as the result.
"""


"""
Variable 'a' has wrong value. Expected: 1147/10, Actual: 16289314/15"""
