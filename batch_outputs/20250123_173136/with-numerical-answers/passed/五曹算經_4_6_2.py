"""
今有倉從一丈三尺廣六尺高一丈中有從牽二枚方五寸從一丈三尺又横牽三枚方四寸從六尺又柱一枚周三尺高一丈。問：受粟㡬何？
術曰：列從一丈三尺上十之得一百三十寸以廣六十寸乘之得七千八百寸又列高一丈上十之為一百寸以乘之得七十八萬寸為都積又列從牽二枚方五寸自相乘得二十五寸以從一百三十寸乘之得三千二百五十寸以從牽二枚乘之得六千五百寸又列横牽三枚方四寸自相乘得十六寸以從六十寸乘之得九百六十寸以横牽三枚乘之得二千八百八十寸又列柱一枚周三尺上十之得三十寸自相乘得九百寸以高一百寸乘之得九萬寸以十二除之得七千五百寸并從横牽及柱等三位得一萬六千八百八十寸以減都積餘七十六萬三千一百二十寸為實以斛法一千六百二十寸除之即得。
答曰： a(=471)斛 奇 b(=100)寸 。
"""

"""
Suppose there is a granary with a length of 1 zhang 3 chi, a width of 6 chi, and a height of 1 zhang.
Inside, there are:
- Two vertical beams, each with a square cross-section of 5 cun.
- Three horizontal beams, each with a square cross-section of 4 cun.
- One pillar with a circumference of 3 chi and a height of 1 zhang.

Question: How much millet can the granary hold?

The procedure says:
1. Convert the length (1 zhang 3 chi) to cun by multiplying by 10, obtaining 130 cun.
   Multiply it by the width (6 chi converted to 60 cun), obtaining 7800 cun².
   Multiply this by the height (1 zhang converted to 100 cun), obtaining 780,000 cun³ as the total volume.
2. For the two vertical beams:
   - Take the square cross-section (5 cun × 5 cun = 25 cun²).
   - Multiply it by the length (130 cun), obtaining 3250 cun³.
   - Multiply this by 2 (for the two beams), obtaining 6500 cun³.
3. For the three horizontal beams:
   - Take the square cross-section (4 cun × 4 cun = 16 cun²).
   - Multiply it by the width (60 cun), obtaining 960 cun³.
   - Multiply this by 3 (for the three beams), obtaining 2880 cun³.
4. For the pillar:
   - Take the circumference (3 chi converted to 30 cun) and calculate the cross-sectional area as a circle:
     (30 cun × 30 cun) ÷ 4π ≈ 900 ÷ 12 = 75 cun².
   - Multiply this by the height (100 cun), obtaining 7500 cun³.
5. Add the volumes of the beams and the pillar (6500 + 2880 + 7500 = 16,880 cun³).
   Subtract this from the total volume (780,000 - 16,880 = 763,120 cun³).
6. Divide the remaining volume by the millet conversion factor (1620 cun³ per hu), obtaining the number of hu.

Answer: *a*(=471) hu and *b*(=100) cun³.
"""

from fractions import Fraction

# Dimensions of the granary
length = 1 * 100 + 3 * 10  # 1 zhang 3 chi = 130 cun
width = 6 * 10  # 6 chi = 60 cun
height = 1 * 100  # 1 zhang = 100 cun

# Total volume of the granary
total_volume = length * width * height  # 130 * 60 * 100 = 780,000 cun³

# Volume of the two vertical beams
beam_vertical_cross_section = 5 * 5  # 5 cun × 5 cun = 25 cun²
beam_vertical_volume = beam_vertical_cross_section * length * 2  # 25 * 130 * 2 = 6500 cun³

# Volume of the three horizontal beams
beam_horizontal_cross_section = 4 * 4  # 4 cun × 4 cun = 16 cun²
beam_horizontal_volume = beam_horizontal_cross_section * width * 3  # 16 * 60 * 3 = 2880 cun³

# Volume of the pillar
pillar_circumference = 3 * 10  # 3 chi = 30 cun
pillar_cross_section = Fraction(pillar_circumference * pillar_circumference, 12)  # (30²) / 12 = 900 / 12 = 75 cun²
pillar_volume = pillar_cross_section * height  # 75 * 100 = 7500 cun³

# Total volume occupied by beams and pillar
occupied_volume = beam_vertical_volume + beam_horizontal_volume + pillar_volume  # 6500 + 2880 + 7500 = 16,880 cun³

# Remaining volume for millet
remaining_volume = total_volume - occupied_volume  # 780,000 - 16,880 = 763,120 cun³

# Convert to hu (1 hu = 1620 cun³)
hu = remaining_volume // 1620  # 763,120 // 1620 = 471 hu
remaining_cun = remaining_volume % 1620  # 763,120 % 1620 = 100 cun³

a = hu  # 471 hu
b = remaining_cun  # 100 cun³
"""
"""
