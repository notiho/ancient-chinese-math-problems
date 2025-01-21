"""
今有倉從一丈三尺廣六尺高一丈中有從牽二枚方五寸從一丈三尺又横牽三枚方四寸從六尺又柱一枚周三尺高一丈問受粟㡬何
術曰列從一丈三尺上十之得一百三十寸以廣六十寸乘之得七千八百寸又列高一丈上十之為一百寸以乘之得七十八萬寸為都積又列從牽二枚方五寸自相乘得二十五寸以從一百三十寸乘之得三千二百五十寸以從牽二枚乘之得六千五百寸又列横牽三枚方四寸自相乘得十六寸以從六十寸乘之得九百六十寸以横牽三枚乘之得二千八百八十寸又列柱一枚周三尺上十之得三十寸自相乘得九百寸以高一百寸乘之得九萬寸以十二除之得七千五百寸并從横牽及柱等三位得一萬六千八百八十寸以減都積餘七十六萬三千一百二十寸為實以斛法一千六百二十寸除之即得
答曰 a斛 奇 b寸 
"""

"""
Suppose there is a granary with a length of 1 zhang 3 chi, a width of 6 chi, and a height of 1 zhang.
Inside, there are:
- 2 vertical beams, each square with a side of 5 cun, and extending the full length of 1 zhang 3 chi.
- 3 horizontal beams, each square with a side of 4 cun, and extending the full width of 6 chi.
- 1 pillar with a circumference of 3 chi and a height of 1 zhang.

Question: How much millet can this granary hold?

The procedure says:
1. Convert the length (1 zhang 3 chi) into cun by multiplying by 10, obtaining 130 cun.
   Multiply this by the width (6 chi converted to 60 cun), obtaining 7800 cun².
   Convert the height (1 zhang converted to 100 cun) into cun and multiply, obtaining the total volume in cun³.
2. For the vertical beams:
   - Take the side length of 5 cun, square it to get 25 cun².
   - Multiply this by the length (130 cun) to get the volume of one beam.
   - Multiply by 2 (for 2 beams) to get the total volume of the vertical beams.
3. For the horizontal beams:
   - Take the side length of 4 cun, square it to get 16 cun².
   - Multiply this by the width (60 cun) to get the volume of one beam.
   - Multiply by 3 (for 3 beams) to get the total volume of the horizontal beams.
4. For the pillar:
   - Convert the circumference (3 chi converted to 30 cun) into cun.
   - Square the circumference to get the cross-sectional area in cun².
   - Multiply by the height (100 cun) to get the volume of the pillar.
   - Divide by 12 (since the cross-sectional area is based on the circumference of a circle) to get the actual volume.
5. Add the volumes of the vertical beams, horizontal beams, and the pillar.
   Subtract this from the total volume of the granary to get the usable volume.
6. Divide the usable volume by the millet conversion factor (1620 cun³ per hu) to get the number of hu and the remainder in cun³.

Answer: *a* hu and *b* cun³.
"""

from fractions import Fraction

# Granary dimensions
length = 1 * 10 + 3  # 1 zhang 3 chi = 13 chi = 130 cun
width = 6 * 10       # 6 chi = 60 cun
height = 1 * 10      # 1 zhang = 100 cun

# Total volume of the granary
total_volume = length * width * height  # in cun³

# Vertical beams
vertical_beam_side = 5  # 5 cun
vertical_beam_count = 2
vertical_beam_volume = (vertical_beam_side ** 2) * length * vertical_beam_count  # in cun³

# Horizontal beams
horizontal_beam_side = 4  # 4 cun
horizontal_beam_count = 3
horizontal_beam_volume = (horizontal_beam_side ** 2) * width * horizontal_beam_count  # in cun³

# Pillar
pillar_circumference = 3 * 10  # 3 chi = 30 cun
pillar_height = 1 * 10         # 1 zhang = 100 cun
pillar_cross_section_area = (pillar_circumference ** 2) / 12  # πr² approximated as circumference² / 12
pillar_volume = pillar_cross_section_area * pillar_height  # in cun³

# Total unusable volume
unusable_volume = vertical_beam_volume + horizontal_beam_volume + pillar_volume

# Usable volume
usable_volume = total_volume - unusable_volume

# Millet conversion factor
millet_conversion = 1620  # 1620 cun³ per hu

# Calculate hu and remainder cun³
a = usable_volume // millet_conversion  # Number of hu
b = usable_volume % millet_conversion  # Remaining cun³

a = Fraction(a)
b = Fraction(b)
"""
Variable 'a' has wrong value. Expected: 471, Actual: 2
Variable 'b' has wrong value. Expected: 100, Actual: 280"""
