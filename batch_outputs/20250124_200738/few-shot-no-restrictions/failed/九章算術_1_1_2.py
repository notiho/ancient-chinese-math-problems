"""
又有田廣十二步，從十四步。問：為田幾何？
方田術曰：廣從步數相乘得積步。以畝法二百四十步除之，即畝數。百畝為一頃。
荅曰： a步 。
"""

#----- content starts here -----
"""
Suppose there is a field with a width of 12 bu and a length of 14 bu.
Question: how large of a field does it make?

The procedure for rectangular fields says: Multiply the width and length (in bu) to obtain the total area in bu².
Divide the total area by the mu-divisor, 240, to get the area in mu.
100 mu make 1 qing.

The answer says: *a* mu.
"""

from fractions import Fraction

# 廣十二步
廣步數 = 12

# 從十四步
從步數 = 14

# 廣從步數相乘得積步
積步 = 廣步數 * 從步數

# 畝法二百四十步
畝法 = 240

# 以畝法二百四十步除之，即畝數
畝數 = Fraction(積步, 畝法)

a = 畝數
print(f"田的面積為 {a} 畝。")#----- content ends here -----

"""
Variable 'a' has wrong value. Expected: 168, Actual: 7/10"""
