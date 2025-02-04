"""
今有倉從一丈三尺廣六尺高一丈中有從牽二枚方五寸從一丈三尺又横牽三枚方四寸從六尺又柱一枚周三尺高一丈。問：受粟㡬何？
術曰：列從一丈三尺上十之得一百三十寸以廣六十寸乘之得七千八百寸又列高一丈上十之為一百寸以乘之得七十八萬寸為都積又列從牽二枚方五寸自相乘得二十五寸以從一百三十寸乘之得三千二百五十寸以從牽二枚乘之得六千五百寸又列横牽三枚方四寸自相乘得十六寸以從六十寸乘之得九百六十寸以横牽三枚乘之得二千八百八十寸又列柱一枚周三尺上十之得三十寸自相乘得九百寸以高一百寸乘之得九萬寸以十二除之得七千五百寸并從横牽及柱等三位得一萬六千八百八十寸以減都積餘七十六萬三千一百二十寸為實以斛法一千六百二十寸除之即得。
答曰： a斛 奇 b寸 。
"""

"""
This problem involves calculating the volume of a granary (倉) while subtracting the volumes of internal obstructions (牽 and 柱). The final result is expressed in *斛* (a unit of volume) and leftover *寸* (cubic inches).

### Problem Breakdown:
1. **Granary Dimensions**:
   - Length: 1 丈 3 尺 = 13 尺 = 130 寸
   - Width: 6 尺 = 60 寸
   - Height: 1 丈 = 10 尺 = 100 寸

2. **Obstructions**:
   - Two vertical beams (牽) with square cross-sections of 5 寸 × 5 寸.
   - Three horizontal beams (牽) with square cross-sections of 4 寸 × 4 寸.
   - One vertical pillar (柱) with a circular cross-section of 周 (circumference) = 3 尺 = 30 寸 and height = 1 丈 = 100 寸.

3. **Procedure**:
   - Calculate the total volume of the granary.
   - Subtract the volumes of the obstructions (vertical beams, horizontal beams, and the pillar).
   - Convert the remaining volume into *斛* and leftover *寸* using the conversion factor: 1 斛 = 1620 cubic 寸.

---

### Python Code Implementation:


"""

#----- content starts here -----

from fractions import Fraction
import math

# Granary dimensions (in 寸)
length = 130  # 1 丈 3 尺 = 13 尺 = 130 寸
width = 60    # 6 尺 = 60 寸
height = 100  # 1 丈 = 10 尺 = 100 寸

# Total volume of the granary
total_volume = length * width * height

# Obstruction 1: Two vertical beams (牽) with 5 寸 × 5 寸 cross-section
vertical_beam_cross_section = 5 * 5  # Cross-sectional area in 寸²
vertical_beam_volume = vertical_beam_cross_section * length * 2  # Two beams

# Obstruction 2: Three horizontal beams (牽) with 4 寸 × 4 寸 cross-section
horizontal_beam_cross_section = 4 * 4  # Cross-sectional area in 寸²
horizontal_beam_volume = horizontal_beam_cross_section * width * 3  # Three beams

# Obstruction 3: One vertical pillar (柱) with circular cross-section
pillar_radius = 30 / (2 * math.pi)  # Convert circumference to radius
pillar_cross_section = math.pi * (pillar_radius ** 2)  # Circular area in 寸²
pillar_volume = pillar_cross_section * height
pillar_volume = Fraction(pillar_volume).limit_denominator()  # Use fractions for precision
pillar_volume_adjusted = pillar_volume / 12  # Divide by 12 as per the problem

# Total obstruction volume
total_obstruction_volume = vertical_beam_volume + horizontal_beam_volume + pillar_volume_adjusted

# Remaining volume
remaining_volume = total_volume - total_obstruction_volume

# Conversion to 斛 and leftover 寸
hu_conversion_factor = 1620  # 1 斛 = 1620 cubic 寸
hu = remaining_volume // hu_conversion_factor  # Integer part (斛)
leftover_cun = remaining_volume % hu_conversion_factor  # Remainder (寸)

# Final answer
a = hu
b = leftover_cun

print(f"Answer: {a} 斛 and {b} 寸.")
#----- content ends here -----


"""


---

### Explanation of the Code:
1. **Granary Volume**:
   - The total volume of the granary is calculated as `length * width * height`.

2. **Obstruction Volumes**:
   - For the vertical and horizontal beams, the cross-sectional area is multiplied by the respective lengths and the number of beams.
   - For the pillar, the circumference is converted to radius, and the circular cross-sectional area is calculated using the formula \( \pi r^2 \). The volume is then divided by 12 as per the problem.

3. **Remaining Volume**:
   - The total obstruction volume is subtracted from the granary's total volume.

4. **Conversion to 斛 and 寸**:
   - The remaining volume is divided by 1620 to get the number of *斛* (integer part) and the leftover *寸* (remainder).

---

### Example Output:
If you run the code, it will compute the exact values for *a* (斛) and *b* (寸).
"""


"""
Variable 'a' has wrong value. Expected: 471, Actual: 475
Variable 'b' has wrong value. Expected: 100, Actual: 2540516857/4856016"""
