"""
今有圭田從三十步一頭廣二十四步一頭無步。問：為田㡬何？
答曰： a畝 奇 b步 。
"""

#----- content starts here -----
"""
Suppose there is a wedge-shaped field (圭田) with one side of length 30 bu, the other side of length 24 bu, and the narrow end is 0 bu.
Question: how large is the area of the field?

Answer: it is *a* mu and *b* bu.
"""

from fractions import Fraction

# Field dimensions
長邊 = 30  # 30 bu
短邊 = 24  # 24 bu
窄端 = 0   # 0 bu

# Average width of the field
平均廣 = Fraction(長邊 + 短邊 + 窄端, 3)

# Area in bu²
面積_步 = 平均廣 * 長邊

# Convert to mu and remaining bu
a = 面積_步 // 240  # 1 mu = 240 bu²
b = 面積_步 % 240

a, b  # Output the result as (a mu, b bu)#----- content ends here -----

"""
Variable 'a' has wrong value. Expected: 1, Actual: 2
Variable 'b' has wrong value. Expected: 120, Actual: 60"""
