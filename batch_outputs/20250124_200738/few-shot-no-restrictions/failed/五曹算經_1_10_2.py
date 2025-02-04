"""
今有田桑生中央從隅至桑一百四十七步。問：為田㡬何？
術曰：列一百四十七步以二乘之得二百九十四步以五乘之得一千四百七十步以七除之得二百一十步自相乘得四萬四千一百步以畝法除之即得。
答曰： a頃 奇 b步 。
"""

#----- content starts here -----
"""
Suppose there is a square field with a mulberry tree in the center. The distance from a corner of the field to the mulberry tree is 147 bu.
Question: how large is the area of the field?

The procedure says: Take 147 bu and multiply it by 2, obtaining 294 bu. Multiply this by 5, obtaining 1470 bu. Divide this by 7, obtaining 210 bu. Square this value, obtaining 44100 bu². Divide this by the mu divisor (240 bu²), obtaining the area in mu.

The answer says: *a* qing and *b* bu.
"""

from fractions import Fraction

# Given data
從隅至桑 = 147  # Distance from the corner to the mulberry tree in bu

# Step 1: Multiply by 2
步_二倍 = 2 * 從隅至桑

# Step 2: Multiply by 5
步_五倍 = 5 * 步_二倍

# Step 3: Divide by 7
田邊長 = Fraction(步_五倍, 7)

# Step 4: Square the side length to get the area in bu²
田積步 = 田邊長 ** 2

# Step 5: Divide by 畝法 (240 bu² per mu) to get the area in mu
畝法 = 240
田積畝 = Fraction(田積步, 畝法)

# Step 6: Convert mu to qing and remaining bu
# 1 qing = 100 mu
頃 = 田積畝 // 100
剩餘畝 = 田積畝 % 100

# Convert the remaining mu to bu for clarity
剩餘步 = 剩餘畝 * 畝法

# Final answer
a = int(頃)  # Number of qing
b = int(剩餘步)  # Remaining bu

a, b  # Output the result as qing and bu#----- content ends here -----

"""
Variable 'a' has wrong value. Expected: 183/100, Actual: 1
Variable 'b' has wrong value. Expected: 180, Actual: 20100"""
