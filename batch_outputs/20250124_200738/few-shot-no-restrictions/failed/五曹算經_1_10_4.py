"""
今有田桑生中央從隅至桑一百四十七步。問：為田㡬何？
術曰：列一百四十七步以二乘之得二百九十四步以五乘之得一千四百七十步以七除之得二百一十步自相乘得四萬四千一百步以畝法除之即得。
答曰： a頃 奇 b步 。
"""

#----- content starts here -----
"""
Suppose there is a field with a mulberry tree in the center. From the corner of the field to the mulberry tree is 147 bu.
Question: how large is the field?

The procedure says: Take 147 bu, multiply it by 2, obtaining 294 bu.
Multiply this by 5, obtaining 1470 bu.
Divide this by 7, obtaining 210 bu.
Square this value, obtaining 44100 bu.
Divide this by the mu-divisor (240 bu per mu), obtaining the area in mu.
Convert the result into qing (1 qing = 100 mu) and remaining bu.

Answer: *a* qing and *b* bu.
"""

from fractions import Fraction

# Given: From the corner to the mulberry tree is 147 bu
corner_to_mulberry = 147

# Step 1: Multiply by 2
step1 = 2 * corner_to_mulberry

# Step 2: Multiply by 5
step2 = 5 * step1

# Step 3: Divide by 7
step3 = Fraction(step2, 7)

# Step 4: Square the result
area_in_bu = step3 ** 2

# Step 5: Divide by the mu-divisor (240 bu per mu)
mu_divisor = 240
area_in_mu = Fraction(area_in_bu, mu_divisor)

# Convert to qing and remaining bu
qing = area_in_mu // 100  # 1 qing = 100 mu
remaining_mu = area_in_mu % 100

# Final answer
a = qing
b = remaining_mu
#----- content ends here -----

"""
Variable 'a' has wrong value. Expected: 183/100, Actual: 1
Variable 'b' has wrong value. Expected: 180, Actual: 335/4"""
