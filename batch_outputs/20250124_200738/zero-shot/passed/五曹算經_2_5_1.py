"""
今有兵一千三百六十二人，人給絹二丈八尺五寸。問：計㡬何？
術曰：列兵一千三百六十二人，以絹二十八尺五寸乘之，得三萬八千八百一十七尺，以四十尺除之即得。
答曰： a疋 。
"""

"""
To solve this problem, we need to calculate how many bolts of silk ("疋") are required to distribute to 1,362 soldiers, where each soldier is given 2丈8尺5寸 of silk. 

1丈 = 10尺, and 1疋 = 40尺. First, we convert the given amount of silk per person into 尺, then calculate the total silk required, and finally divide by 40 to determine the number of bolts.

Here's the Python code:


"""

#----- content starts here -----

from fractions import Fraction

# Given data
soldiers = 1362
silk_per_person = 2 * 10 + 8 + Fraction(5, 10)  # Convert 2丈8尺5寸 to 尺
total_silk = soldiers * silk_per_person  # Total silk in 尺
a = total_silk / 40  # Convert total silk to 疋

# Result
a
#----- content ends here -----


"""


This will compute the value of `a` in terms of bolts of silk ("疋").
"""


"""
"""
