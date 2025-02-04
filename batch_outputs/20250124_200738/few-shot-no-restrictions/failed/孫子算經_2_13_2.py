"""
今有方田桑生中央，從角至桑，一百四十七步。問：為田幾何？
術曰：置角至桑一百四十七步，倍之，得二百九十四步，以五乘之，得一千四百七十步，以七除之，得二百一十步，自相乘，得四萬四千一百步，以二百四十步除之，即得。
答曰： a頃 ，奇 b步 。
"""

#----- content starts here -----
"""
Suppose there is a square field with a mulberry tree growing at its center.
From one corner of the field to the mulberry tree, the distance is 147 bu.
Question: how large is the field?

The procedure says: Take the distance from the corner to the mulberry tree, 147 bu, and double it, obtaining 294 bu.
Multiply it by 5, obtaining 1470 bu.
Divide it by 7, obtaining 210 bu.
Square this value, obtaining 44100 bu.
Divide it by 240 bu (the mu divisor), obtaining the area in mu.
Convert the result into qing and remaining bu.

Answer: *a* qing, with *b* bu remaining.
"""

from fractions import Fraction

# Given data
角至桑 = 147  # Distance from corner to mulberry tree in bu

# Step 1: Double the distance
倍步 = 2 * 角至桑  # 294 bu

# Step 2: Multiply by 5
乘五 = 5 * 倍步  # 1470 bu

# Step 3: Divide by 7
除七 = Fraction(乘五, 7)  # 210 bu

# Step 4: Square the result
田積步 = 除七 ** 2  # 44100 bu

# Step 5: Divide by 240 to get the area in mu
畝數 = Fraction(田積步, 240)  # 183 mu and 180/240 mu

# Step 6: Convert to qing and remaining bu
畝每頃 = 100  # 1 qing = 100 mu
a = 畝數 // 畝每頃  # Whole qing
b = 畝數 % 畝每頃  # Remaining mu

# Final result
a = int(a)  # Convert qing to integer
b = b  # Remaining mu as a fraction
#----- content ends here -----

"""
Variable 'a' has wrong value. Expected: 183/100, Actual: 1
Variable 'b' has wrong value. Expected: 180, Actual: 335/4"""
