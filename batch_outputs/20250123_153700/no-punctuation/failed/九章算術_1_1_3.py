"""
又有田廣十二步從十四步問為田幾何
方田術曰廣從步數相乘得積步以畝法二百四十步除之即畝數百畝為一頃
荅曰 a步 
"""

"""
Suppose there is a field with a width of 12 bu and a length of 14 bu.
Question: how large of a field does it make?

The procedure for rectangular fields says: The numbers of bu in width and length are multiplied with each other, obtaining the [number of] accumulated bu.
When dividing it by the mu-divisor, 240, it is the number of mu.
100 mu make 1 qing.

The answer says: *a* mu.
"""

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
"""
Variable 'a' has wrong value. Expected: 168, Actual: 7/10"""
