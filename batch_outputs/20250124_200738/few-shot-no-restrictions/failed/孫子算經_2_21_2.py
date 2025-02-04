"""
今有築城，上廣二丈，下廣五丈四尺，高三丈八尺，長五千五百五十尺，秋程人功三百尺。問：須功幾何？
術曰：置里數以三百步乘之，內零步，六之，得五萬二千八百二十四尺，并上下廣，得二丈六寸，半之，以深乘之，得一百八十五尺四寸，以長乘得九百七十九萬三千五百六十九尺六寸，以人功三百尺除之，即得。
答曰： a功 。
"""

#----- content starts here -----
"""
Suppose there is a city wall to be built. The top width is 2 zhang, the bottom width is 5 zhang 4 chi, the height is 3 zhang 8 chi, and the length is 5550 chi. 
One person can complete 300 chi of work in a day. 
Question: How many person-days of labor are required?

The procedure says: 
1. Place the length in li (convert to chi) and multiply by 300 chi. 
2. Add the remainder chi (if any) and multiply by 6, obtaining the total chi. 
3. Add the top and bottom widths, obtaining 2 zhang 6 chi. 
4. Halve this value, then multiply by the depth (height), obtaining the cross-sectional area. 
5. Multiply this by the length to obtain the total volume. 
6. Divide the total volume by the work rate (300 chi per person-day) to obtain the required labor.

Answer: *a* person-days of labor.
"""

from fractions import Fraction

# Input values
上廣 = 2  # zhang
下廣 = 5 + Fraction(4, 10)  # 5 zhang 4 chi = 5.4 zhang
高 = 3 + Fraction(8, 10)  # 3 zhang 8 chi = 3.8 zhang
長 = 5550  # chi
人功 = 300  # chi per person-day

# Step 1: Add top and bottom widths
總廣 = 上廣 + 下廣  # 2 zhang + 5.4 zhang = 7.4 zhang

# Step 2: Halve the total width
平均廣 = 總廣 / 2  # 7.4 zhang / 2 = 3.7 zhang

# Step 3: Multiply by the height to get the cross-sectional area
橫截面積 = 平均廣 * 高  # 3.7 zhang * 3.8 zhang = 14.06 zhang^2

# Step 4: Multiply by the length to get the total volume
總體積 = 橫截面積 * 長  # 14.06 zhang^2 * 5550 chi = 77913 zhang * chi

# Step 5: Convert volume to chi^3 (1 zhang = 10 chi)
總體積_尺 = 總體積 * 10  # 77913 zhang * chi * 10 = 779130 chi^3

# Step 6: Divide by the work rate to get the required labor
所需功 = 總體積_尺 / 人功  # 779130 chi^3 / 300 chi/person-day

# Final answer
a = 所需功
a#----- content ends here -----

"""
Variable 'a' has wrong value. Expected: 26011, Actual: 26011/10"""
