"""
今有倉廣二丈六尺長三丈四尺深一丈二尺中有二柱長一丈二尺圓三尺牽二枚長二丈六尺方五寸梁二枚長二丈六尺方三尺問受粟幾何
術曰置廣長相乗以其深乗得一萬六百八尺柱圓三尺自相乗得九尺以乗其長得一百八尺倍之得二百一十六尺以十二除之得一十八尺牽方自相乗退位得二寸五分復乗其長得六尺五寸倍之得一十三尺梁方自乗得九尺復乗其長得二百三十四尺倍之得四百六十八尺并柱牽梁得四百九十九尺以減大數餘一萬一百九尺以斛法除之即粟數
答曰 a斛
"""

"""
Suppose there is a granary with a width of 2 zhang 6 chi, a length of 3 zhang 4 chi, and a depth of 1 zhang 2 chi.
Inside, there are:
- 2 pillars, each with a length of 1 zhang 2 chi and a circular cross-section of 3 chi in diameter,
- 2 beams, each with a length of 2 zhang 6 chi and a square cross-section of 5 cun,
- 2 additional beams, each with a length of 2 zhang 6 chi and a square cross-section of 3 chi.

Question: how much millet can the granary hold?

The procedure says:
1. Multiply the width and length, then multiply by the depth to get the total volume.
2. For the pillars:
   - Square the diameter of the circular cross-section.
   - Multiply by the length of the pillar.
   - Double the result (for 2 pillars).
   - Divide by 12 to convert to cubic chi.
3. For the beams with a square cross-section of 5 cun:
   - Square the side length (convert to chi first).
   - Multiply by the length of the beam.
   - Double the result (for 2 beams).
4. For the beams with a square cross-section of 3 chi:
   - Square the side length.
   - Multiply by the length of the beam.
   - Double the result (for 2 beams).
5. Add the volumes of the pillars and beams, then subtract from the total volume.
6. Divide the remaining volume by the "hu" conversion factor to get the millet capacity.

Answer: *a* hu.
"""

from fractions import Fraction

# Dimensions of the granary
廣 = 2 * 10 + 6  # Convert zhang and chi to chi
長 = 3 * 10 + 4  # Convert zhang and chi to chi
深 = 1 * 10 + 2  # Convert zhang and chi to chi

# Step 1: Calculate total volume of the granary
總體積 = 廣 * 長 * 深  # Total volume in cubic chi

# Dimensions of the pillars
柱長 = 1 * 10 + 2  # Convert zhang and chi to chi
柱圓直徑 = 3  # Diameter in chi
柱半徑 = Fraction(柱圓直徑, 2)  # Radius in chi

# Step 2: Calculate volume of the pillars
柱截面積 = (柱半徑 ** 2) * 3.141592653589793  # Area of circular cross-section (πr^2)
柱體積 = 柱截面積 * 柱長  # Volume of one pillar
柱總體積 = 2 * 柱體積  # Total volume for 2 pillars
柱總體積 = 柱總體積 / 12  # Convert to cubic chi

# Dimensions of the beams with a square cross-section of 5 cun
牽長 = 2 * 10 + 6  # Convert zhang and chi to chi
牽方邊長 = Fraction(5, 10)  # Convert cun to chi

# Step 3: Calculate volume of the beams with a square cross-section of 5 cun
牽截面積 = 牽方邊長 ** 2  # Area of square cross-section
牽體積 = 牽截面積 * 牽長  # Volume of one beam
牽總體積 = 2 * 牽體積  # Total volume for 2 beams

# Dimensions of the beams with a square cross-section of 3 chi
梁長 = 2 * 10 + 6  # Convert zhang and chi to chi
梁方邊長 = 3  # Side length in chi

# Step 4: Calculate volume of the beams with a square cross-section of 3 chi
梁截面積 = 梁方邊長 ** 2  # Area of square cross-section
梁體積 = 梁截面積 * 梁長  # Volume of one beam
梁總體積 = 2 * 梁體積  # Total volume for 2 beams

# Step 5: Subtract the volumes of the pillars and beams from the total volume
總減體積 = 總體積 - (柱總體積 + 牽總體積 + 梁總體積)

# Step 6: Convert the remaining volume to hu
斛法 = 100  # 1 hu = 100 cubic chi
a = Fraction(總減體積, 斛法)  # Millet capacity in hu

a
"""
Code error: both arguments should be Rational instances"""
