"""
今有鋼鐵二千五百斤依前所耗數卻求為黄鐵問得幾何
術曰置鋼鐵數一十六乗之一十三除之即得
答曰黄鐵 a斤
"""

"""
Suppose there are 2500 jin of steel. Based on the previous consumption ratio, it is desired to convert it into yellow iron.
Question: how much yellow iron is obtained?

The procedure says: Place the amount of steel. Multiply it by 13 and divide it by 16, and the result is obtained.

Answer: it makes *a* jin of yellow iron.
"""

# 鋼鐵二千五百斤
鋼鐵 = 2500

# 一十六乗之一十三
黃鐵 = 13 * 鋼鐵

# 除之即得
a = Fraction(黃鐵, 16)
"""
Variable 'a' has wrong value. Expected: 40000/13, Actual: 8125/4"""
