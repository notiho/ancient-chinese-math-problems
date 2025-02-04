"""
假令圓囤上小下大，斛法二尺五寸，以率徑一周三。上下周差一丈二尺，高多上周一丈八尺，容粟七百五斛六斗。今已運出二百六十六石四斗。問：殘粟去口、上下周、高各多少？
答曰：上周 a丈 ，下周 b丈 ，高 c丈 ，去口 d丈 ，粟周 e丈 。
"""

"""
This problem involves a circular granary (圓囤) with a smaller top circumference and a larger bottom circumference. The problem provides the dimensions and volume of the granary, as well as the amount of grain already removed, and asks for the remaining dimensions and grain volume.

Let's break it down step by step and solve it in Python:

---

### Problem Breakdown:
1. **Given:**
   - The circumference of the top (上周) is smaller than the bottom (下周).
   - The difference between the top and bottom circumferences is 12 chi (一丈二尺 = 12 chi).
   - The height (高) is 18 chi more than the top circumference (高多上周一丈八尺 = 18 chi).
   - The granary can hold 705 dou 6 sheng of grain (容粟七百五斛六斗).
   - 266 shi 4 dou of grain has already been removed (已運出二百六十六石四斗).

2. **Find:**
   - Top circumference (上周, `a`).
   - Bottom circumference (下周, `b`).
   - Height (高, `c`).
   - Distance from the top to the remaining grain surface (去口, `d`).
   - Remaining grain volume (粟周, `e`).

3. **Conversion Factors:**
   - 1 斛 (hu) = 10 斗 (dou).
   - 1 石 (shi) = 10 斗 (dou).

4. **Formula for Volume of a Truncated Circular Cone:**
   The volume \( V \) of a truncated circular cone is given by:
   \[
   V = \frac{h}{3} \times \pi \times \left( r_1^2 + r_1 r_2 + r_2^2 \right)
   \]
   Where:
   - \( h \) is the height.
   - \( r_1 \) is the radius of the top.
   - \( r_2 \) is the radius of the bottom.

   Since the problem uses circumference instead of radius, we can substitute:
   \[
   r = \frac{\text{circumference}}{2\pi}
   \]
   And simplify the formula accordingly.

---

### Python Code:


"""


from fractions import Fraction

# Given values
total_volume_dou = 705 * 10 + 6  # Convert 705斛6斗 to total dou
removed_volume_dou = 266 * 10 + 4  # Convert 266石4斗 to total dou
remaining_volume_dou = total_volume_dou - removed_volume_dou  # Remaining grain volume in dou

circumference_difference = 12  # Difference between top and bottom circumferences in chi
height_difference = 18  # Height is 18 chi more than the top circumference

# Step 1: Solve for top circumference (a), bottom circumference (b), and height (c)
# Let top circumference = a
# Then bottom circumference = a + 12
# And height = a + 18

# Step 2: Use the volume formula for a truncated cone to solve for a
# Volume formula (simplified for circumference):
# V = (h / 12) * (a^2 + a * b + b^2)
# Where h = height, a = top circumference, b = bottom circumference

# Substitute b = a + 12 and h = a + 18 into the formula:
# V = ((a + 18) / 12) * (a^2 + a * (a + 12) + (a + 12)^2)

# Expand the formula:
# V = ((a + 18) / 12) * (a^2 + a^2 + 12a + a^2 + 24a + 144)
# V = ((a + 18) / 12) * (3a^2 + 36a + 144)
# V = (a + 18) * (a^2 + 12a + 48) / 4

# Set V equal to the total volume (in dou) and solve for a:
total_volume = Fraction(total_volume_dou)  # Use Fraction for precise calculations
a = 0  # Placeholder for top circumference (to be solved iteratively)

for possible_a in range(1, 100):  # Iterate over possible values of a (top circumference)
    b = possible_a + circumference_difference  # Bottom circumference
    h = possible_a + height_difference  # Height
    calculated_volume = Fraction(h) * (possible_a**2 + possible_a * b + b**2) / 12
    if calculated_volume == total_volume:
        a = possible_a
        break

# Step 3: Calculate remaining dimensions and grain volume
b = a + circumference_difference  # Bottom circumference
c = a + height_difference  # Height

# Remaining grain volume
remaining_height = 0  # Placeholder for remaining height (to be solved iteratively)
for possible_h in range(1, c + 1):  # Iterate over possible heights
    calculated_remaining_volume = Fraction(possible_h) * (a**2 + a * b + b**2) / 12
    if calculated_remaining_volume == remaining_volume_dou:
        remaining_height = possible_h
        break

d = c - remaining_height  # Distance from the top to the remaining grain surface
e = remaining_volume_dou / 10  # Convert remaining volume to hu

# Output results
print(f"Top circumference (上周, a): {a} 丈")
print(f"Bottom circumference (下周, b): {b} 丈")
print(f"Height (高, c): {c} 丈")
print(f"Distance to grain surface (去口, d): {d} 丈")
print(f"Remaining grain volume (粟周, e): {e} 斛")


"""


---

### Explanation of the Code:
1. **Step 1:** The formula for the volume of a truncated cone is simplified using the given relationships between the top circumference, bottom circumference, and height.
2. **Step 2:** The code iteratively solves for the top circumference (`a`) by checking which value satisfies the total volume equation.
3. **Step 3:** Once `a` is found, the remaining height (`d`) is calculated by iteratively solving for the remaining volume.
4. **Output:** The results are printed in terms of chi (丈) and hu (斛).

Let me know if you'd like further clarification!
"""


"""
Variable 'a' has wrong value. Expected: 9/5, Actual: 0
Variable 'b' has wrong value. Expected: 3, Actual: 12
Variable 'c' has wrong value. Expected: 18/5, Actual: 18
Variable 'd' has wrong value. Expected: 9/5, Actual: 18
Variable 'e' has wrong value. Expected: 12/5, Actual: 439.2"""
