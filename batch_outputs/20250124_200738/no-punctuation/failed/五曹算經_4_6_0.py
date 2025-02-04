"""
今有倉從一丈三尺廣六尺高一丈中有從牽二枚方五寸從一丈三尺又横牽三枚方四寸從六尺又柱一枚周三尺高一丈問受粟㡬何
術曰列從一丈三尺上十之得一百三十寸以廣六十寸乘之得七千八百寸又列高一丈上十之為一百寸以乘之得七十八萬寸為都積又列從牽二枚方五寸自相乘得二十五寸以從一百三十寸乘之得三千二百五十寸以從牽二枚乘之得六千五百寸又列横牽三枚方四寸自相乘得十六寸以從六十寸乘之得九百六十寸以横牽三枚乘之得二千八百八十寸又列柱一枚周三尺上十之得三十寸自相乘得九百寸以高一百寸乘之得九萬寸以十二除之得七千五百寸并從横牽及柱等三位得一萬六千八百八十寸以減都積餘七十六萬三千一百二十寸為實以斛法一千六百二十寸除之即得
答曰 a斛 奇 b寸 
"""

#----- content starts here -----
"""
Suppose there is a granary with a length of 1 zhang 3 chi, a width of 6 chi, and a height of 1 zhang. 
Inside, there are:
- 2 vertical beams, each with a square cross-section of 5 cun by 5 cun and a length of 1 zhang 3 chi,
- 3 horizontal beams, each with a square cross-section of 4 cun by 4 cun and a length of 6 chi,
- 1 pillar with a circumference of 3 chi and a height of 1 zhang.

Question: how much millet can the granary hold?

The procedure says:
1. Convert the length of 1 zhang 3 chi to cun by multiplying by 10, obtaining 130 cun. Multiply this by the width of 60 cun, obtaining 7800 cun².
2. Convert the height of 1 zhang to cun by multiplying by 10, obtaining 100 cun. Multiply this by the previous result, obtaining 780,000 cun³ as the total volume.
3. For the vertical beams:
   - Take the square cross-section of 5 cun × 5 cun, obtaining 25 cun².
   - Multiply this by the length of 130 cun, obtaining 3250 cun³ for one beam.
   - Multiply this by 2 beams, obtaining 6500 cun³.
4. For the horizontal beams:
   - Take the square cross-section of 4 cun × 4 cun, obtaining 16 cun².
   - Multiply this by the length of 60 cun, obtaining 960 cun³ for one beam.
   - Multiply this by 3 beams, obtaining 2880 cun³.
5. For the pillar:
   - Convert the circumference of 3 chi to cun by multiplying by 10, obtaining 30 cun.
   - Square this, obtaining 900 cun².
   - Multiply this by the height of 100 cun, obtaining 90,000 cun³.
   - Divide this by 12 (since the cross-section is circular), obtaining 7500 cun³.
6. Add the volumes of the vertical beams, horizontal beams, and pillar, obtaining 16,880 cun³.
7. Subtract this from the total volume, obtaining 763,120 cun³ as the usable volume.
8. Divide this by the volume of 1 hu (1620 cun³), obtaining the number of hu and the remainder in cun³.

Answer: *a* hu and *b* cun³.
"""

from fractions import Fraction

# Dimensions of the granary
length = 1 * 10 + 3  # 1 zhang 3 chi = 13 chi = 130 cun
width = 6 * 10       # 6 chi = 60 cun
height = 1 * 10      # 1 zhang = 10 chi = 100 cun

# Total volume of the granary
total_volume = length * width * height  # in cun³

# Vertical beams
vertical_beam_cross_section = 5 * 5  # 5 cun × 5 cun = 25 cun²
vertical_beam_length = length        # 130 cun
vertical_beam_volume = vertical_beam_cross_section * vertical_beam_length * 2  # 2 beams

# Horizontal beams
horizontal_beam_cross_section = 4 * 4  # 4 cun × 4 cun = 16 cun²
horizontal_beam_length = width         # 60 cun
horizontal_beam_volume = horizontal_beam_cross_section * horizontal_beam_length * 3  # 3 beams

# Pillar
pillar_circumference = 3 * 10  # 3 chi = 30 cun
pillar_cross_section = (pillar_circumference ** 2) / 12  # πr² approximated as (C² / 12)
pillar_height = height         # 100 cun
pillar_volume = pillar_cross_section * pillar_height

# Total volume occupied by beams and pillar
occupied_volume = vertical_beam_volume + horizontal_beam_volume + pillar_volume

# Usable volume
usable_volume = total_volume - occupied_volume

# Volume of 1 hu
hu_volume = 1620  # in cun³

# Calculate the number of hu and the remainder in cun³
a = usable_volume // hu_volume  # Number of hu
b = usable_volume % hu_volume   # Remaining cun³

a = int(a)
b = int(b)#----- content ends here -----

"""
Variable 'a' has wrong value. Expected: 471, Actual: 2
Variable 'b' has wrong value. Expected: 100, Actual: 280"""
