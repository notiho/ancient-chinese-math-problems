"""
假令有股弦相乘冪四千七百三十九五分之三，句少於弦五十四五分之二。問：股多少？
術曰：冪自乘，倍少數而一，為立冪。又少數再自乘，半之，以減立冪，余為實。又少數自乘，倍之，為方法。又置少數，五之，二而一，為廉法，從。開立方除之，即句。加差，即弦。弦除冪，即股。
答曰： a 。
"""

"""
This problem involves solving a classic right triangle problem using ancient Chinese mathematical methods. The problem gives the relationship between the hypotenuse (弦), the base (句), and the perpendicular (股), and asks for the value of the perpendicular (股). Let's translate this into Python step by step.

### Problem Breakdown:
1. **Given:**
   - The product of the base (句) and the hypotenuse (弦) is \( 4739 \frac{3}{5} \) (or \( \frac{23698}{5} \)).
   - The base (句) is less than the hypotenuse (弦) by \( 54 \frac{2}{5} \) (or \( \frac{272}{5} \)).

2. **Procedure:**
   - Compute the cube of the product (冪) by squaring it and multiplying by 2.
   - Use the difference between the base and hypotenuse to compute intermediate values.
   - Solve for the base (句), hypotenuse (弦), and finally the perpendicular (股).

---

### Python Code:


"""

#----- content starts here -----

from fractions import Fraction
from math import pow

# Given values
冪 = Fraction(4739, 5)  # 股弦相乘冪
少數 = Fraction(272, 5)  # 句少於弦

# Step 1: 冪自乘，倍少數而一，為立冪
立冪 = 冪**2 + 2 * 冪 * 少數 + 少數**2

# Step 2: 又少數再自乘，半之，以減立冪，余為實
實 = 立冪 - (少數**2 / 2)

# Step 3: 又少數自乘，倍之，為方法
方法 = 2 * (少數**2)

# Step 4: 又置少數，五之，二而一，為廉法，從
廉法 = (5 * 少數) / 2

# Step 5: 開立方除之，即句
句 = pow(實 / 方法, 1/3)

# Step 6: 加差，即弦
弦 = 句 + 少數

# Step 7: 弦除冪，即股
股 = 冪 / 弦

# Final Answer
a = 股
print(f"股 = {a}")
#----- content ends here -----


"""


---

### Explanation of the Code:
1. **冪自乘，倍少數而一，為立冪:**
   - Compute the cube of the product (冪) by squaring it and adding terms involving the difference (少數).

2. **少數再自乘，半之，以減立冪:**
   - Subtract half the square of the difference (少數) from the cube of the product to get the intermediate value (實).

3. **少數自乘，倍之，為方法:**
   - Compute the method (方法) by doubling the square of the difference (少數).

4. **置少數，五之，二而一，為廉法，從:**
   - Compute the auxiliary divisor (廉法) using the difference (少數).

5. **開立方除之，即句:**
   - Solve for the base (句) by taking the cube root of the ratio of 实 to 方法.

6. **加差，即弦:**
   - Add the difference (少數) to the base (句) to get the hypotenuse (弦).

7. **弦除冪，即股:**
   - Divide the product (冪) by the hypotenuse (弦) to get the perpendicular (股).

---

### Final Answer:
The perpendicular (股) is `a`. The exact value will be computed when the code is run.
"""


"""
Variable 'a' has wrong value. Expected: 68, Actual: 15.814148130526078"""
