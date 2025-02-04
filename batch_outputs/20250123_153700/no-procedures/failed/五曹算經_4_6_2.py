"""
今有倉從一丈三尺廣六尺高一丈中有從牽二枚方五寸從一丈三尺又横牽三枚方四寸從六尺又柱一枚周三尺高一丈。問：受粟㡬何？
答曰： a斛 奇 b寸 。
"""

"""
This problem involves calculating the volume of a granary (倉) with specific dimensions, while accounting for the space occupied by beams (牽) and a pillar (柱). The goal is to determine how much grain (粟) the granary can hold.

### Problem Breakdown:
1. **Granary dimensions**:
   - Length (從): 1 丈 3 尺 = 13 尺
   - Width (廣): 6 尺
   - Height (高): 1 丈 = 10 尺

2. **Beams (牽)**:
   - Two beams along the length, each with a square cross-section of 5 寸 × 5 寸.
   - Three beams along the width, each with a square cross-section of 4 寸 × 4 寸.

3. **Pillar (柱)**:
   - One pillar with a circular cross-section of 周 (circumference) 3 尺 and height 1 丈 (10 尺).

4. **Volume of grain (粟)**:
   - The total volume of the granary minus the volume occupied by the beams and the pillar.
   - 1 cubic 尺 = 1 斛 (unit of grain).

---

### Solution in Python:


"""


from fractions import Fraction
import math

# Granary dimensions
length = 13  # 尺
width = 6    # 尺
height = 10  # 尺

# Total volume of the granary
total_volume = length * width * height  # in cubic 尺

# Beams along the length
beam_length_count = 2
beam_length_cross_section = Fraction(5, 10) ** 2  # 5 寸 = 5/10 尺
beam_length_volume = beam_length_count * beam_length_cross_section * length

# Beams along the width
beam_width_count = 3
beam_width_cross_section = Fraction(4, 10) ** 2  # 4 寸 = 4/10 尺
beam_width_volume = beam_width_count * beam_width_cross_section * width

# Pillar
pillar_circumference = 3  # 尺
pillar_radius = pillar_circumference / (2 * math.pi)  # r = C / (2π)
pillar_cross_section = math.pi * (pillar_radius ** 2)
pillar_height = 10  # 尺
pillar_volume = pillar_cross_section * pillar_height

# Total occupied volume
occupied_volume = beam_length_volume + beam_width_volume + pillar_volume

# Usable volume for grain
usable_volume = total_volume - occupied_volume

# Convert usable volume into 斛 and 寸
a = int(usable_volume)  # Whole 斛
b = Fraction(usable_volume - a).limit_denominator(10) * 10  # Remaining fraction in 寸

# Output the result
a, b


"""


---

### Explanation of the Code:
1. **Granary Volume**:
   - The total volume of the granary is calculated as `length × width × height`.

2. **Beams**:
   - The volume of each beam is calculated based on its cross-sectional area and length.
   - The cross-sectional dimensions are converted from 寸 to 尺 (1 尺 = 10 寸).

3. **Pillar**:
   - The pillar is treated as a cylinder. Its radius is derived from its circumference using the formula \( r = \frac{C}{2\pi} \).
   - The cross-sectional area is \( \pi r^2 \), and the volume is the cross-sectional area multiplied by the height.

4. **Usable Volume**:
   - The total occupied volume (beams + pillar) is subtracted from the granary's total volume to get the usable volume for grain.

5. **Conversion to 斛 and 寸**:
   - The usable volume is converted into whole 斛 (integer part) and remaining 寸 (fractional part, converted to tenths).

---

### Final Answer:
The result will be in the form:
- `a` 斛 (whole units of grain)
- `b` 寸 (fractional units of grain in tenths).
"""


"""
Variable 'a' has wrong value. Expected: 471, Actual: 763
Variable 'b' has wrong value. Expected: 100, Actual: 40/9"""
