"""
假令有句弦相乘冪一千三百三十七二十分之一，弦多股一、十分之一。問：股多少？
術曰：冪自乘，倍多而一，為立冪。又多再自乘，半之，減立冪，余為實。又多數自乘，倍之，為方法。又置多數，五之，二而一，為廉法，從。開立方除之，即股。案：此術脫簡既多，法亦煩擾，宜雲冪自乘，多數而一，所得四之，為實。多為廉法，從。立方開之，得減差，半之，即股。
答曰： a 。
"""

"""
This is a complex ancient Chinese mathematical problem involving the Pythagorean theorem and cubic roots. Let's break it down step by step and translate it into Python code.

### Problem Explanation:
We are given:
- The product of the hypotenuse (弦) and the base (句), called the "power" (冪), is \( 1337 \frac{1}{20} \).
- The hypotenuse (弦) exceeds the perpendicular (股) by \( 1 \frac{1}{10} \).

We are tasked to find the length of the perpendicular (股).

### Procedure:
The procedure involves several steps, but the simplified version is:
1. Multiply the power (冪) by the excess (多數, the difference between the hypotenuse and the perpendicular), then divide by 4 to get the "actual value" (實).
2. Use the excess (多數) as the divisor (廉法).
3. Extract the cube root of the result to find the difference (減差).
4. Halve the difference to get the perpendicular (股).

### Python Code:


"""

#----- content starts here -----

from fractions import Fraction
from math import pow

# 冪 (power): 1337 1/20
冪 = Fraction(1337) + Fraction(1, 20)

# 多數 (excess): 1 1/10
多數 = Fraction(1) + Fraction(1, 10)

# Step 1: 冪自乘，多數而一，所得四之，為實
實 = (冪 * 多數) / 4

# Step 2: 多數為廉法
廉法 = 多數

# Step 3: 開立方 (cube root) of (實 / 廉法)
減差 = pow(float(實 / 廉法), 1/3)

# Step 4: 半之，即股
股 = Fraction(減差) / 2

# Answer
a = 股
print(f"股 = {a}")
#----- content ends here -----


"""


### Explanation of the Code:
1. **冪自乘，多數而一，所得四之，為實**:
   - Multiply the power (冪) by the excess (多數), then divide by 4 to get the "actual value" (實).

2. **多數為廉法**:
   - Use the excess (多數) as the divisor (廉法).

3. **開立方**:
   - Extract the cube root of the result from dividing the actual value (實) by the divisor (廉法).

4. **半之，即股**:
   - Halve the cube root to get the perpendicular (股).

### Final Answer:
The value of \( a \) (the perpendicular, 股) will be printed as a fraction.
"""


"""
Variable 'a' has wrong value. Expected: 462/5, Actual: 1953450200581315/562949953421312"""
