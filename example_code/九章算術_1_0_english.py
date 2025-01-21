#今有田廣十五步，從十六步。問：為田幾何？
#荅曰： a畝 。

"""
Suppose there is a field with a width of 15 bu and a length of 16 bu.
Question: how large of a field does it make?

The answer says: *a* mu.
"""

#廣十五步
廣步數 = 15

#從十六步
從步數 = 16

#Multiply the number of bu in width and height
area_in_bu = 廣步數 * 從步數

# Convert into mu 
a = Fraction(area_in_bu, 240)
