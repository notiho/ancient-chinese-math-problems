"""
今有倉從一丈三尺廣六尺高一丈中有從牽二枚方五寸從一丈三尺又横牽三枚方四寸從六尺又柱一枚周三尺高一丈。問：受粟㡬何？
術曰：列從一丈三尺上十之得一百三十寸以廣六十寸乘之得七千八百寸又列高一丈上十之為一百寸以乘之得七十八萬寸為都積又列從牽二枚方五寸自相乘得二十五寸以從一百三十寸乘之得三千二百五十寸以從牽二枚乘之得六千五百寸又列横牽三枚方四寸自相乘得十六寸以從六十寸乘之得九百六十寸以横牽三枚乘之得二千八百八十寸又列柱一枚周三尺上十之得三十寸自相乘得九百寸以高一百寸乘之得九萬寸以十二除之得七千五百寸并從横牽及柱等三位得一萬六千八百八十寸以減都積餘七十六萬三千一百二十寸為實以斛法一千六百二十寸除之即得。
答曰： a斛 奇 b寸 。
"""

#----- content starts here -----
"""
Suppose there is a granary with a length of 1 zhang 3 chi, a width of 6 chi, and a height of 1 zhang. 
Inside, there are:
- 2 vertical beams, each square with a side length of 5 cun, spanning the full length of 1 zhang 3 chi.
- 3 horizontal beams, each square with a side length of 4 cun, spanning the full width of 6 chi.
- 1 pillar with a circumference of 3 chi and a height of 1 zhang.

Question: How much millet can the granary hold?

The procedure says:
1. Convert the length of 1 zhang 3 chi to cun by multiplying by 10, obtaining 130 cun. Multiply this by the width of 6 chi (converted to 60 cun), obtaining 7800 cun². Then multiply by the height of 1 zhang (converted to 100 cun), obtaining 780,000 cun³ as the total volume.
2. For the 2 vertical beams:
   - Take the side length of 5 cun, square it to get 25 cun². Multiply this by the length of 130 cun to get 3250 cun³. Multiply by 2 beams to get 6500 cun³.
3. For the 3 horizontal beams:
   - Take the side length of 4 cun, square it to get 16 cun². Multiply this by the width of 60 cun to get 960 cun³. Multiply by 3 beams to get 2880 cun³.
4. For the pillar:
   - Take the circumference of 3 chi (converted to 30 cun), square it to get 900 cun². Multiply by the height of 100 cun to get 90,000 cun³. Divide by 12 (since the pillar is cylindrical) to get 7500 cun³.
5. Add the volumes of the vertical beams, horizontal beams, and the pillar: 6500 + 2880 + 7500 = 16,880 cun³.
6. Subtract this from the total volume: 780,000 - 16,880 = 763,120 cun³.
7. Divide by the millet conversion factor of 1620 cun³ per hu to get the number of hu.

Answer: *a* hu and *b* cun³.
"""

from fractions import Fraction

# Dimensions of the granary
length = 1 * 10 + 3  # 1丈3尺 converted to寸
width = 6 * 10       # 6尺 converted to寸
height = 1 * 10      # 1丈 converted to寸

# Total volume of the granary
total_volume = length * width * height

# Vertical beams
vertical_beams_count = 2
vertical_beam_side = 5  # 方5寸
vertical_beam_volume = (vertical_beam_side ** 2) * length * vertical_beams_count

# Horizontal beams
horizontal_beams_count = 3
horizontal_beam_side = 4  # 方4寸
horizontal_beam_volume = (horizontal_beam_side ** 2) * width * horizontal_beams_count

# Pillar
pillar_circumference = 3 * 10  # 周3尺 converted to寸
pillar_height = height
pillar_volume = (pillar_circumference ** 2) * pillar_height // 12  # Divide by 12 for cylindrical volume

# Total obstruction volume
obstruction_volume = vertical_beam_volume + horizontal_beam_volume + pillar_volume

# Usable volume
usable_volume = total_volume - obstruction_volume

# Conversion factor for millet (1斛 = 1620寸³)
millet_conversion_factor = 1620

# Calculate hu and remaining cun³
a = usable_volume // millet_conversion_factor  # Number of hu
b = usable_volume % millet_conversion_factor   # Remaining cun³

a, b  # Output the result as (a hu, b cun³)#----- content ends here -----

"""
Variable 'a' has wrong value. Expected: 471, Actual: 2
Variable 'b' has wrong value. Expected: 100, Actual: 280"""
