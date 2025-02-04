"""
今有倉從一丈三尺廣六尺高一丈中有從牽二枚方五寸從一丈三尺又横牽三枚方四寸從六尺又柱一枚周三尺高一丈。問：受粟㡬何？
術曰：列從一丈三尺上十之得一百三十寸以廣六十寸乘之得七千八百寸又列高一丈上十之為一百寸以乘之得七十八萬寸為都積又列從牽二枚方五寸自相乘得二十五寸以從一百三十寸乘之得三千二百五十寸以從牽二枚乘之得六千五百寸又列横牽三枚方四寸自相乘得十六寸以從六十寸乘之得九百六十寸以横牽三枚乘之得二千八百八十寸又列柱一枚周三尺上十之得三十寸自相乘得九百寸以高一百寸乘之得九萬寸以十二除之得七千五百寸并從横牽及柱等三位得一萬六千八百八十寸以減都積餘七十六萬三千一百二十寸為實以斛法一千六百二十寸除之即得。
答曰： a斛 奇 b寸 。
"""

#----- content starts here -----
"""
Suppose there is a granary with a length of 1 zhang 3 chi, a width of 6 chi, and a height of 1 zhang.
Inside, there are:
- 2 vertical beams, each square with a side length of 5 cun, spanning the full height of 1 zhang 3 chi.
- 3 horizontal beams, each square with a side length of 4 cun, spanning the full width of 6 chi.
- 1 pillar with a circumference of 3 chi and a height of 1 zhang.

Question: How much millet can the granary hold?

The procedure says:
1. Convert the length of 1 zhang 3 chi to cun by multiplying by 10, obtaining 130 cun. Multiply this by the width of 60 cun, obtaining 7800 cun².
2. Convert the height of 1 zhang to cun by multiplying by 10, obtaining 100 cun. Multiply this by the previous result, obtaining 780,000 cun³ as the total volume.
3. For the vertical beams:
   - Each beam is square with a side length of 5 cun. Multiply 5 cun by itself, obtaining 25 cun².
   - Multiply this by the length of 130 cun, obtaining 3250 cun³ per beam.
   - Multiply this by 2 beams, obtaining 6500 cun³.
4. For the horizontal beams:
   - Each beam is square with a side length of 4 cun. Multiply 4 cun by itself, obtaining 16 cun².
   - Multiply this by the width of 60 cun, obtaining 960 cun³ per beam.
   - Multiply this by 3 beams, obtaining 2880 cun³.
5. For the pillar:
   - The circumference is 3 chi, converted to 30 cun. Divide this by 12 to find the diameter, obtaining 2.5 cun.
   - Multiply the diameter by itself, then by π (approximated as 3), obtaining the cross-sectional area of approximately 900 cun².
   - Multiply this by the height of 100 cun, obtaining 90,000 cun³.
   - Divide this by 12 (since the pillar is circular), obtaining 7500 cun³.
6. Add the volumes of the vertical beams, horizontal beams, and the pillar, obtaining 16,880 cun³.
7. Subtract this from the total volume of the granary, obtaining 763,120 cun³ as the usable volume.
8. Divide this by the millet capacity factor of 1620 cun³ per hu, obtaining the number of hu and the remainder in cun³.

Answer: *a* hu and *b* cun³.
"""

# Dimensions of the granary
length = 1 * 10 + 3  # 1 zhang 3 chi = 13 chi = 130 cun
width = 6 * 10       # 6 chi = 60 cun
height = 1 * 10      # 1 zhang = 10 chi = 100 cun

# Total volume of the granary
total_volume = length * width * height  # in cun³

# Vertical beams (2 beams, each 5 cun x 5 cun x 130 cun)
vertical_beam_side = 5  # cun
vertical_beam_length = length  # 130 cun
vertical_beam_volume = vertical_beam_side**2 * vertical_beam_length * 2  # 2 beams

# Horizontal beams (3 beams, each 4 cun x 4 cun x 60 cun)
horizontal_beam_side = 4  # cun
horizontal_beam_width = width  # 60 cun
horizontal_beam_volume = horizontal_beam_side**2 * horizontal_beam_width * 3  # 3 beams

# Pillar (1 pillar, circular with circumference 30 cun and height 100 cun)
pillar_circumference = 3 * 10  # 3 chi = 30 cun
pillar_diameter = Fraction(pillar_circumference, 3.14)  # Approximate diameter using π
pillar_radius = Fraction(pillar_diameter, 2)  # Radius
pillar_height = height  # 100 cun
pillar_cross_section_area = Fraction(22, 7) * pillar_radius**2  # πr² (using π ≈ 22/7)
pillar_volume = Fraction(pillar_cross_section_area * pillar_height, 1)  # Volume of the pillar

# Total volume occupied by beams and pillar
occupied_volume = vertical_beam_volume + horizontal_beam_volume + pillar_volume

# Usable volume of the granary
usable_volume = total_volume - occupied_volume

# Millet capacity factor
millet_capacity = 1620  # 1 hu = 1620 cun³

# Calculate the number of hu and the remainder in cun³
a = usable_volume // millet_capacity  # Number of hu
b = usable_volume % millet_capacity  # Remaining cun³#----- content ends here -----

"""
Code error: both arguments should be Rational instances"""
