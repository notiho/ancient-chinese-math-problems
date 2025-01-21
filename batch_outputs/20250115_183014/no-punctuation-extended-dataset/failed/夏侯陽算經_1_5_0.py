"""
今有方倉長三十一丈六尺廣七十二尺髙一十七尺中有九柱各圓三尺五寸長十七尺又有六柱各方二尺八寸長十七尺梁三枚長三十二尺厚廣二尺牽三枚長三十二尺各方七寸問受粟幾何
術曰置長廣相乗以髙乗為實圓柱自乗以乘長十二而一九因之為實方柱自乗以乗長六因之為實梁厚廣相乗以乗長三因之為實牽方自乗以乗長三因之為實并柱梁牽等減倉實尺以斛法除之即粟數
答曰 a斛
"""

"""
Suppose there is a rectangular granary with a length of 31 zhang 6 chi, a width of 72 chi, and a height of 17 chi.
Inside, there are 9 cylindrical pillars, each with a diameter of 3 chi 5 cun and a height of 17 chi.
Additionally, there are 6 square pillars, each with a side length of 2 chi 8 cun and a height of 17 chi.
There are 3 beams, each with a length of 32 chi, a width of 2 chi, and a thickness of 2 chi.
There are also 3 tie beams, each with a length of 32 chi and a square cross-section of 7 cun by 7 cun.
Question: How much millet can the granary hold?

The procedure says:
1. Multiply the length and width, then multiply by the height to get the volume of the granary.
2. For cylindrical pillars: Square the diameter, multiply by the height, and divide by 12. Multiply this by the number of cylindrical pillars to get their total volume.
3. For square pillars: Square the side length, multiply by the height, and multiply by the number of square pillars to get their total volume.
4. For beams: Multiply the width and thickness, then multiply by the length, and multiply by the number of beams to get their total volume.
5. For tie beams: Square the side length, multiply by the length, and multiply by the number of tie beams to get their total volume.
6. Subtract the total volume of the pillars, beams, and tie beams from the granary's volume.
7. Divide the remaining volume by the volume of one hu (10 cubic chi) to get the number of hu of millet.

Answer: *a* hu.
"""

from fractions import Fraction

# Granary dimensions
倉長 = 31 * 10 + 6  # Convert zhang and chi to chi
倉廣 = 72
倉高 = 17

# Cylindrical pillars
圓柱數 = 9
圓柱直徑 = 3 * 10 + 5  # Convert chi and cun to chi
圓柱高 = 17

# Square pillars
方柱數 = 6
方柱邊長 = 2 * 10 + 8  # Convert chi and cun to chi
方柱高 = 17

# Beams
梁數 = 3
梁長 = 32
梁厚 = 2
梁廣 = 2

# Tie beams
牽數 = 3
牽長 = 32
牽邊長 = Fraction(7, 10)  # Convert cun to chi

# Volume of the granary
倉實 = 倉長 * 倉廣 * 倉高

# Volume of cylindrical pillars
圓柱體積 = (Fraction(圓柱直徑, 2) ** 2 * 3.141592653589793) * 圓柱高 / 12
圓柱總體積 = 圓柱體積 * 圓柱數

# Volume of square pillars
方柱體積 = 方柱邊長 ** 2 * 方柱高
方柱總體積 = 方柱體積 * 方柱數

# Volume of beams
梁體積 = 梁厚 * 梁廣 * 梁長
梁總體積 = 梁體積 * 梁數

# Volume of tie beams
牽體積 = 牽邊長 ** 2 * 牽長
牽總體積 = 牽體積 * 牽數

# Subtract the volumes of pillars, beams, and tie beams from the granary's volume
剩餘體積 = 倉實 - (圓柱總體積 + 方柱總體積 + 梁總體積 + 牽總體積)

# Convert the remaining volume to hu (1 hu = 10 cubic chi)
粟數 = 剩餘體積 / 10

a = 粟數
"""
Variable 'a' has wrong value. Expected: 51386279/216, Actual: 29411.802243543614"""
