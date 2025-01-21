"""
今有倉廣二丈六尺長三丈四尺深一丈二尺中有二柱長一丈二尺圓三尺牽二枚長二丈六尺方五寸梁二枚長二丈六尺方三尺問受粟幾何
術曰置廣長相乗以其深乗得一萬六百八尺柱圓三尺自相乗得九尺以乗其長得一百八尺倍之得二百一十六尺以十二除之得一十八尺牽方自相乗退位得二寸五分復乗其長得六尺五寸倍之得一十三尺梁方自乗得九尺復乗其長得二百三十四尺倍之得四百六十八尺并柱牽梁得四百九十九尺以減大數餘一萬一百九尺以斛法除之即粟數
答曰 a斛
"""

"""
Suppose there is a granary with a width of 2 zhang 6 chi, a length of 3 zhang 4 chi, and a depth of 1 zhang 2 chi.
Inside, there are:
- 2 pillars, each 1 zhang 2 chi long and with a circular cross-section of 3 chi in diameter.
- 2 beams, each 2 zhang 6 chi long and with a square cross-section of 5 cun on each side.
- 2 additional beams, each 2 zhang 6 chi long and with a square cross-section of 3 chi on each side.

Question: How much millet can the granary hold?

The procedure says:
- Multiply the width and length, then multiply by the depth to get the total volume.
- For the pillars: Square the diameter (3 chi), multiply by the length, and double it (for 2 pillars). Divide by 12 to get the volume of the pillars.
- For the beams with a square cross-section of 5 cun: Square the side length (5 cun), convert to chi (divide by 10), multiply by the length, and double it (for 2 beams).
- For the beams with a square cross-section of 3 chi: Square the side length (3 chi), multiply by the length, and double it (for 2 beams).
- Add the volumes of the pillars and beams, then subtract from the total volume.
- Divide the remaining volume by the "hu method" (10 chi³ per hu) to get the amount of millet.

Answer: *a* hu.
"""

from fractions import Fraction

# Dimensions of the granary
廣 = 2 * 10 + 6  # Convert zhang and chi to chi
長 = 3 * 10 + 4
深 = 1 * 10 + 2

# Volume of the granary
總體積 = 廣 * 長 * 深

# Dimensions of the pillars
柱圓直徑 = 3  # chi
柱長 = 1 * 10 + 2  # chi

# Volume of one pillar
柱圓半徑 = Fraction(柱圓直徑, 2)
柱體積 = (柱圓半徑 ** 2) * 3.141592653589793 * 柱長  # πr²h for one pillar
柱總體積 = 2 * 柱體積  # Two pillars

# Dimensions of the beams (5 cun square cross-section)
牽方邊長 = Fraction(5, 10)  # Convert cun to chi
牽長 = 2 * 10 + 6  # chi

# Volume of one beam (5 cun square cross-section)
牽體積 = (牽方邊長 ** 2) * 牽長
牽總體積 = 2 * 牽體積  # Two beams

# Dimensions of the beams (3 chi square cross-section)
梁方邊長 = 3  # chi
梁長 = 2 * 10 + 6  # chi

# Volume of one beam (3 chi square cross-section)
梁體積 = (梁方邊長 ** 2) * 梁長
梁總體積 = 2 * 梁體積  # Two beams

# Total volume of pillars and beams
柱牽梁總體積 = 柱總體積 + 牽總體積 + 梁總體積

# Remaining volume in the granary
剩餘體積 = 總體積 - 柱牽梁總體積

# Convert remaining volume to hu (1 hu = 10 chi³)
粟數 = 剩餘體積 / 10

a = 粟數
"""
Variable 'a' has wrong value. Expected: 505450/81, Actual: 995.7353996706152"""
