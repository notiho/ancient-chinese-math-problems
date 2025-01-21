"""
今有圭田廣十二步正從二十一步問為田幾何
術曰半廣以乘正從
荅曰 a步 
"""

"""
Suppose there is a wedge-shaped field with a width of 12 bu and a length of 21 bu.
Question: how large of a field does it make?

The procedure says: Take half of the width and multiply it by the length.

The answer says: *a* bu.
"""

# 廣十二步
廣 = 12

# 正從二十一步
正從 = 21

# 半廣
半廣 = Fraction(廣, 2)

# 以乘正從
a = 半廣 * 正從
"""
"""
