"""
今有倉從一丈三尺廣六尺高一丈中有從牽二枚方五寸從一丈三尺又横牽三枚方四寸從六尺又柱一枚周三尺高一丈。問：受粟㡬何？
術曰：列從一丈三尺上十之得一百三十寸以廣六十寸乘之得七千八百寸又列高一丈上十之為一百寸以乘之得七十八萬寸為都積又列從牽二枚方五寸自相乘得二十五寸以從一百三十寸乘之得三千二百五十寸以從牽二枚乘之得六千五百寸又列横牽三枚方四寸自相乘得十六寸以從六十寸乘之得九百六十寸以横牽三枚乘之得二千八百八十寸又列柱一枚周三尺上十之得三十寸自相乘得九百寸以高一百寸乘之得九萬寸以十二除之得七千五百寸并從横牽及柱等三位得一萬六千八百八十寸以減都積餘七十六萬三千一百二十寸為實以斛法一千六百二十寸除之即得。
答曰： a(=471)斛 奇 b(=100)寸 。
"""

#----- content starts here -----
"""
Suppose there is a granary with a length of 1 zhang 3 chi, a width of 6 chi, and a height of 1 zhang. 
Inside, there are:
- Two vertical beams, each square with a side length of 5 cun, and extending the full height of 1 zhang 3 chi.
- Three horizontal beams, each square with a side length of 4 cun, and extending the full width of 6 chi.
- One pillar with a circumference of 3 chi and a height of 1 zhang.

Question: How much millet can the granary hold?

The procedure says:
1. Convert the length (1 zhang 3 chi) to cun by multiplying by 10, obtaining 130 cun. Multiply this by the width (6 chi converted to 60 cun), obtaining 7800 cun². Then multiply by the height (1 zhang converted to 100 cun), obtaining 780,000 cun³ as the total volume.
2. For the vertical beams:
   - Each beam is square with a side of 5 cun. Multiply 5 cun by itself to get 25 cun². Multiply this by the length (130 cun) to get 3250 cun³ per beam. Multiply by 2 beams to get 6500 cun³.
3. For the horizontal beams:
   - Each beam is square with a side of 4 cun. Multiply 4 cun by itself to get 16 cun². Multiply this by the width (60 cun) to get 960 cun³ per beam. Multiply by 3 beams to get 2880 cun³.
4. For the pillar:
   - The pillar has a circumference of 3 chi (30 cun). Divide the circumference by π (approximated as 3) to get the diameter (10 cun). Divide the diameter by 2 to get the radius (5 cun). Multiply the radius by itself to get the cross-sectional area (25 cun²). Multiply this by the height (100 cun) to get 2500 cun³. Multiply by π (approximated as 3) to get 7500 cun³.
5. Add the volumes of the beams and pillar together (6500 + 2880 + 7500 = 16,880 cun³). Subtract this from the total volume (780,000 - 16,880 = 763,120 cun³).
6. Divide the remaining volume by the millet conversion factor (1620 cun³ per hu) to get the number of hu.

Answer: *a*(=471) hu and *b*(=100) cun³.
"""

from fractions import Fraction

# Dimensions of the granary
length = 1 * 100 + 3 * 10  # 1丈3尺 = 130寸
width = 6 * 10  # 6尺 = 60寸
height = 1 * 100  # 1丈 = 100寸

# Total volume of the granary
total_volume = length * width * height  # 都積 = 780,000寸³

# Vertical beams (2 beams, each square with a side of 5寸)
beam_side = 5  # 方5寸
beam_volume_per = beam_side * beam_side * length  # 自相乘 * 長
beam_volume_total = beam_volume_per * 2  # 2 beams

# Horizontal beams (3 beams, each square with a side of 4寸)
horizontal_beam_side = 4  # 方4寸
horizontal_beam_volume_per = horizontal_beam_side * horizontal_beam_side * width  # 自相乘 * 廣
horizontal_beam_volume_total = horizontal_beam_volume_per * 3  # 3 beams

# Pillar (1 pillar, circumference 3尺, height 1丈)
pillar_circumference = 3 * 10  # 周3尺 = 30寸
pillar_radius = Fraction(pillar_circumference, 3) / 2  # 半徑 = 周 / 3 / 2
pillar_cross_section = pillar_radius * pillar_radius  # 自相乘
pillar_volume = pillar_cross_section * height * 3  # 高 * π (approximated as 3)

# Total volume of beams and pillar
obstruction_volume = beam_volume_total + horizontal_beam_volume_total + pillar_volume

# Remaining volume in the granary
remaining_volume = total_volume - obstruction_volume

# Millet conversion factor
millet_conversion = 1620  # 1斛 = 1620寸³

# Calculate the number of hu and remaining cun³
a = remaining_volume // millet_conversion  # Number of hu
b = remaining_volume % millet_conversion  # Remaining cun³

a, b  # 471 hu and 100 cun³#----- content ends here -----

"""
"""
