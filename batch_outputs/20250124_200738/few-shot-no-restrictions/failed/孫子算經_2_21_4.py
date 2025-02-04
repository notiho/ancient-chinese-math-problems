"""
今有築城，上廣二丈，下廣五丈四尺，高三丈八尺，長五千五百五十尺，秋程人功三百尺。問：須功幾何？
術曰：置里數以三百步乘之，內零步，六之，得五萬二千八百二十四尺，并上下廣，得二丈六寸，半之，以深乘之，得一百八十五尺四寸，以長乘得九百七十九萬三千五百六十九尺六寸，以人功三百尺除之，即得。
答曰： a功 。
"""

#----- content starts here -----
"""
Suppose there is a wall being constructed. The top width is 2 zhang, the bottom width is 5 zhang 4 chi, the height is 3 zhang 8 chi, and the length is 5550 chi. 
One person can complete 300 chi of work in one day. 
Question: how many person-days of work are required?

The procedure says: 
1. Place the length in li (convert to chi by multiplying by 300). Add any remaining chi, then multiply by 6, obtaining the total length in chi.
2. Add the top and bottom widths, obtaining 2 zhang 6 chi. Halve this to get the average width.
3. Multiply the average width by the height, obtaining the cross-sectional area.
4. Multiply the cross-sectional area by the total length, obtaining the total volume of the wall.
5. Divide the total volume by the amount of work one person can complete in a day (300 chi), obtaining the total number of person-days required.

Answer: *a* person-days.
"""

from fractions import Fraction

# Given dimensions
上廣 = 2  # in zhang
下廣 = 5 + Fraction(4, 10)  # 5 zhang 4 chi (convert chi to zhang, 1 zhang = 10 chi)
高 = 3 + Fraction(8, 10)  # 3 zhang 8 chi (convert chi to zhang)
長 = 5550  # in chi
人功 = 300  # chi per person-day

# Step 1: Convert length to chi and multiply by 6
總長 = 長 * 6  # Total length in chi

# Step 2: Add top and bottom widths, then halve to get the average width
平均廣 = (上廣 + 下廣) / 2  # Average width in zhang

# Step 3: Multiply average width by height to get cross-sectional area
橫截面積 = 平均廣 * 高  # Cross-sectional area in zhang^2

# Step 4: Multiply cross-sectional area by total length to get total volume
總體積 = 橫截面積 * 總長  # Total volume in zhang^3

# Step 5: Divide total volume by work per person-day to get total person-days
a = 總體積 / 人功  # Total person-days required

# Convert the result to chi for clarity
a_in_chi = a * 10  # Convert zhang^3 to chi^3 if needed

a#----- content ends here -----

"""
Variable 'a' has wrong value. Expected: 26011, Actual: 78033/50"""
