"""
今有倉廣二丈六尺長三丈四尺深一丈二尺中有二柱長一丈二尺圓三尺牽二枚長二丈六尺方五寸梁二枚長二丈六尺方三尺問受粟幾何
術曰置廣長相乗以其深乗得一萬六百八尺柱圓三尺自相乗得九尺以乗其長得一百八尺倍之得二百一十六尺以十二除之得一十八尺牽方自相乗退位得二寸五分復乗其長得六尺五寸倍之得一十三尺梁方自乗得九尺復乗其長得二百三十四尺倍之得四百六十八尺并柱牽梁得四百九十九尺以減大數餘一萬一百九尺以斛法除之即粟數
答曰 a斛
"""

"""
Suppose there is a granary with a width of 2 zhang and 6 chi, a length of 3 zhang and 4 chi, and a depth of 1 zhang and 2 chi.
Inside, there are:
- 2 pillars, each 1 zhang and 2 chi long, with a circular cross-section of 3 chi in diameter,
- 2 beams, each 2 zhang and 6 chi long, with a square cross-section of 5 cun per side,
- 2 additional beams, each 2 zhang and 6 chi long, with a square cross-section of 3 chi per side.

Question: How much millet can the granary hold?

The procedure says:
1. Multiply the width and length, then multiply by the depth to get the total volume.
2. For the pillars:
   - Square the diameter (3 chi), multiply by the length, and double it (for 2 pillars).
   - Divide by 12 to account for the circular cross-section.
3. For the beams with square cross-sections:
   - For the beams with 5 cun sides:
     - Square the side length (convert to chi), multiply by the length, and double it (for 2 beams).
   - For the beams with 3 chi sides:
     - Square the side length, multiply by the length, and double it (for 2 beams).
4. Add the volumes of the pillars and beams, then subtract from the total volume.
5. Divide the remaining volume by the "hu method" (10 chi³ per hu) to get the millet capacity.

Answer: *a* hu.
"""

from fractions import Fraction

# Dimensions of the granary
廣 = 2 * 10 + 6  # Convert to chi (2 zhang 6 chi = 26 chi)
長 = 3 * 10 + 4  # Convert to chi (3 zhang 4 chi = 34 chi)
深 = 1 * 10 + 2  # Convert to chi (1 zhang 2 chi = 12 chi)

# Step 1: Total volume of the granary
總體積 = 廣 * 長 * 深  # Total volume in chi³

# Dimensions of the pillars
柱長 = 1 * 10 + 2  # Convert to chi (1 zhang 2 chi = 12 chi)
柱圓直徑 = 3  # Diameter in chi

# Step 2: Volume of the pillars
柱圓半徑 = Fraction(柱圓直徑, 2)  # Radius = diameter / 2
柱截面積 = (柱圓半徑 ** 2) * 3.141592653589793  # Area of circular cross-section (πr²)
柱體積 = 柱截面積 * 柱長  # Volume of one pillar
柱總體積 = 2 * 柱體積  # Total volume for 2 pillars

# Step 3: Volume of the beams
# Beams with 5 cun sides
牽方邊長 = Fraction(5, 10)  # Convert to chi (5 cun = 0.5 chi)
牽長 = 2 * 10 + 6  # Convert to chi (2 zhang 6 chi = 26 chi)
牽截面積 = 牽方邊長 ** 2  # Area of square cross-section
牽體積 = 牽截面積 * 牽長  # Volume of one beam
牽總體積 = 2 * 牽體積  # Total volume for 2 beams

# Beams with 3 chi sides
梁方邊長 = 3  # Side length in chi
梁長 = 2 * 10 + 6  # Convert to chi (2 zhang 6 chi = 26 chi)
梁截面積 = 梁方邊長 ** 2  # Area of square cross-section
梁體積 = 梁截面積 * 梁長  # Volume of one beam
梁總體積 = 2 * 梁體積  # Total volume for 2 beams

# Step 4: Subtract the volumes of the pillars and beams from the total volume
內部體積 = 總體積 - (柱總體積 + 牽總體積 + 梁總體積)

# Step 5: Convert the remaining volume to hu (1 hu = 10 chi³)
粟數 = Fraction(內部體積, 10)

a = 粟數  # Final answer in hu
"""
Code error: both arguments should be Rational instances"""
