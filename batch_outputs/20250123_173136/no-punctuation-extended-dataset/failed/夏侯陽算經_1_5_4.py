"""
今有方倉長三十一丈六尺廣七十二尺髙一十七尺中有九柱各圓三尺五寸長十七尺又有六柱各方二尺八寸長十七尺梁三枚長三十二尺厚廣二尺牽三枚長三十二尺各方七寸問受粟幾何
術曰置長廣相乗以髙乗為實圓柱自乗以乘長十二而一九因之為實方柱自乗以乗長六因之為實梁厚廣相乗以乗長三因之為實牽方自乗以乗長三因之為實并柱梁牽等減倉實尺以斛法除之即粟數
答曰 a斛
"""

"""
Suppose there is a rectangular granary with a length of 31 zhang 6 chi, a width of 72 chi, and a height of 17 chi.
Inside, there are 9 cylindrical pillars, each with a diameter of 3 chi 5 cun and a height of 17 chi.
Additionally, there are 6 square pillars, each with a side length of 2 chi 8 cun and a height of 17 chi.
There are 3 beams, each 32 chi long, 2 chi wide, and 2 chi thick.
Finally, there are 3 tie beams, each 32 chi long and with a square cross-section of 7 cun by 7 cun.
Question: how much grain can the granary hold?

The procedure says:
1. Multiply the length and width, then multiply by the height to get the total volume of the granary.
2. For cylindrical pillars, square the diameter, multiply by the height, and divide by 12. Multiply this by the number of cylindrical pillars to get their total volume.
3. For square pillars, square the side length, multiply by the height, and multiply by the number of square pillars to get their total volume.
4. For beams, multiply the width and thickness, then multiply by the length, and multiply by the number of beams to get their total volume.
5. For tie beams, square the side length, multiply by the length, and multiply by the number of tie beams to get their total volume.
6. Subtract the total volume of the pillars, beams, and tie beams from the granary's total volume.
7. Divide the remaining volume by the volume of one hu (10 cubic chi) to get the amount of grain.

Answer: *a* hu.
"""

from fractions import Fraction

# Dimensions of the granary
長 = 31 * 10 + 6  # Convert zhang and chi to chi (1 zhang = 10 chi)
廣 = 72
高 = 17

# Cylindrical pillars
圓柱數量 = 9
圓柱直徑 = 3 * 10 + 5  # Convert chi and cun to chi (1 chi = 10 cun)
圓柱高 = 17

# Square pillars
方柱數量 = 6
方柱邊長 = 2 * 10 + 8  # Convert chi and cun to chi
方柱高 = 17

# Beams
梁數量 = 3
梁長 = 32
梁厚 = 2
梁廣 = 2

# Tie beams
牽數量 = 3
牽長 = 32
牽邊長 = Fraction(7, 10)  # Convert cun to chi

# Volume of the granary
倉實 = 長 * 廣 * 高

# Volume of cylindrical pillars
圓柱體積 = 圓柱數量 * (Fraction(圓柱直徑, 2) ** 2 * 圓柱高 * Fraction(3.141592653589793, 12))

# Volume of square pillars
方柱體積 = 方柱數量 * (方柱邊長 ** 2 * 方柱高)

# Volume of beams
梁體積 = 梁數量 * (梁厚 * 梁廣 * 梁長)

# Volume of tie beams
牽體積 = 牽數量 * (牽邊長 ** 2 * 牽長)

# Subtract the volumes of the pillars, beams, and tie beams from the granary's total volume
剩餘體積 = 倉實 - 圓柱體積 - 方柱體積 - 梁體積 - 牽體積

# Convert the remaining volume to hu (1 hu = 10 cubic chi)
a = 剩餘體積 / 10
"""
Code error: both arguments should be Rational instances"""
