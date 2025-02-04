"""
又有田廣十二步，從十四步。問：為田幾何？
方田術曰：廣從步數相乘得積步。以畝法二百四十步除之，即畝數。百畝為一頃。
荅曰： a(=168)步 。
"""

"""
Suppose there is a field with a width of 12 bu and a length of 14 bu.
Question: how large of a field does it make?

The procedure for rectangular fields says: The numbers of bu in width and length are multiplied with each other, obtaining the [number of] accumulated bu.
When dividing it by the mu-divisor, 240, it is the number of mu.
100 mu make 1 qing.

The answer says: *a*(=168) bu.
"""

# 廣十二步
廣步數 = 12

# 從十四步
從步數 = 14

# 廣從步數相乘得積步
積步 = 廣步數 * 從步數

# 積步即為田面積，單位為步
a = 積步 # 168
"""
"""
