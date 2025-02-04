"""
今有田桑生中央從隅至桑一百四十七步。問：為田㡬何？
術曰：列一百四十七步以二乘之得二百九十四步以五乘之得一千四百七十步以七除之得二百一十步自相乘得四萬四千一百步以畝法除之即得。
答曰： a頃 奇 b步 。
"""

#----- content starts here -----
"""
Suppose there is a square field with a mulberry tree in the center. The distance from one corner of the field to the mulberry tree is 147 bu.
Question: how large is the field?

The procedure says: Take 147 bu, multiply it by 2, obtaining 294 bu.
Multiply it by 5, obtaining 1470 bu.
Divide it by 7, obtaining 210 bu.
Square this result, obtaining 44100 bu.
Divide it by the mu-divisor (240 bu per mu), obtaining the area in mu.
Convert the result into qing (100 mu per qing) and remaining bu.

Answer: *a* qing and *b* bu.
"""

from fractions import Fraction

# Given data
隅至桑 = 147  # Distance from corner to the mulberry tree in bu

# Step 1: Multiply by 2
步_1 = 隅至桑 * 2

# Step 2: Multiply by 5
步_2 = 步_1 * 5

# Step 3: Divide by 7
步_3 = Fraction(步_2, 7)

# Step 4: Square the result
積步 = 步_3 ** 2

# Step 5: Divide by 畝法 (240 bu per mu)
畝法 = 240
畝數 = Fraction(積步, 畝法)

# Step 6: Convert to qing (100 mu per qing) and remaining bu
畝每頃 = 100
頃數 = 畝數 // 畝每頃  # Integer part for qing
剩餘畝 = 畝數 % 畝每頃  # Remaining mu

a = int(頃數)  # Number of qing
b = 剩餘畝  # Remaining mu

# Final result
a, b#----- content ends here -----

"""
Variable 'a' has wrong value. Expected: 183/100, Actual: 1
Variable 'b' has wrong value. Expected: 180, Actual: 335/4"""
