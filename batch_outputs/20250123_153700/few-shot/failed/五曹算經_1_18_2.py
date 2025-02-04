"""
今有田從一百步廣四十二步中有圓池周三十步徑一十步。問：池占外為田㡬何？
術曰：列從一百步以廣四十二步乘之得四千二百步為田積又列池周三十步半之得一十五步列徑一十步半之得五步二位相乘得七十五步為池積以減田積餘四千一百二十五步以畝法除之即得。
答曰： a畝 奇 b步 。
"""

"""
Suppose there is a rectangular field with a length of 100 bu and a width of 42 bu. 
Within this field, there is a circular pond with a circumference of 30 bu and a diameter of 10 bu.
Question: how much of the field remains as usable land outside the pond?

The procedure says: 
1. Take the length of 100 bu and multiply it by the width of 42 bu, obtaining 4200 bu² as the total field area.
2. Take the circumference of the pond, 30 bu, and halve it, obtaining 15 bu as the radius.
3. Take the diameter of the pond, 10 bu, and halve it, obtaining 5 bu as the radius (this confirms the radius is consistent).
4. Multiply the two radii (15 bu and 5 bu), obtaining 75 bu² as the pond area.
5. Subtract the pond area from the total field area, leaving 4125 bu² as the remaining field area.
6. Divide the remaining field area by the mu-divisor (240 bu per mu) to convert it into mu and bu.

Answer: *a* mu and *b* bu.
"""

from fractions import Fraction

# Field dimensions
從 = 100  # Length of the field in bu
廣 = 42   # Width of the field in bu

# Pond dimensions
池周 = 30  # Circumference of the pond in bu
池徑 = 10  # Diameter of the pond in bu

# 畝法
畝法 = 240  # 1 mu = 240 bu²

# Step 1: Calculate the total field area
田積 = 從 * 廣  # Total field area in bu²

# Step 2: Calculate the radius of the pond from the circumference
池半周 = Fraction(池周, 2)  # Half of the circumference (radius from circumference)

# Step 3: Calculate the radius of the pond from the diameter
池半徑 = Fraction(池徑, 2)  # Half of the diameter (radius from diameter)

# Confirm the radius is consistent (池半周 and 池半徑 should be equal)
assert 池半周 == 池半徑

# Step 4: Calculate the pond area
池積 = 池半周 * 池半徑  # Pond area in bu²

# Step 5: Subtract the pond area from the total field area
餘積 = 田積 - 池積  # Remaining field area in bu²

# Step 6: Convert the remaining field area into mu and bu
a = 餘積 // 畝法  # Whole mu
b = 餘積 % 畝法  # Remaining bu

a, b  # Final answer in mu and bu
"""
Code error: """
