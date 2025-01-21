"""
今有圭田廣十二步，正從二十一步。問：為田幾何？
術曰：半廣以乘正從。
荅曰： a(=126)步 。
"""

"""
Suppose there is a wedge-shaped field with a width of 12 bu and a length of 21 bu.
Question: how large is the field?

The procedure says: Take half the width and multiply it by the length.

The answer says: *a*(=126) bu.
"""

# 廣十二步
廣 = 12

# 正從二十一步
正從 = 21

# 半廣以乘正從
半廣 = Fraction(廣, 2)
a = 半廣 * 正從 # 126
"""
"""
