"""
今有倉從一丈三尺廣六尺高一丈中有從牽二枚方五寸從一丈三尺又横牽三枚方四寸從六尺又柱一枚周三尺高一丈。問：受粟㡬何？
術曰：列從一丈三尺上十之得一百三十寸以廣六十寸乘之得七千八百寸又列高一丈上十之為一百寸以乘之得七十八萬寸為都積又列從牽二枚方五寸自相乘得二十五寸以從一百三十寸乘之得三千二百五十寸以從牽二枚乘之得六千五百寸又列横牽三枚方四寸自相乘得十六寸以從六十寸乘之得九百六十寸以横牽三枚乘之得二千八百八十寸又列柱一枚周三尺上十之得三十寸自相乘得九百寸以高一百寸乘之得九萬寸以十二除之得七千五百寸并從横牽及柱等三位得一萬六千八百八十寸以減都積餘七十六萬三千一百二十寸為實以斛法一千六百二十寸除之即得。
答曰： a斛 奇 b寸 。
"""

"""
This problem involves calculating the volume of a granary while accounting for the space taken up by internal structures (beams and a pillar). The final result is the capacity of the granary in terms of *hu* (a unit of volume) and leftover *cun* (cubic inches). Let's translate the procedure into Python code.

---

### Problem Breakdown:
1. **Granary dimensions**:
   - Length: 1 zhang 3 chi = 13 chi = 130 cun.
   - Width: 6 chi = 60 cun.
   - Height: 1 zhang = 10 chi = 100 cun.

2. **Internal structures**:
   - Two vertical beams, each with a square cross-section of 5 cun × 5 cun.
   - Three horizontal beams, each with a square cross-section of 4 cun × 4 cun.
   - One pillar with a circular cross-section of diameter 3 chi (30 cun) and height 1 zhang (100 cun).

3. **Procedure**:
   - Calculate the total volume of the granary.
   - Subtract the volume of the internal structures (vertical beams, horizontal beams, and pillar).
   - Convert the remaining volume into *hu* and leftover *cun* using the conversion factor: 1 *hu* = 1620 cubic cun.

---

### Python Code:


"""

#----- content starts here -----

from fractions import Fraction

# Granary dimensions
length_cun = 130  # 1 zhang 3 chi = 130 cun
width_cun = 60    # 6 chi = 60 cun
height_cun = 100  # 1 zhang = 100 cun

# Total volume of the granary
total_volume_cun = length_cun * width_cun * height_cun

# Internal structures
# 1. Two vertical beams (5 cun × 5 cun cross-section)
beam_side_cun = 5
beam_volume_cun = 2 * (beam_side_cun ** 2) * length_cun

# 2. Three horizontal beams (4 cun × 4 cun cross-section)
horizontal_beam_side_cun = 4
horizontal_beam_volume_cun = 3 * (horizontal_beam_side_cun ** 2) * width_cun

# 3. One pillar (circular cross-section, diameter 30 cun, height 100 cun)
pillar_diameter_cun = 30
pillar_radius_cun = pillar_diameter_cun / 2
pillar_volume_cun = (Fraction(22, 7) * (pillar_radius_cun ** 2) * height_cun)

# Total volume of internal structures
internal_volume_cun = beam_volume_cun + horizontal_beam_volume_cun + pillar_volume_cun

# Remaining volume of the granary
remaining_volume_cun = total_volume_cun - internal_volume_cun

# Convert to hu and leftover cun
hu_volume_cun = 1620  # 1 hu = 1620 cubic cun
hu = remaining_volume_cun // hu_volume_cun
leftover_cun = remaining_volume_cun % hu_volume_cun

# Results
a = hu
b = leftover_cun

print(f"Answer: {a} hu and {b} cun.")
#----- content ends here -----


"""


---

### Explanation of the Code:
1. **Granary Volume**:
   - The volume is calculated as `length × width × height`.

2. **Internal Structures**:
   - For the beams, the volume is calculated as `cross-sectional area × length` or `width`, multiplied by the number of beams.
   - For the pillar, the volume is calculated using the formula for the volume of a cylinder: \( \pi r^2 h \), approximating \( \pi \) as \( \frac{22}{7} \).

3. **Remaining Volume**:
   - Subtract the total volume of the internal structures from the total granary volume.

4. **Conversion to *hu* and *cun***:
   - Divide the remaining volume by 1620 to get the number of *hu*.
   - Use the remainder to get the leftover *cun*.

---

### Example Output:
If you run the code, it will compute the exact values for `a` (number of *hu*) and `b` (leftover *cun*).
"""


"""
Variable 'a' has wrong value. Expected: 471, Actual: 432.0
Variable 'b' has wrong value. Expected: 100, Actual: 65.71428571431898"""
