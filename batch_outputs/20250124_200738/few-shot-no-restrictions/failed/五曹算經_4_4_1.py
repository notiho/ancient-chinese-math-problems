"""
今有圓囷周三丈，高一丈六尺。問：受粟㡬何？
術曰：列周三丈自相乘得九百尺以高一丈六尺乘之得一萬四千四百尺以十二除之得一千二百尺以斛法一尺六寸二分除之即得。
答曰： a斛 奇 b尺 。
"""

#----- content starts here -----
"""
Suppose there is a cylindrical granary with a circumference of 3 zhang and a height of 1 zhang 6 chi.
Question: how much millet can it hold?

The procedure says: Take the circumference of 3 zhang, square it to get 900 chi².
Multiply this by the height of 1 zhang 6 chi to get 14400 chi³.
Divide this by 12 to get 1200 chi³.
Finally, divide this by the volume of 1 hu (1 chi 6 cun 2 fen) to get the result.

Answer: *a* hu and *b* chi³.
"""

from fractions import Fraction

# Constants
circumference = 3 * 10  # 3 zhang = 30 chi
height = 1 * 10 + 6  # 1 zhang 6 chi = 16 chi
hu_volume = 1 * 10 + 6 + Fraction(2, 10)  # 1 chi 6 cun 2 fen = 16.2 chi³
divisor = 12  # Conversion factor for cylindrical volume

# Step 1: Square the circumference
base_area = circumference ** 2  # chi²

# Step 2: Multiply by the height
volume = base_area * height  # chi³

# Step 3: Divide by 12
adjusted_volume = volume / divisor  # chi³

# Step 4: Divide by the volume of 1 hu
hu_count = adjusted_volume // hu_volume  # Integer part (number of hu)
remaining_volume = adjusted_volume % hu_volume  # Remainder (chi³)

# Results
a = hu_count
b = remaining_volume

a, b#----- content ends here -----

"""
Variable 'a' has wrong value. Expected: 740, Actual: 74.0
Variable 'b' has wrong value. Expected: 6/5, Actual: 1.2000000000000526"""
