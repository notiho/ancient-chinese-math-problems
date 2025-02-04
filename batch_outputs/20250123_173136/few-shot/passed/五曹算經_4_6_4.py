"""
今有倉從一丈三尺廣六尺高一丈中有從牽二枚方五寸從一丈三尺又横牽三枚方四寸從六尺又柱一枚周三尺高一丈。問：受粟㡬何？
術曰：列從一丈三尺上十之得一百三十寸以廣六十寸乘之得七千八百寸又列高一丈上十之為一百寸以乘之得七十八萬寸為都積又列從牽二枚方五寸自相乘得二十五寸以從一百三十寸乘之得三千二百五十寸以從牽二枚乘之得六千五百寸又列横牽三枚方四寸自相乘得十六寸以從六十寸乘之得九百六十寸以横牽三枚乘之得二千八百八十寸又列柱一枚周三尺上十之得三十寸自相乘得九百寸以高一百寸乘之得九萬寸以十二除之得七千五百寸并從横牽及柱等三位得一萬六千八百八十寸以減都積餘七十六萬三千一百二十寸為實以斛法一千六百二十寸除之即得。
答曰： a斛 奇 b寸 。
"""

"""
Suppose there is a granary with a length of 1 zhang 3 chi, a width of 6 chi, and a height of 1 zhang.
Inside, there are:
- 2 vertical beams, each square with a side of 5 cun, spanning the full length of 1 zhang 3 chi.
- 3 horizontal beams, each square with a side of 4 cun, spanning the full width of 6 chi.
- 1 pillar with a circumference of 3 chi and a height of 1 zhang.

Question: How much millet can the granary hold?

The procedure says:
1. Convert the length of 1 zhang 3 chi to cun by multiplying by 10, obtaining 130 cun.
   Multiply this by the width of 6 chi (converted to 60 cun), obtaining 7800 cun².
   Multiply this by the height of 1 zhang (converted to 100 cun), obtaining 780,000 cun³ as the total volume.
2. For the 2 vertical beams:
   - Each beam has a square cross-section with a side of 5 cun. Multiply 5 cun by itself to get 25 cun².
   - Multiply this by the length of 130 cun to get 3250 cun³ for one beam.
   - Multiply this by 2 beams to get 6500 cun³.
3. For the 3 horizontal beams:
   - Each beam has a square cross-section with a side of 4 cun. Multiply 4 cun by itself to get 16 cun².
   - Multiply this by the width of 60 cun to get 960 cun³ for one beam.
   - Multiply this by 3 beams to get 2880 cun³.
4. For the pillar:
   - The pillar has a circumference of 3 chi (30 cun). Divide by π (approximated as 3) to get the diameter of 10 cun.
   - Divide the diameter by 2 to get the radius of 5 cun. Multiply the radius by itself to get 25 cun².
   - Multiply this by π (approximated as 3) to get the cross-sectional area of 75 cun².
   - Multiply this by the height of 100 cun to get 7500 cun³.
5. Add the volumes of the beams and the pillar (6500 + 2880 + 7500 = 16,880 cun³).
6. Subtract this from the total volume (780,000 - 16,880 = 763,120 cun³).
7. Divide this by the millet conversion factor of 1620 cun³ per hu to get the number of hu.

Answer: *a* hu and *b* cun³.
"""

# Step 1: Calculate the total volume of the granary
length = 1 * 100 + 3 * 10  # 1丈3尺 converted to cun
width = 6 * 10  # 6尺 converted to cun
height = 1 * 100  # 1丈 converted to cun

total_volume = length * width * height  # Total volume in cun³

# Step 2: Calculate the volume of the 2 vertical beams
beam_side = 5  # Side of the square cross-section in cun
beam_length = length  # Beam spans the full length of the granary
beam_volume_one = beam_side * beam_side * beam_length  # Volume of one beam
beam_volume_total = 2 * beam_volume_one  # Total volume of 2 beams

# Step 3: Calculate the volume of the 3 horizontal beams
horizontal_beam_side = 4  # Side of the square cross-section in cun
horizontal_beam_length = width  # Beam spans the full width of the granary
horizontal_beam_volume_one = horizontal_beam_side * horizontal_beam_side * horizontal_beam_length  # Volume of one beam
horizontal_beam_volume_total = 3 * horizontal_beam_volume_one  # Total volume of 3 beams

# Step 4: Calculate the volume of the pillar
pillar_circumference = 3 * 10  # Circumference in cun (3尺 converted to cun)
pillar_radius = pillar_circumference / (2 * 3)  # Radius in cun (using π ≈ 3)
pillar_cross_section_area = pillar_radius * pillar_radius * 3  # Cross-sectional area (πr², using π ≈ 3)
pillar_height = height  # Pillar spans the full height of the granary
pillar_volume = pillar_cross_section_area * pillar_height  # Volume of the pillar

# Step 5: Subtract the volumes of the beams and pillar from the total volume
obstruction_volume = beam_volume_total + horizontal_beam_volume_total + pillar_volume
usable_volume = total_volume - obstruction_volume

# Step 6: Convert the usable volume to hu
millet_conversion_factor = 1620  # 1 hu = 1620 cun³
a = usable_volume // millet_conversion_factor  # Full hu
b = usable_volume % millet_conversion_factor  # Remaining cun³

a, b  # Final answer
"""
"""
