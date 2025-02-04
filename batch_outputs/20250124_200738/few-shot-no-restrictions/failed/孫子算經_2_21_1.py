"""
今有築城，上廣二丈，下廣五丈四尺，高三丈八尺，長五千五百五十尺，秋程人功三百尺。問：須功幾何？
術曰：置里數以三百步乘之，內零步，六之，得五萬二千八百二十四尺，并上下廣，得二丈六寸，半之，以深乘之，得一百八十五尺四寸，以長乘得九百七十九萬三千五百六十九尺六寸，以人功三百尺除之，即得。
答曰： a功 。
"""

#----- content starts here -----
"""
Suppose a city wall is being built. The top width is 2 zhang, the bottom width is 5 zhang 4 chi, the height is 3 zhang 8 chi, and the length is 5550 chi. 
One person's daily work capacity is 300 chi³. 
Question: How many person-days of labor are required?

The procedure says: 
1. Place the length in li (convert to chi by multiplying by 300), and include any remaining chi. Multiply by 6, obtaining 52824 chi.
2. Add the top and bottom widths, obtaining 2 zhang 6 chi. Halve this to get the average width.
3. Multiply the average width by the height, obtaining 185 chi 4 cun.
4. Multiply this by the length, obtaining 9793569 chi³ 6 cun.
5. Divide by the daily work capacity of 300 chi³ to get the number of person-days.

Answer: *a* person-days.
"""

from fractions import Fraction

# Constants
top_width = 2 * 10  # Convert zhang to chi
bottom_width = 5 * 10 + 4  # Convert zhang and chi to chi
height = 3 * 10 + 8  # Convert zhang and chi to chi
length = 5550  # Length in chi
daily_work_capacity = 300  # Daily work capacity in chi³

# Step 1: Multiply length by 6
length_multiplied = length * 6

# Step 2: Add top and bottom widths, then halve to get average width
average_width = Fraction(top_width + bottom_width, 2)

# Step 3: Multiply average width by height
cross_section_area = average_width * height

# Step 4: Multiply cross-section area by length
total_volume = cross_section_area * length_multiplied

# Step 5: Divide total volume by daily work capacity
person_days = Fraction(total_volume, daily_work_capacity)

# Final answer
a = person_days
a#----- content ends here -----

"""
Variable 'a' has wrong value. Expected: 26011, Actual: 156066"""
