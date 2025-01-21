"""
今有倉從一丈三尺廣六尺高一丈中有從牽二枚方五寸從一丈三尺又横牽三枚方四寸從六尺又柱一枚周三尺高一丈。問：受粟㡬何？
術曰：列從一丈三尺上十之得一百三十寸以廣六十寸乘之得七千八百寸又列高一丈上十之為一百寸以乘之得七十八萬寸為都積又列從牽二枚方五寸自相乘得二十五寸以從一百三十寸乘之得三千二百五十寸以從牽二枚乘之得六千五百寸又列横牽三枚方四寸自相乘得十六寸以從六十寸乘之得九百六十寸以横牽三枚乘之得二千八百八十寸又列柱一枚周三尺上十之得三十寸自相乘得九百寸以高一百寸乘之得九萬寸以十二除之得七千五百寸并從横牽及柱等三位得一萬六千八百八十寸以減都積餘七十六萬三千一百二十寸為實以斛法一千六百二十寸除之即得。
答曰： a斛 奇 b寸 。
"""

"""
Suppose there is a granary with a length of 1 zhang 3 chi, a width of 6 chi, and a height of 1 zhang. 
Inside, there are two vertical beams, each square with a side length of 5 cun, running the full height of 1 zhang 3 chi. 
Additionally, there are three horizontal beams, each square with a side length of 4 cun, running the full width of 6 chi. 
Finally, there is one pillar with a circumference of 3 chi and a height of 1 zhang. 
Question: how much millet can the granary hold?

The procedure says:
1. Convert the length of 1 zhang 3 chi into cun by multiplying by 10, obtaining 130 cun. Multiply this by the width of 6 chi converted to 60 cun, obtaining 7,800 cun². Then multiply by the height of 1 zhang converted to 100 cun, obtaining 780,000 cun³ as the total volume.
2. For the two vertical beams, square the side length of 5 cun to get 25 cun². Multiply this by the length of 130 cun to get 3,250 cun³. Multiply this by 2 (for the two beams) to get 6,500 cun³.
3. For the three horizontal beams, square the side length of 4 cun to get 16 cun². Multiply this by the width of 60 cun to get 960 cun³. Multiply this by 3 (for the three beams) to get 2,880 cun³.
4. For the pillar, convert the circumference of 3 chi into 30 cun. Square this to get 900 cun². Multiply this by the height of 100 cun to get 90,000 cun³. Divide this by 12 (since the cross-section is circular) to get 7,500 cun³.
5. Add the volumes of the vertical beams, horizontal beams, and the pillar to get 16,880 cun³. Subtract this from the total volume of 780,000 cun³ to get the usable volume of 763,120 cun³.
6. Divide the usable volume by the millet standard of 1,620 cun³ per hu to determine the capacity in hu and remaining cun³.

Answer: *a* hu and *b* cun³.
"""

from fractions import Fraction

# Dimensions of the granary
length = 1 * 10 + 3  # 1 zhang 3 chi = 130 cun
width = 6 * 10       # 6 chi = 60 cun
height = 1 * 10      # 1 zhang = 100 cun

# Total volume of the granary
total_volume = length * width * height  # 都積

# Vertical beams
vertical_beam_side = 5  # 5 cun
vertical_beam_count = 2
vertical_beam_volume = vertical_beam_side**2 * length * vertical_beam_count

# Horizontal beams
horizontal_beam_side = 4  # 4 cun
horizontal_beam_count = 3
horizontal_beam_volume = horizontal_beam_side**2 * width * horizontal_beam_count

# Pillar
pillar_circumference = 3 * 10  # 3 chi = 30 cun
pillar_height = height
pillar_volume = (pillar_circumference**2 * pillar_height) / 12

# Total obstruction volume
obstruction_volume = vertical_beam_volume + horizontal_beam_volume + pillar_volume

# Usable volume
usable_volume = total_volume - obstruction_volume

# Millet standard
millet_standard = 1620  # 1 hu = 1620 cun³

# Calculate the capacity in hu and remaining cun³
a = usable_volume // millet_standard  # Full hu
b = usable_volume % millet_standard  # Remaining cun³

a = int(a)
b = int(b)
"""
Variable 'a' has wrong value. Expected: 471, Actual: 2
Variable 'b' has wrong value. Expected: 100, Actual: 280"""
