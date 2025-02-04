"""
今有方亭下方三丈上方一丈髙二丈五尺欲接築為方錐問接築髙㡬何
術曰置上方尺數以髙乗之為實以上方尺數減下方尺數餘為法實如法而一
答曰 a丈
"""

"""
Suppose there is a square pavilion with a bottom side length of 3 zhang, a top side length of 1 zhang, and a height of 2 zhang and 5 chi.
It is desired to extend and construct it into a square pyramid.
Question: what is the height of the extension?

The procedure says: Place the number of chi of the top side.
Multiply it by the height, obtaining the dividend.
Subtract the number of chi of the bottom side from the number of chi of the top side.
The remainder is the divisor.
Divide the dividend by the divisor, obtaining the height of the extension.

Answer: *a* zhang.
"""

# 下方三丈 (convert to chi: 1 丈 = 10 尺)
下方 = 3 * 10

# 上方一丈 (convert to chi)
上方 = 1 * 10

# 高二丈五尺 (convert to chi)
高 = 2 * 10 + 5

# 置上方尺數，以高乘之，為實
實 = 上方 * 高

# 以上方尺數減下方尺數，餘為法
法 = 下方 - 上方

# 實如法而一
a = Fraction(實, 法) / 10  # Convert back to zhang for the final answer
"""
"""
