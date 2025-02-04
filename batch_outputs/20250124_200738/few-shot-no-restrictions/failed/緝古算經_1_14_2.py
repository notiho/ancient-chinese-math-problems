"""
假令有句股相乘冪七百六十五分之一，弦多於句三十六十分之九。問：三事各多少？
術曰：冪自乘，倍多數而一，為實。半多數，為廉法，從。開立方除之，即句。以弦多句加之，即弦。以句除冪，即股。
答曰：句 a ，股 b ，弦 c 。
"""

"""
This problem involves solving a classic right triangle problem using ancient Chinese mathematical methods. The problem gives the relationship between the hypotenuse (弦), one leg (句), and the other leg (股), along with the area of the square of the hypotenuse (冪). Let's translate this into Python code step by step.

---

### Problem Breakdown:
1. **Given:**
   - The product of the two legs (句股相乘) is \( \frac{1}{765} \) (冪).
   - The hypotenuse (弦) is greater than one leg (句) by \( \frac{9}{36} = \frac{1}{4} \) (弦多於句).

2. **Find:**
   - The values of the three components: 句 (one leg), 股 (the other leg), and 弦 (the hypotenuse).

3. **Procedure:**
   - Square the given product (冪自乘).
   - Multiply it by twice the "difference" (倍多數而一).
   - Use the result to find the cube root (開立方).
   - From the cube root, calculate the three components:
     - 句 (one leg).
     - 弦 (hypotenuse) = 句 + the difference.
     - 股 (the other leg) = 冪 / 句.

---

### Python Code Implementation:


"""

#----- content starts here -----

from fractions import Fraction
from sympy import cbrt

# Given values
冪 = Fraction(1, 765)  # The product of the two legs
弦多句 = Fraction(9, 36)  # The difference between the hypotenuse and one leg

# Step 1: 冪自乘 (square the given product)
冪平方 = 冪 ** 2

# Step 2: 倍多數而一 (multiply by twice the difference plus 1)
倍多數 = 2 * 弦多句 + 1
實 = 冪平方 * 倍多數

# Step 3: 開立方 (find the cube root to get 句)
句 = cbrt(實)

# Step 4: Calculate 弦 (hypotenuse) = 句 + 弦多句
弦 = 句 + 弦多句

# Step 5: Calculate 股 (the other leg) = 冪 / 句
股 = 冪 / 句

# Final results
a = 句
b = 股
c = 弦

# Print results
print(f"句 (one leg): {a}")
print(f"股 (the other leg): {b}")
print(f"弦 (hypotenuse): {c}")
#----- content ends here -----


"""


---

### Explanation of the Code:
1. **冪平方**: The square of the given product \( \frac{1}{765} \).
2. **倍多數**: The multiplier is twice the difference \( \frac{1}{4} \) plus 1.
3. **實**: The intermediate result obtained by multiplying \( 冪平方 \) by \( 倍多數 \).
4. **句**: The cube root of \( 實 \), which gives one leg of the triangle.
5. **弦**: The hypotenuse is calculated by adding the difference \( \frac{1}{4} \) to \( 句 \).
6. **股**: The other leg is calculated by dividing \( 冪 \) by \( 句 \).

---

### Output:
The program will output the values of 句 (one leg), 股 (the other leg), and 弦 (the hypotenuse) as fractions for precise representation.
"""


"""
Variable 'a' has wrong value. Expected: 287/20, Actual: 340**(1/3)/510
Variable 'b' has wrong value. Expected: 246/5, Actual: 14450**(1/3)/255
Variable 'c' has wrong value. Expected: 205/4, Actual: 340**(1/3)/510 + 1/4"""
