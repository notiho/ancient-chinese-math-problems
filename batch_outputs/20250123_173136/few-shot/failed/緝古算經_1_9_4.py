"""
假令有粟二萬三千一百二十斛七斗三升，欲作方倉一，圓窖一，盛各滿中而粟適盡。令高、深等，使方面少於圓徑九寸，多於高二丈九尺八寸，率徑七，周二十二。問：方、徑、深多少？
求方、徑高深，術曰：十四乘斛法，以乘粟數，二十五而一，為實。又倍多加少，以乘少數，又十一乘之，二十五而一，多自乘加之，為方法。又倍少數，十一乘之，二十五而一，又倍多加之，為廉法，從。開立方除之，即高、深。各加差，即方徑。還元，術曰：倉方自乘，以高乘之，為實。圓徑自乘，以深乘之，一十一乘，一十四而一，為實。皆為斛法除之，即得容粟。
答曰：倉方 a丈 ，窖徑 b丈 ，高與深各 c丈 。
"""

"""
This is a complex ancient Chinese mathematical problem involving the calculation of dimensions for a square granary and a circular pit to hold a given amount of grain. Let's translate the procedure into Python step by step.

### Problem Breakdown:
- The total amount of grain is given as 23120 hu, 7 dou, and 3 sheng.
- The square granary's side length is less than the circular pit's diameter by 9 cun.
- The square granary's side length is greater than its height by 2 zhang, 9 chi, and 8 cun.
- The relationship between the circumference and diameter of the circle is given as 22:7.
- The goal is to calculate the side length of the square granary (`a`), the diameter of the circular pit (`b`), and the height/depth (`c`).

### Procedure:
The procedure involves several steps, including calculating the dimensions using the given relationships and verifying the results by calculating the volume of the granary and pit.

Here is the Python implementation:


"""


from fractions import Fraction
from math import pow

# 粟二萬三千一百二十斛七斗三升
粟數 = 23120 + Fraction(7, 10) + Fraction(3, 100)

# 斛法
斛法 = 14

# 率徑七，周二十二
圓率 = Fraction(22, 7)

# 方倉少於圓徑九寸
少數 = Fraction(9, 10)

# 方倉多於高二丈九尺八寸
多數 = 2 * 10 + 9 + Fraction(8, 10)

# Step 1: Calculate the 实 (volume-related value)
實 = Fraction(14, 1) * 粟數 * Fraction(1, 25)

# Step 2: Calculate the 方方法 (square granary method)
方法 = (2 * 多數 + 少數) * 少數 * Fraction(11, 1) * Fraction(1, 25) + pow(多數, 2)

# Step 3: Calculate the 廉法 (circular pit method)
廉法 = (2 * 少數 * Fraction(11, 1) * Fraction(1, 25)) + (2 * 多數 + 少數)

# Step 4: Solve for 高/深 (height/depth)
高深 = pow(Fraction(實, 廉法), Fraction(1, 3))

# Step 5: Calculate 方 and 徑 (side length and diameter)
方 = 高深 + 多數
徑 = 高深 + 少數

# Step 6: Verify the results
# Square granary volume
方倉容積 = 方**2 * 高深

# Circular pit volume
圓窖容積 = (徑**2 * 高深 * Fraction(11, 1)) * Fraction(1, 14)

# Convert volumes to hu
方倉容積_斛 = 方倉容積 / 斛法
圓窖容積_斛 = 圓窖容積 / 斛法

# Ensure the total volume matches the given 粟數
assert abs(方倉容積_斛 + 圓窖容積_斛 - 粟數) < 1e-6, "Volumes do not match!"

# Final results
a = 方
b = 徑
c = 高深

print(f"倉方 a丈: {a}")
print(f"窖徑 b丈: {b}")
print(f"高與深各 c丈: {c}")


"""


### Explanation of the Code:
1. **Input Conversion**: The total grain amount is converted into a fractional value to handle the mixed units (hu, dou, sheng).
2. **Volume Calculation**: The procedure calculates the volume-related values (`實`, `方法`, `廉法`) based on the relationships provided.
3. **Dimension Calculation**: Using the calculated values, the height/depth (`c`), side length (`a`), and diameter (`b`) are determined.
4. **Verification**: The calculated dimensions are verified by computing the volumes of the square granary and circular pit and ensuring they match the total grain amount.

### Output:
The program will output the side length of the square granary (`a`), the diameter of the circular pit (`b`), and the height/depth (`c`) in zhang.
"""


"""
Code error: Volumes do not match!"""
