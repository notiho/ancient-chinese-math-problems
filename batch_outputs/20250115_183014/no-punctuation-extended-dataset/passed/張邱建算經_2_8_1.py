"""
今有方錐下方二丈髙三丈欲斬末為方亭令上方六尺問斬髙㡬何
術曰令上方尺數乗髙尺數為實以下方尺數為法實如法而一
答曰 a尺
"""

"""
Suppose there is a square pyramid with a base side length of 2 zhang and a height of 3 zhang.
It is desired to cut off the top to form a smaller square pyramid, leaving the top square with a side length of 6 chi.
Question: at what height should the cut be made?

The procedure says: Multiply the side length of the top square by the height of the pyramid, obtaining the dividend.
Take the side length of the base square as the divisor.
Divide the dividend by the divisor to obtain the height of the cut.

Answer: *a* chi.
"""

# 下方二丈 (convert to chi)
下方 = 2 * 10  # 1 丈 = 10 尺

# 高三丈 (convert to chi)
高 = 3 * 10  # 1 丈 = 10 尺

# 上方六尺
上方 = 6

# 令上方尺數乘高尺數，為實
實 = 上方 * 高

# 以下方尺數為法
法 = 下方

# 實如法而一
a = Fraction(實, 法)  # The height of the cut in chi
"""
"""
