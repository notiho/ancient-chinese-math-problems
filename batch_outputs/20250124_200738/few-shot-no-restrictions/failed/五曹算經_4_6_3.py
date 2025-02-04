"""
今有倉從一丈三尺廣六尺高一丈中有從牽二枚方五寸從一丈三尺又横牽三枚方四寸從六尺又柱一枚周三尺高一丈。問：受粟㡬何？
術曰：列從一丈三尺上十之得一百三十寸以廣六十寸乘之得七千八百寸又列高一丈上十之為一百寸以乘之得七十八萬寸為都積又列從牽二枚方五寸自相乘得二十五寸以從一百三十寸乘之得三千二百五十寸以從牽二枚乘之得六千五百寸又列横牽三枚方四寸自相乘得十六寸以從六十寸乘之得九百六十寸以横牽三枚乘之得二千八百八十寸又列柱一枚周三尺上十之得三十寸自相乘得九百寸以高一百寸乘之得九萬寸以十二除之得七千五百寸并從横牽及柱等三位得一萬六千八百八十寸以減都積餘七十六萬三千一百二十寸為實以斛法一千六百二十寸除之即得。
答曰： a斛 奇 b寸 。
"""

"""
This problem involves calculating the volume of a granary while subtracting the volumes of internal structures (beams, posts, etc.) and then converting the remaining volume into a measurement of grain storage capacity.

### Problem Breakdown:
1. **Granary Dimensions**:
   - Length: 1丈3尺 = 13尺 = 130寸 (1丈 = 10尺, 1尺 = 10寸)
   - Width: 6尺 = 60寸
   - Height: 1丈 = 10尺 = 100寸

2. **Internal Structures**:
   - Two vertical beams (牽) with a square cross-section of 5寸 × 5寸.
   - Three horizontal beams (牽) with a square cross-section of 4寸 × 4寸.
   - One pillar (柱) with a circular cross-section of 周3尺 (circumference = 30寸) and height = 1丈 = 100寸.

3. **Granary Volume**:
   - Compute the total volume of the granary.
   - Subtract the volumes of the internal structures.

4. **Grain Storage Capacity**:
   - Use the conversion factor: 1斛 = 1620寸³.

---

### Python Code Implementation:


"""

#----- content starts here -----

from fractions import Fraction
import math

# Granary dimensions (in 寸)
length = 130  # 1丈3尺 = 130寸
width = 60    # 6尺 = 60寸
height = 100  # 1丈 = 100寸

# Total granary volume
granary_volume = length * width * height

# Internal structures
# 1. Two vertical beams (牽)
beam_square_side = 5  # 5寸 × 5寸
beam_volume = (beam_square_side ** 2) * length * 2  # Two beams

# 2. Three horizontal beams (牽)
horizontal_beam_square_side = 4  # 4寸 × 4寸
horizontal_beam_volume = (horizontal_beam_square_side ** 2) * width * 3  # Three beams

# 3. One pillar (柱)
pillar_circumference = 30  # 周3尺 = 30寸
pillar_radius = pillar_circumference / (2 * math.pi)  # r = C / (2π)
pillar_volume = math.pi * (pillar_radius ** 2) * height  # Volume of a cylinder
pillar_volume = Fraction(pillar_volume).limit_denominator()  # Convert to fraction
pillar_volume = pillar_volume / 12  # Divide by 12 as per the problem

# Total internal structure volume
internal_volume = beam_volume + horizontal_beam_volume + pillar_volume

# Remaining volume for grain
remaining_volume = granary_volume - internal_volume

# Grain storage capacity
grain_capacity = remaining_volume / 1620  # 1斛 = 1620寸³
a = grain_capacity.numerator // grain_capacity.denominator  # Integer part (斛)
b = grain_capacity.numerator % grain_capacity.denominator  # Remainder (寸)

# Output
print(f"答曰：{a}斛 奇 {b}寸。")
#----- content ends here -----


"""


---

### Explanation of the Code:
1. **Granary Volume**:
   - The total volume of the granary is calculated as `length × width × height`.

2. **Internal Structures**:
   - The volume of the two vertical beams is calculated as `side² × length × 2`.
   - The volume of the three horizontal beams is calculated as `side² × width × 3`.
   - The volume of the pillar is calculated using the formula for the volume of a cylinder: `πr²h`, where `r` is derived from the circumference. The result is divided by 12 as per the problem.

3. **Remaining Volume**:
   - The total volume of the internal structures is subtracted from the granary volume to get the remaining volume.

4. **Grain Storage Capacity**:
   - The remaining volume is divided by 1620 to convert it into the unit of 斛. The integer part represents the number of 斛, and the remainder represents the leftover volume in 寸³.

---

### Example Output:
If you run the code, it will calculate the exact values of `a` (number of 斛) and `b` (remaining 寸³).
"""


"""
Variable 'a' has wrong value. Expected: 471, Actual: 475
Variable 'b' has wrong value. Expected: 100, Actual: 2540516857"""
