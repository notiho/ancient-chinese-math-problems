"""
假令有粟三千七十二石，欲作方倉一、圓窖一，令徑與方等，方於窖深二尺，少於倉高三尺，盛各滿中而粟適盡。問：方、徑、高、深各多少？
術曰：三十五乘粟，二十五而一，為率。多自乘，以並多少乘之，以乘一十四，如二十五而一，所得以減率，余為實。並多少，以乘多，倍之，乘一十四，如二十五而一，多自乘加之，為方法。又並多少，以乘一十四，如二十五而一，加多加之，為廉法，從。開立方除之，即窖深。各加差，即方、徑、高。
答曰：方徑各 a丈 ，高 b丈 ，深 c丈 。
"""

"""
This is a complex ancient Chinese mathematical problem involving the calculation of dimensions for a square granary and a circular pit based on the volume of grain. Let's break it down step by step and translate the procedure into Python code.

### Problem Description:
There are 3072 shi of grain. A square granary and a circular pit are to be constructed such that:
- The diameter of the circular pit equals the side length of the square granary.
- The depth of the circular pit is 2 chi deeper than the height of the square granary.
- The height of the square granary is 3 chi shorter than the side length of the square granary.
- Both the granary and the pit are filled completely, and the total volume equals the grain volume.

The task is to calculate the side length of the square granary (`方`), the diameter of the circular pit (`徑`), the height of the square granary (`高`), and the depth of the circular pit (`深`).

---

### Procedure:
The procedure involves several steps using ancient Chinese mathematical methods. Here's the breakdown:

1. **Calculate the rate (`率`)**:
   - Multiply the grain volume by 35.
   - Divide by 25.

2. **Calculate the "real" (`實`)**:
   - Multiply the "more" (`多`, which is the difference between the granary side length and height) by itself.
   - Multiply this by the "combined difference" (`並多少`, which is the sum of the differences between the granary and pit dimensions).
   - Multiply by 14.
   - Divide by 25.
   - Subtract this from the rate to get the "real."

3. **Calculate the "method for the square granary" (`方法`)**:
   - Multiply the "combined difference" by the "more."
   - Double this value.
   - Multiply by 14.
   - Divide by 25.
   - Add the square of the "more."

4. **Calculate the "method for the circular pit" (`廉法`)**:
   - Multiply the "combined difference" by 14.
   - Divide by 25.
   - Add the "more."

5. **Solve for the depth of the circular pit (`深`)**:
   - Take the cube root of the "real" divided by the "method for the circular pit."

6. **Calculate the other dimensions**:
   - Add the differences to the depth to get the side length, diameter, and height.

---

### Python Code:


"""


from fractions import Fraction
from math import pow

# 粟三千七十二石
粟 = 3072

# 固定常數
三十五 = 35
二十五 = 25
一十四 = 14

# 差異
多 = Fraction(3, 10)  # Granary side length is 3 chi more than its height (3 chi = 3/10 zhang)
並多少 = Fraction(5, 10)  # Combined difference (2 chi + 3 chi = 5 chi = 5/10 zhang)

# Step 1: Calculate the rate (率)
率 = Fraction(三十五 * 粟, 二十五)

# Step 2: Calculate the "real" (實)
實 = 率 - Fraction(多 * 多 * 並多少 * 一十四, 二十五)

# Step 3: Calculate the "method for the square granary" (方法)
方法 = Fraction(並多少 * 多 * 2 * 一十四, 二十五) + 多 * 多

# Step 4: Calculate the "method for the circular pit" (廉法)
廉法 = Fraction(並多少 * 一十四, 二十五) + 多

# Step 5: Solve for the depth of the circular pit (深)
深 = pow(Fraction(實, 廉法), Fraction(1, 3))

# Step 6: Calculate the other dimensions
方 = 深 + 多
徑 = 方  # Diameter equals the side length of the square granary
高 = 深 - Fraction(2, 10)  # Granary height is 2 chi (2/10 zhang) less than the depth

# Convert results to simplified fractions
a = 方
b = 高
c = 深

# Output the results
a, b, c


"""


---

### Explanation of Results:
- `a`: Side length of the square granary and diameter of the circular pit (in zhang).
- `b`: Height of the square granary (in zhang).
- `c`: Depth of the circular pit (in zhang).

This code follows the ancient procedure step by step and uses `Fraction` to ensure precision in calculations.
"""


"""
Variable 'a' has wrong value. Expected: 8/5, Actual: 19.800222627760494
Variable 'b' has wrong value. Expected: 19/10, Actual: 19.300222627760494
Variable 'c' has wrong value. Expected: 7/5, Actual: 19.500222627760493"""
