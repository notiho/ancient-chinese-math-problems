"""
今有倉從一丈三尺廣六尺高一丈中有從牽二枚方五寸從一丈三尺又横牽三枚方四寸從六尺又柱一枚周三尺高一丈。問：受粟㡬何？
術曰：列從一丈三尺上十之得一百三十寸以廣六十寸乘之得七千八百寸又列高一丈上十之為一百寸以乘之得七十八萬寸為都積又列從牽二枚方五寸自相乘得二十五寸以從一百三十寸乘之得三千二百五十寸以從牽二枚乘之得六千五百寸又列横牽三枚方四寸自相乘得十六寸以從六十寸乘之得九百六十寸以横牽三枚乘之得二千八百八十寸又列柱一枚周三尺上十之得三十寸自相乘得九百寸以高一百寸乘之得九萬寸以十二除之得七千五百寸并從横牽及柱等三位得一萬六千八百八十寸以減都積餘七十六萬三千一百二十寸為實以斛法一千六百二十寸除之即得。
答曰： a斛 奇 b寸 。
"""

"""
Suppose there is a granary with the following dimensions:
- Length: 1 zhang 3 chi (13 chi)
- Width: 6 chi
- Height: 1 zhang (10 chi)

Inside the granary:
- There are 2 vertical beams, each square with a side length of 5 cun, and the length of the beams is the same as the granary's length (13 chi).
- There are 3 horizontal beams, each square with a side length of 4 cun, and the length of the beams is the same as the granary's width (6 chi).
- There is 1 pillar with a circumference of 3 chi, and its height is the same as the granary's height (10 chi).

Question: How much millet can the granary hold?

The procedure says:
1. Convert the length of 1 zhang 3 chi to cun by multiplying by 10, obtaining 130 cun.
   Multiply this by the width of 6 chi (converted to 60 cun), obtaining 7800 cun².
2. Convert the height of 1 zhang to cun by multiplying by 10, obtaining 100 cun.
   Multiply this by the previous result, obtaining the total volume of 780,000 cun³.
3. For the vertical beams:
   - Each beam is square with a side length of 5 cun. Multiply 5 cun by itself to get 25 cun².
   - Multiply this by the length of the granary (130 cun), obtaining 3250 cun³ per beam.
   - Multiply this by 2 beams, obtaining 6500 cun³.
4. For the horizontal beams:
   - Each beam is square with a side length of 4 cun. Multiply 4 cun by itself to get 16 cun².
   - Multiply this by the width of the granary (60 cun), obtaining 960 cun³ per beam.
   - Multiply this by 3 beams, obtaining 2880 cun³.
5. For the pillar:
   - The pillar has a circumference of 3 chi (30 cun). Divide this by 4π to approximate the diameter, then square the radius and multiply by π to approximate the cross-sectional area.
   - Alternatively, use the simplified method: square the circumference (30 cun × 30 cun = 900 cun²), multiply by the height (100 cun), and divide by 12 to approximate the volume, obtaining 7500 cun³.
6. Add the volumes of the vertical beams, horizontal beams, and pillar, obtaining 16,880 cun³.
7. Subtract this from the total volume of the granary, obtaining the remaining volume of 763,120 cun³.
8. Divide this by the millet conversion factor (1620 cun³ per hu), obtaining the number of hu and the remainder.

Answer: *a* hu and *b* cun³.
"""

# Granary dimensions
length_chi = 13  # 1 zhang 3 chi
width_chi = 6    # 6 chi
height_chi = 10  # 1 zhang

# Conversion to cun
length_cun = length_chi * 10
width_cun = width_chi * 10
height_cun = height_chi * 10

# Total volume of the granary
total_volume = length_cun * width_cun * height_cun

# Vertical beams
vertical_beam_side = 5  # 5 cun
vertical_beam_count = 2
vertical_beam_volume = (vertical_beam_side ** 2) * length_cun * vertical_beam_count

# Horizontal beams
horizontal_beam_side = 4  # 4 cun
horizontal_beam_count = 3
horizontal_beam_volume = (horizontal_beam_side ** 2) * width_cun * horizontal_beam_count

# Pillar
pillar_circumference = 30  # 3 chi = 30 cun
pillar_height = height_cun
pillar_volume = (pillar_circumference ** 2) * pillar_height // 12

# Total obstruction volume
obstruction_volume = vertical_beam_volume + horizontal_beam_volume + pillar_volume

# Remaining volume for millet
remaining_volume = total_volume - obstruction_volume

# Millet conversion factor
millet_conversion = 1620  # 1620 cun³ per hu

# Calculate hu and remaining cun³
a = remaining_volume // millet_conversion
b = remaining_volume % millet_conversion
"""
"""
