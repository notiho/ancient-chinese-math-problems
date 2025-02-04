"""
假令有粟一萬六千三百四十八石八斗，欲作方倉四、圓窖三，令高、深等，方面少於圓徑一丈，多於高五尺，斛法二尺五寸，率徑七，周二十二。問：方、高、徑多少？
術曰：以一十四乘斛法，以乘粟數，如八十九而一，為實。倍多加少，以乘少數，三十三乘之，八十九而一，多自乘加之，為方法。又倍少數，以三十三乘之，八十九而一，倍多加之，為廉法，從。開立方除之，即高、深。各加差，即方徑。
答曰：方 a丈 ，高深 b丈 ，圓徑 c丈 。
"""

"""
This is a complex ancient Chinese mathematical problem involving the calculation of dimensions for a square granary and a circular pit based on the given volume of grain. Let's break it down step by step and translate the procedure into Python code.

### Problem Explanation:
- There is a total of 16,348 **shi** and 8 **dou** of grain.
- A square granary and a circular pit are to be constructed, with equal height/depth.
- The side of the square granary is 1 **zhang** less than the diameter of the circular pit and 5 **chi** more than the height/depth.
- The **hu** (volume unit) is defined as 2 **chi** 5 **cun** (2.5 **chi**).
- The ratio of the circumference to the diameter of a circle is given as 22:7.
- The task is to calculate the side length of the square granary, the height/depth, and the diameter of the circular pit.

### Procedure:
1. Multiply 14 by the **hu** (volume unit) and then multiply by the total grain volume. Divide by 89 to get the "real volume."
2. Double the "more" value (5 **chi**) and add the "less" value (1 **zhang**) to get the "less multiplier." Multiply this by the "less" value, then multiply by 33 and divide by 89. Add the square of the "less" value to get the "square method."
3. Double the "less" value and multiply by 33, then divide by 89. Add twice the "more" value to get the "edge method."
4. Solve for the height/depth by taking the cube root of the "real volume" divided by the "square method."
5. Add the "more" value to the height/depth to get the side length of the square granary.
6. Add the "less" value to the height/depth to get the diameter of the circular pit.

### Python Code:

"""


from fractions import Fraction
from math import pow

# 粟一萬六千三百四十八石八斗
粟石 = 16348
粟斗 = 8
粟總數 = 粟石 * 10 + 粟斗  # Convert to dou (1 shi = 10 dou)

# 斛法二尺五寸
斛法 = Fraction(25, 10)  # 2 chi 5 cun = 2.5 chi

# 率徑七，周二十二
圓率 = Fraction(22, 7)

# 方圓差值
多 = Fraction(5, 10)  # 5 chi = 0.5 zhang
少 = 1  # 1 zhang

# Step 1: Calculate the "real volume"
實 = Fraction(14) * 斛法 * 粟總數 / 89

# Step 2: Calculate the "square method" (方法)
倍多 = 2 * 多
倍少 = 2 * 少
少數 = 少
多數 = 多

方法 = (33 * 倍多 + 倍少) * 少數 / 89 + 少數**2

# Step 3: Calculate the "edge method" (廉法)
廉法 = (33 * 倍少 / 89) + 2 * 倍多

# Step 4: Solve for height/depth (高深)
高深 = pow(float(實 / 方法), 1/3)  # Cube root of (實 / 方法)

# Step 5: Calculate the side length of the square granary (方)
方 = 高深 + 多

# Step 6: Calculate the diameter of the circular pit (圓徑)
圓徑 = 高深 + 少

# Convert results to fractions for precision
高深 = Fraction(round(高深, 6)).limit_denominator()
方 = Fraction(round(方, 6)).limit_denominator()
圓徑 = Fraction(round(圓徑, 6)).limit_denominator()

# Output results
a = 方
b = 高深
c = 圓徑

print(f"方 {a}丈 ，高深 {b}丈 ，圓徑 {c}丈 。")


"""


### Explanation of Variables:
- `粟總數`: Total grain volume in **dou**.
- `斛法`: Volume of one **hu** in **chi**.
- `多`: The "more" value (5 **chi** = 0.5 **zhang**).
- `少`: The "less" value (1 **zhang**).
- `實`: The "real volume" derived from the grain volume.
- `方法`: The "square method" used to calculate the height/depth.
- `廉法`: The "edge method" used to calculate the height/depth.
- `高深`: The height/depth of both the square granary and the circular pit.
- `方`: The side length of the square granary.
- `圓徑`: The diameter of the circular pit.

### Final Output:
The code calculates the side length of the square granary (`a`), the height/depth (`b`), and the diameter of the circular pit (`c`) in **zhang**.
"""


"""
Variable 'a' has wrong value. Expected: 9/5, Actual: 4546037/125000
Variable 'b' has wrong value. Expected: 13/10, Actual: 4483537/125000
Variable 'c' has wrong value. Expected: 14/5, Actual: 4608537/125000"""
