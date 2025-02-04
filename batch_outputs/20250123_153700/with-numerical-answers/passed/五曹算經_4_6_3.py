"""
今有倉從一丈三尺廣六尺高一丈中有從牽二枚方五寸從一丈三尺又横牽三枚方四寸從六尺又柱一枚周三尺高一丈。問：受粟㡬何？
術曰：列從一丈三尺上十之得一百三十寸以廣六十寸乘之得七千八百寸又列高一丈上十之為一百寸以乘之得七十八萬寸為都積又列從牽二枚方五寸自相乘得二十五寸以從一百三十寸乘之得三千二百五十寸以從牽二枚乘之得六千五百寸又列横牽三枚方四寸自相乘得十六寸以從六十寸乘之得九百六十寸以横牽三枚乘之得二千八百八十寸又列柱一枚周三尺上十之得三十寸自相乘得九百寸以高一百寸乘之得九萬寸以十二除之得七千五百寸并從横牽及柱等三位得一萬六千八百八十寸以減都積餘七十六萬三千一百二十寸為實以斛法一千六百二十寸除之即得。
答曰： a(=471)斛 奇 b(=100)寸 。
"""

"""
Suppose there is a granary with a length of 1 zhang 3 chi, a width of 6 chi, and a height of 1 zhang.
Inside, there are:
- 2 vertical beams, each square with a side length of 5 cun, spanning the full height of the granary (1 zhang 3 chi).
- 3 horizontal beams, each square with a side length of 4 cun, spanning the full width of the granary (6 chi).
- 1 pillar, with a circumference of 3 chi and a height of 1 zhang.

Question: How much millet can the granary hold?

The procedure says:
1. Convert the length (1 zhang 3 chi) into cun by multiplying by 10, obtaining 130 cun.
   Multiply this by the width (6 chi converted to 60 cun), obtaining 7800 cun².
   Then multiply by the height (1 zhang converted to 100 cun), obtaining 780,000 cun³ as the total volume.
2. For the 2 vertical beams:
   - Take the side length of 5 cun, square it to get 25 cun².
   - Multiply this by the length (130 cun), obtaining 3250 cun³.
   - Multiply this by 2 (for the 2 beams), obtaining 6500 cun³.
3. For the 3 horizontal beams:
   - Take the side length of 4 cun, square it to get 16 cun².
   - Multiply this by the width (60 cun), obtaining 960 cun³.
   - Multiply this by 3 (for the 3 beams), obtaining 2880 cun³.
4. For the pillar:
   - Take the circumference of 3 chi (converted to 30 cun), square it to get 900 cun².
   - Multiply this by the height (100 cun), obtaining 90,000 cun³.
   - Divide this by 12 (to account for the circular cross-section), obtaining 7500 cun³.
5. Add the volumes of the vertical beams, horizontal beams, and the pillar, obtaining 16,880 cun³.
6. Subtract this from the total volume, leaving 763,120 cun³ as the usable volume.
7. Divide this by the millet conversion factor (1620 cun³ per hu), obtaining the result.

Answer: *a*(=471) hu and *b*(=100) cun³.
"""

from fractions import Fraction

# Dimensions of the granary
length_zhang = 1
length_chi = 3
width_chi = 6
height_zhang = 1

# Conversion factors
zhang_to_cun = 100
chi_to_cun = 10

# Convert dimensions to cun
length_cun = length_zhang * zhang_to_cun + length_chi * chi_to_cun  # 130 cun
width_cun = width_chi * chi_to_cun  # 60 cun
height_cun = height_zhang * zhang_to_cun  # 100 cun

# Total volume of the granary
total_volume = length_cun * width_cun * height_cun  # 780,000 cun³

# Vertical beams
vertical_beams_count = 2
vertical_beam_side = 5  # 5 cun
vertical_beam_volume = (vertical_beam_side ** 2) * length_cun * vertical_beams_count  # 6,500 cun³

# Horizontal beams
horizontal_beams_count = 3
horizontal_beam_side = 4  # 4 cun
horizontal_beam_volume = (horizontal_beam_side ** 2) * width_cun * horizontal_beams_count  # 2,880 cun³

# Pillar
pillar_circumference_chi = 3
pillar_circumference_cun = pillar_circumference_chi * chi_to_cun  # 30 cun
pillar_cross_section_area = (pillar_circumference_cun ** 2) / 12  # Circular cross-section
pillar_volume = pillar_cross_section_area * height_cun  # 7,500 cun³

# Total obstruction volume
obstruction_volume = vertical_beam_volume + horizontal_beam_volume + pillar_volume  # 16,880 cun³

# Usable volume
usable_volume = total_volume - obstruction_volume  # 763,120 cun³

# Millet conversion factor
millet_conversion = 1620  # 1 hu = 1620 cun³

# Calculate the amount of millet the granary can hold
millet_hu = usable_volume // millet_conversion  # 471 hu
millet_remainder = usable_volume % millet_conversion  # 100 cun³

a = millet_hu  # 471 hu
b = millet_remainder  # 100 cun³
"""
"""
