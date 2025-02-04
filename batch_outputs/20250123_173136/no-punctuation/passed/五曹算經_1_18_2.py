"""
今有田從一百步廣四十二步中有圓池周三十步徑一十步問池占外為田㡬何
術曰列從一百步以廣四十二步乘之得四千二百步為田積又列池周三十步半之得一十五步列徑一十步半之得五步二位相乘得七十五步為池積以減田積餘四千一百二十五步以畝法除之即得
答曰 a畝 奇 b步 
"""

"""
Suppose there is a rectangular field with a length of 100 bu and a width of 42 bu. 
Within it, there is a circular pond with a circumference of 30 bu and a diameter of 10 bu.
Question: how much of the field is occupied by the pond, and how much remains as usable field?

The procedure says: 
List the length of 100 bu and multiply it by the width of 42 bu, obtaining 4200 bu as the total field area.
Next, list the circumference of the pond, 30 bu, and halve it, obtaining 15 bu as the radius.
List the diameter, 10 bu, and halve it, obtaining 5 bu as the radius (confirming consistency).
Multiply the two radii, obtaining 75 bu as the pond area.
Subtract the pond area from the total field area, leaving 4125 bu.
Divide this by the mu-divisor (240 bu), obtaining the remaining field in mu and bu.

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

# Calculate the total field area
田積 = 從 * 廣  # Total field area in bu²

# Calculate the pond area
池半周 = Fraction(池周, 2)  # Half the circumference (radius)
池半徑 = Fraction(池徑, 2)  # Half the diameter (radius, consistency check)
池積 = 池半周 * 池半徑  # Pond area in bu²

# Subtract the pond area from the total field area
餘田積 = 田積 - 池積  # Remaining field area in bu²

# Convert the remaining field area to mu and bu
a = 餘田積 // 畝法  # Whole mu
b = 餘田積 % 畝法  # Remaining bu

a = int(a)
b = int(b)
"""
"""
