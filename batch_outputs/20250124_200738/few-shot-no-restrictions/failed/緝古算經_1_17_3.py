"""
假令有股弦相乘冪四千七百三十九五分之三，句少於弦五十四五分之二。問：股多少？
術曰：冪自乘，倍少數而一，為立冪。又少數再自乘，半之，以減立冪，余為實。又少數自乘，倍之，為方法。又置少數，五之，二而一，為廉法，從。開立方除之，即句。加差，即弦。弦除冪，即股。
答曰： a 。
"""

"""
This is a classic problem involving the Pythagorean theorem and cubic equations. Let's break it down step by step and encode the procedure in Python.

### Problem Breakdown:
1. **Given:**
   - The product of the two sides (leg and hypotenuse) is \( 4739 \frac{3}{5} \) (or \( \frac{23698}{5} \)).
   - The difference between the hypotenuse and the other leg is \( 54 \frac{2}{5} \) (or \( \frac{272}{5} \)).

2. **Question:**
   - Find the length of the other leg (股, "gu").

3. **Procedure:**
   - Compute the cube of the product (冪自乘, "mi self-multiplied").
   - Multiply the difference by 2 and add 1 (倍少數而一, "double the difference and add 1") to form the cubic power (立冪, "cubic power").
   - Subtract half the square of the difference (少數再自乘，半之, "difference squared, halved") from the cubic power to get the remainder (余, "remainder").
   - Multiply the square of the difference by 2 (少數自乘，倍之, "difference squared, doubled") to form the divisor (方法, "method divisor").
   - Divide the remainder by the divisor to find the shorter leg (句, "ju").
   - Add the difference to the shorter leg to find the hypotenuse (弦, "xian").
   - Divide the product by the hypotenuse to find the other leg (股, "gu").

---

### Python Code:


"""

#----- content starts here -----

from fractions import Fraction

# Given values
冪 = Fraction(4739, 5)  # Product of the two sides
少數 = Fraction(272, 5)  # Difference between hypotenuse and shorter leg

# 冪自乘 (cube of the product)
冪自乘 = 冪 ** 3

# 倍少數而一 (double the difference and add 1)
倍少數而一 = 2 * 少數 + 1

# 立冪 (cubic power)
立冪 = 冪自乘 * 倍少數而一

# 少數再自乘，半之 (square of the difference, halved)
少數平方半 = (少數 ** 2) / 2

# 余 (remainder)
余 = 立冪 - 少數平方半

# 少數自乘，倍之 (square of the difference, doubled)
方法 = 2 * (少數 ** 2)

# 句 (shorter leg)
句 = 余 / 方法

# 弦 (hypotenuse)
弦 = 句 + 少數

# 股 (other leg)
股 = 冪 / 弦

# Final answer
a = 股
print(f"股 (other leg) = {a}")
#----- content ends here -----


"""


---

### Explanation of Variables:
- `冪` represents the product of the two sides.
- `少數` represents the difference between the hypotenuse and the shorter leg.
- `冪自乘` is the cube of the product.
- `倍少數而一` is the doubled difference plus 1.
- `立冪` is the cubic power.
- `少數平方半` is half the square of the difference.
- `余` is the remainder after subtracting `少數平方半` from `立冪`.
- `方法` is the divisor formed by doubling the square of the difference.
- `句` is the shorter leg.
- `弦` is the hypotenuse.
- `股` is the other leg.

---

### Example Output:
If you run the code, it will compute the length of the other leg (`股`) based on the given values.
"""


"""
Variable 'a' has wrong value. Expected: 68, Actual: 3506101760/58429740756711"""
