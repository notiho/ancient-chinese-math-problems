"""
今有倉廣二丈六尺長三丈四尺深一丈二尺中有二柱長一丈二尺圓三尺牽二枚長二丈六尺方五寸梁二枚長二丈六尺方三尺問受粟幾何
術曰置廣長相乗以其深乗得一萬六百八尺柱圓三尺自相乗得九尺以乗其長得一百八尺倍之得二百一十六尺以十二除之得一十八尺牽方自相乗退位得二寸五分復乗其長得六尺五寸倍之得一十三尺梁方自乗得九尺復乗其長得二百三十四尺倍之得四百六十八尺并柱牽梁得四百九十九尺以減大數餘一萬一百九尺以斛法除之即粟數
答曰 a斛
"""

"""
Suppose there is a granary with a width of 2 zhang 6 chi, a length of 3 zhang 4 chi, and a depth of 1 zhang 2 chi.
Inside, there are:
- 2 pillars, each 1 zhang 2 chi in length and 3 chi in diameter,
- 2 beams, each 2 zhang 6 chi in length and 5 cun square,
- 2 additional beams, each 2 zhang 6 chi in length and 3 chi square.

Question: How much millet can the granary hold?

The procedure says:
- Multiply the width and length, then multiply by the depth to get the total volume.
- For the pillars: Square the diameter (3 chi), multiply by the length, and double it. Divide by 12 to convert to cubic chi.
- For the beams (5 cun square): Square the side length (5 cun), convert to chi (divide by 10), multiply by the length, and double it.
- For the beams (3 chi square): Square the side length (3 chi), multiply by the length, and double it.
- Add the volumes of the pillars and beams, then subtract from the total volume.
- Divide the remaining volume by the "hu" divisor to get the millet capacity.

Answer: *a* hu.
"""

from fractions import Fraction

# Dimensions of the granary
廣 = 2 * 10 + 6  # Convert zhang and chi to chi
長 = 3 * 10 + 4  # Convert zhang and chi to chi
深 = 1 * 10 + 2  # Convert zhang and chi to chi

# Calculate the total volume of the granary
總體積 = 廣 * 長 * 深  # Total volume in cubic chi

# Dimensions of the pillars
柱圓 = 3  # Diameter in chi
柱長 = 1 * 10 + 2  # Length in chi
柱數 = 2  # Number of pillars

# Calculate the volume of the pillars
柱體積 = (柱圓 ** 2) * 柱長 * 柱數  # Volume in cubic chi
柱體積 = Fraction(柱體積, 12)  # Convert to cubic chi by dividing by 12

# Dimensions of the first set of beams (5 cun square)
牽邊 = Fraction(5, 10)  # Side length in chi (convert from cun to chi)
牽長 = 2 * 10 + 6  # Length in chi
牽數 = 2  # Number of beams

# Calculate the volume of the first set of beams
牽體積 = (牽邊 ** 2) * 牽長 * 牽數  # Volume in cubic chi

# Dimensions of the second set of beams (3 chi square)
梁邊 = 3  # Side length in chi
梁長 = 2 * 10 + 6  # Length in chi
梁數 = 2  # Number of beams

# Calculate the volume of the second set of beams
梁體積 = (梁邊 ** 2) * 梁長 * 梁數  # Volume in cubic chi

# Total volume of the pillars and beams
內部體積 = 柱體積 + 牽體積 + 梁體積

# Subtract the internal structures' volume from the total granary volume
剩餘體積 = 總體積 - 內部體積

# "Hu" divisor (1 hu = 10 cubic chi)
斛法 = 10

# Calculate the millet capacity
a = Fraction(剩餘體積, 斛法)  # Capacity in hu
"""
Variable 'a' has wrong value. Expected: 505450/81, Actual: 10109/10"""
