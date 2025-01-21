"""
今有方倉長三十一丈六尺廣七十二尺髙一十七尺中有九柱各圓三尺五寸長十七尺又有六柱各方二尺八寸長十七尺梁三枚長三十二尺厚廣二尺牽三枚長三十二尺各方七寸問受粟幾何
術曰置長廣相乗以髙乗為實圓柱自乗以乘長十二而一九因之為實方柱自乗以乗長六因之為實梁厚廣相乗以乗長三因之為實牽方自乗以乗長三因之為實并柱梁牽等減倉實尺以斛法除之即粟數
答曰 a斛
"""

"""
Suppose there is a rectangular granary with a length of 31 zhang 6 chi, a width of 72 chi, and a height of 17 chi.
Inside, there are 9 circular columns, each with a diameter of 3 chi 5 cun and a height of 17 chi.
Additionally, there are 6 square columns, each with a side length of 2 chi 8 cun and a height of 17 chi.
There are 3 beams, each 32 chi long, 2 chi wide, and 2 chi thick.
Finally, there are 3 ties, each 32 chi long and 7 cun on each side.
Question: how much millet can it hold?

The procedure says:
1. Multiply the length and width of the granary, then multiply by the height to get the total volume.
2. For circular columns, square the diameter, multiply by the height, and divide by 12. Multiply by the number of columns to get their total volume.
3. For square columns, square the side length, multiply by the height, and multiply by the number of columns to get their total volume.
4. For beams, multiply the width and thickness, then multiply by the length and the number of beams to get their total volume.
5. For ties, square the side length, multiply by the length, and multiply by the number of ties to get their total volume.
6. Subtract the total volume of the columns, beams, and ties from the granary's total volume.
7. Divide the remaining volume by the volume of one hu (10 cubic chi) to get the amount of millet.

Answer: *a* hu.
"""

from fractions import Fraction

# Granary dimensions
倉長 = 31 * 10 + 6  # Convert zhang and chi to chi
倉廣 = 72
倉高 = 17

# Circular columns
圓柱直徑 = 3 * 10 + 5  # Convert chi and cun to chi
圓柱高 = 17
圓柱數 = 9

# Square columns
方柱邊長 = 2 * 10 + 8  # Convert chi and cun to chi
方柱高 = 17
方柱數 = 6

# Beams
梁長 = 32
梁廣 = 2
梁厚 = 2
梁數 = 3

# Ties
牽長 = 32
牽邊長 = Fraction(7, 10)  # Convert cun to chi
牽數 = 3

# Volume of the granary
倉實 = 倉長 * 倉廣 * 倉高

# Volume of circular columns
圓柱體積 = Fraction(圓柱直徑**2 * 圓柱高, 12) * 圓柱數

# Volume of square columns
方柱體積 = 方柱邊長**2 * 方柱高 * 方柱數

# Volume of beams
梁體積 = 梁廣 * 梁厚 * 梁長 * 梁數

# Volume of ties
牽體積 = 牽邊長**2 * 牽長 * 牽數

# Subtract the volumes of columns, beams, and ties from the granary's volume
剩餘體積 = 倉實 - (圓柱體積 + 方柱體積 + 梁體積 + 牽體積)

# Convert the remaining volume to hu (1 hu = 10 cubic chi)
a = Fraction(剩餘體積, 10)  # Volume in hu
"""
Variable 'a' has wrong value. Expected: 51386279/216, Actual: 29076621/1000"""
