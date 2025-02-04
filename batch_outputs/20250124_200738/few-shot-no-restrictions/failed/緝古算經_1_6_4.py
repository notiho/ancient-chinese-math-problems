"""
假令亭倉上小下大，上下方差六尺，高多上方九尺，容粟一百八十七石二斗。今已運出五十石四斗。問：倉上下方、高及余粟深、上方各多少？
求倉方、高，術曰：以斛法乘容粟，為積尺。又方差自乘，三而一，為隅陽冪。以乘截高，以減積，余為實。又方差乘截高，加隅陽冪，為方法。又置方差，加截高，為廉法，從。開立方除之，即上方。加差，即合所問。求余粟高及上方，術曰：以斛法乘出粟，三之，以乘高冪，令方差冪而一，為實。高乘上方，方差而一，為小高。令自乘，三之，為方法。三因小高，為廉法，從。開立方除之，得取出高。以減本高，余即殘粟高。置出粟高，又以方差乘之，以本高除之，所得加上方，即余粟上方。
答曰：上方 a尺 ，下方 b尺 ，高 c丈 ；余粟深上方俱 d尺 。
"""

"""
This is a classic ancient Chinese problem involving a frustum-shaped granary (a truncated pyramid). The problem involves calculating the dimensions of the granary (top side, bottom side, and height) and the remaining depth and top side of the granary after some grain has been removed. Let's break it down step by step and encode it in Python.

---

### Problem Breakdown:
1. **Given:**
   - Top side is smaller than the bottom side by 6 chi (方差 = 6).
   - Height is 9 chi more than the top side (高多上方 = 9).
   - Total volume of grain = 187 石 2 斗 = \( 187 + \frac{2}{10} \) 石.
   - Grain removed = 50 石 4 斗 = \( 50 + \frac{4}{10} \) 石.

2. **To Find:**
   - Top side (上方, \( a \)).
   - Bottom side (下方, \( b \)).
   - Height (高, \( c \)).
   - Remaining grain depth and top side after removal (余粟深, 上方).

3. **Procedure:**
   - Use the formula for the volume of a frustum:
     \[
     V = \frac{h}{3} \times (A_1 + A_2 + \sqrt{A_1 \times A_2})
     \]
     where \( A_1 \) is the area of the top square, \( A_2 \) is the area of the bottom square, and \( h \) is the height.
   - Solve for the unknowns step by step.

---

### Python Code:


"""

#----- content starts here -----

from fractions import Fraction
from sympy import symbols, solve, Eq

# Given values
方差 = 6  # Top side is smaller than bottom side by 6 chi
高多上方 = 9  # Height is 9 chi more than the top side
容粟 = Fraction(187, 1) + Fraction(2, 10)  # Total volume in 石
出粟 = Fraction(50, 1) + Fraction(4, 10)  # Grain removed in 石
斛法 = 10  # Conversion factor: 1 石 = 10 cubic chi

# Step 1: Convert volume to cubic chi
容粟積 = 容粟 * 斛法  # Total volume in cubic chi
出粟積 = 出粟 * 斛法  # Removed volume in cubic chi

# Step 2: Define variables
上方, 下方, 高 = symbols('上方 下方 高')

# Step 3: Solve for 上方, 下方, 高
# 方差 = 下方 - 上方
# 高 = 上方 + 高多上方
# Volume formula: 容粟積 = 高 / 3 * (上方**2 + 下方**2 + 上方 * 下方)
方差_eq = Eq(下方 - 上方, 方差)
高_eq = Eq(高, 上方 + 高多上方)
volume_eq = Eq(容粟積, 高 / 3 * (上方**2 + 下方**2 + 上方 * 下方))

# Solve the system of equations
solution = solve([方差_eq, 高_eq, volume_eq], [上方, 下方, 高])
上方_val = solution[0][0]
下方_val = solution[0][1]
高_val = solution[0][2]

# Step 4: Calculate remaining grain depth and top side
# Remaining volume = 容粟積 - 出粟積
余粟積 = 容粟積 - 出粟積

# Use the same volume formula to solve for remaining depth (余粟深) and top side (余粟上方)
余粟深 = symbols('余粟深')
remaining_volume_eq = Eq(余粟積, 余粟深 / 3 * (上方_val**2 + 下方_val**2 + 上方_val * 下方_val))

# Solve for 余粟深
余粟深_val = solve(remaining_volume_eq, 余粟深)[0]

# Calculate the new top side (余粟上方)
余粟上方 = 上方_val + (余粟深_val * 方差 / 高_val)

# Final results
a = 上方_val
b = 下方_val
c = 高_val / 10  # Convert 高 to 丈 (1 丈 = 10 chi)
d = 余粟深_val

print(f"上方 a = {a} 尺")
print(f"下方 b = {b} 尺")
print(f"高 c = {c} 丈")
print(f"余粟深及上方 d = {d} 尺")
#----- content ends here -----


"""


---

### Explanation of the Code:
1. **Volume Conversion:** Convert the given grain volumes from 石 to cubic chi using the conversion factor \( 1 石 = 10 \, \text{cubic chi} \).
2. **Equations Setup:**
   - Use the relationships between top side, bottom side, and height.
   - Use the frustum volume formula to relate the dimensions to the total volume.
3. **Solve for Dimensions:** Solve the system of equations to find the top side, bottom side, and height.
4. **Remaining Grain Depth:** Subtract the removed volume from the total volume and solve for the remaining depth and top side using the same frustum formula.

---

### Final Output:
The program will output the following:
- Top side (\( a \)) in chi.
- Bottom side (\( b \)) in chi.
- Height (\( c \)) in zhang.
- Remaining depth and top side (\( d \)) in chi.
"""


"""
Variable 'a' has wrong value. Expected: 3, Actual: ((3 - 5*(sqrt(850057) + 922)**(1/3))*(sqrt(850057) + 922)**(1/3) + sqrt(850057) + 922)/(sqrt(850057) + 922)**(2/3)
Variable 'b' has wrong value. Expected: 9, Actual: ((3 + (sqrt(850057) + 922)**(1/3))*(sqrt(850057) + 922)**(1/3) + sqrt(850057) + 922)/(sqrt(850057) + 922)**(2/3)
Variable 'c' has wrong value. Expected: 6/5, Actual: 3/(10*(sqrt(850057) + 922)**(1/3)) + 2/5 + (sqrt(850057) + 922)**(1/3)/10
Variable 'd' has wrong value. Expected: 6, Actual: 1368*(sqrt(850057) + 922)**(4/3)/(-4*sqrt(850057)*(sqrt(850057) + 922)**(2/3) - 3679*(sqrt(850057) + 922)**(2/3) + 13*sqrt(850057)*(sqrt(850057) + 922)**(1/3) + 11986*(sqrt(850057) + 922)**(1/3) + 1689077 + 1832*sqrt(850057))"""
