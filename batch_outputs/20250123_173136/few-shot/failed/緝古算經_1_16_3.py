"""
假令有句弦相乘冪一千三百三十七二十分之一，弦多股一、十分之一。問：股多少？
術曰：冪自乘，倍多而一，為立冪。又多再自乘，半之，減立冪，余為實。又多數自乘，倍之，為方法。又置多數，五之，二而一，為廉法，從。開立方除之，即股。案：此術脫簡既多，法亦煩擾，宜雲冪自乘，多數而一，所得四之，為實。多為廉法，從。立方開之，得減差，半之，即股。
答曰： a 。
"""

"""
This is a complex ancient Chinese mathematical problem involving the Pythagorean theorem and cubic roots. Let's carefully translate the procedure into Python code step by step.

### Problem Description:
Suppose there is a right triangle where the product of the hypotenuse (弦) and the base (句) equals \( 1337 \frac{1}{20} \) (or \( 1337.05 \)). The hypotenuse exceeds the perpendicular (股) by \( 1 \frac{1}{10} \) (or \( 1.1 \)).  
Question: What is the length of the perpendicular (股)?

### Procedure:
The procedure involves a series of steps to calculate the perpendicular (股) using the given information. The steps include squaring, cubing, and extracting cube roots. The simplified procedure is used for efficiency.

---


"""


from fractions import Fraction

# Given values
冪 = Fraction(1337, 1) + Fraction(1, 20)  # 冪 (product of 弦 and 句)
多 = Fraction(1, 1) + Fraction(1, 10)    # 弦 exceeds 股 by 多 (1.1)

# Simplified procedure:
# 冪自乘，多數而一，所得四之，為實
實 = (冪 * 多) / 4

# 多為廉法，從
廉法 = 多

# 立方開之，得減差，半之，即股
股 = (實 / 廉法) ** (1/3) / 2

# Answer
a = 股


"""


### Explanation of the Code:
1. **冪自乘，多數而一，所得四之，為實**:
   - Multiply the given product \( 冪 \) by \( 多 \) (the difference between 弦 and 股).
   - Divide the result by 4 to get \( 實 \).

2. **多為廉法，從**:
   - Use \( 多 \) as the divisor (廉法).

3. **立方開之，得減差，半之，即股**:
   - Take the cube root of \( 實 / 廉法 \).
   - Halve the result to get \( 股 \).

### Final Answer:
The value of \( a \) is the length of the perpendicular (股).
"""


"""
Variable 'a' has wrong value. Expected: 462/5, Actual: 3.47002462423041"""
