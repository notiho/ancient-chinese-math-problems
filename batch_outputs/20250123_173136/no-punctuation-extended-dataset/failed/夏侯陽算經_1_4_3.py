"""
今有倉廣二丈六尺長三丈四尺深一丈二尺中有二柱長一丈二尺圓三尺牽二枚長二丈六尺方五寸梁二枚長二丈六尺方三尺問受粟幾何
術曰置廣長相乗以其深乗得一萬六百八尺柱圓三尺自相乗得九尺以乗其長得一百八尺倍之得二百一十六尺以十二除之得一十八尺牽方自相乗退位得二寸五分復乗其長得六尺五寸倍之得一十三尺梁方自乗得九尺復乗其長得二百三十四尺倍之得四百六十八尺并柱牽梁得四百九十九尺以減大數餘一萬一百九尺以斛法除之即粟數
答曰 a斛
"""

"""
Suppose there is a granary with a width of 2 zhang 6 chi, a length of 3 zhang 4 chi, and a depth of 1 zhang 2 chi.
Inside, there are:
- 2 pillars, each 1 zhang 2 chi long and 3 chi in diameter (circular cross-section),
- 2 beams, each 2 zhang 6 chi long and 5 cun square in cross-section,
- 2 beams, each 2 zhang 6 chi long and 3 chi square in cross-section.

Question: How much millet can the granary hold?

The procedure says:
1. Multiply the width and length, then multiply by the depth to get the total volume.
2. For the pillars:
   - Square the diameter (3 chi), multiply by the length, and double it (for 2 pillars).
   - Divide by 12 to convert to cubic chi.
3. For the beams with square cross-sections:
   - For the smaller beams (5 cun square):
     - Square the side length (5 cun), convert to chi, multiply by the length, and double it (for 2 beams).
   - For the larger beams (3 chi square):
     - Square the side length (3 chi), multiply by the length, and double it (for 2 beams).
4. Add the volumes of the pillars and beams, then subtract from the total volume.
5. Divide the remaining volume by the hu divisor to get the millet capacity.

Answer: *a* hu.
"""

from fractions import Fraction

# Dimensions of the granary
廣 = 2 * 10 + 6  # Convert zhang and chi to chi (1 zhang = 10 chi)
長 = 3 * 10 + 4  # Convert zhang and chi to chi
深 = 1 * 10 + 2  # Convert zhang and chi to chi

# Step 1: Calculate the total volume of the granary
總體積 = 廣 * 長 * 深  # Total volume in cubic chi

# Dimensions of the pillars
柱圓 = 3  # Diameter in chi
柱長 = 1 * 10 + 2  # Length in chi
柱數 = 2  # Number of pillars

# Step 2: Calculate the volume of the pillars
柱截面積 = (柱圓 / 2) ** 2 * 3.141592653589793  # Area of circular cross-section (πr^2)
柱體積 = 柱截面積 * 柱長 * 柱數  # Total volume of pillars

# Dimensions of the smaller beams
牽邊 = 5 / 10  # Side length in chi (convert from cun to chi, 1 chi = 10 cun)
牽長 = 2 * 10 + 6  # Length in chi
牽數 = 2  # Number of smaller beams

# Step 3: Calculate the volume of the smaller beams
牽截面積 = 牽邊 ** 2  # Area of square cross-section
牽體積 = 牽截面積 * 牽長 * 牽數  # Total volume of smaller beams

# Dimensions of the larger beams
梁邊 = 3  # Side length in chi
梁長 = 2 * 10 + 6  # Length in chi
梁數 = 2  # Number of larger beams

# Step 4: Calculate the volume of the larger beams
梁截面積 = 梁邊 ** 2  # Area of square cross-section
梁體積 = 梁截面積 * 梁長 * 梁數  # Total volume of larger beams

# Step 5: Calculate the total volume of the obstructions
障礙體積 = 柱體積 + 牽體積 + 梁體積  # Total volume of obstructions

# Step 6: Subtract the obstructions from the total volume
淨體積 = 總體積 - 障礙體積  # Net volume available for millet

# Step 7: Convert to hu (1 hu = 100 cubic chi)
粟數 = Fraction(淨體積, 100)  # Convert to hu

a = 粟數  # Final answer in hu
"""
Code error: both arguments should be Rational instances"""
