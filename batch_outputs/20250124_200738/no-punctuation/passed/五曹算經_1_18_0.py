"""
今有田從一百步廣四十二步中有圓池周三十步徑一十步問池占外為田㡬何
術曰列從一百步以廣四十二步乘之得四千二百步為田積又列池周三十步半之得一十五步列徑一十步半之得五步二位相乘得七十五步為池積以減田積餘四千一百二十五步以畝法除之即得
答曰 a畝 奇 b步 
"""

#----- content starts here -----
"""
Suppose there is a rectangular field with a length of 100 bu and a width of 42 bu. 
Within the field, there is a circular pond with a circumference of 30 bu and a diameter of 10 bu.
Question: how much area does the pond occupy, and how much remains as usable field?

The procedure says: 
1. Place the length of 100 bu and multiply it by the width of 42 bu, obtaining 4200 bu² as the total field area.
2. Place the circumference of the pond, 30 bu, and halve it, obtaining 15 bu as the radius.
3. Place the diameter of the pond, 10 bu, and halve it, obtaining 5 bu as the radius.
4. Multiply the two radii (15 bu and 5 bu), obtaining 75 bu² as the pond area.
5. Subtract the pond area from the total field area, leaving 4125 bu² as the remaining field area.
6. Divide the remaining area by the mu-divisor (240 bu² per mu) to obtain the result.

Answer: *a* mu and *b* bu.
"""

from fractions import Fraction

# Rectangular field dimensions
從 = 100  # Length in bu
廣 = 42   # Width in bu

# Pond dimensions
池周 = 30  # Circumference in bu
池徑 = 10  # Diameter in bu

# 畝法
畝法 = 240  # 1 mu = 240 bu²

# Step 1: Calculate total field area
田積 = 從 * 廣  # Total field area in bu²

# Step 2: Halve the circumference to get one radius
池周半 = Fraction(池周, 2)  # Half of circumference (radius 1)

# Step 3: Halve the diameter to get the other radius
池徑半 = Fraction(池徑, 2)  # Half of diameter (radius 2)

# Step 4: Multiply the two radii to get the pond area
池積 = 池周半 * 池徑半  # Pond area in bu²

# Step 5: Subtract pond area from total field area
餘積 = 田積 - 池積  # Remaining field area in bu²

# Step 6: Divide remaining area by mu-divisor to get mu and remaining bu
畝數 = 餘積 // 畝法  # Whole mu
餘步 = 餘積 % 畝法  # Remaining bu

a = 畝數
b = 餘步#----- content ends here -----

"""
"""
