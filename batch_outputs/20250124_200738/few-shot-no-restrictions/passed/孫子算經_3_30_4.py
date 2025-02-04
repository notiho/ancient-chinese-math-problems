"""
今有九里渠，三寸魚頭，頭相次。問：魚得幾何？
術曰：置九里以三百步乘之，得二千七百步；又以六尺乘之，得一萬六千二百尺，上十之，得一十六萬二千寸，以魚三寸除之，即得。
答曰： a 。
"""

#----- content starts here -----
"""
Suppose there is a canal 9 li long, with fish heads spaced 3 cun apart, one after another.
Question: how many fish are there?

The procedure says: Take 9 li and multiply it by 300 bu, obtaining 2700 bu.
Then multiply it by 6 chi, obtaining 16200 chi.
Convert it to cun by multiplying by 10, obtaining 162000 cun.
Divide it by 3 cun (the spacing of the fish), and the result is the number of fish.

Answer: *a* fish.
"""

from fractions import Fraction

# 置九里
里 = 9

# 每里有三百步
步每里 = 300
總步 = 里 * 步每里  # 得二千七百步

# 每步有六尺
尺每步 = 6
總尺 = 總步 * 尺每步  # 得一萬六千二百尺

# 每尺有十寸
寸每尺 = 10
總寸 = 總尺 * 寸每尺  # 得一十六萬二千寸

# 魚頭間距三寸
魚頭間距 = 3

# 以魚三寸除之，即得
a = Fraction(總寸, 魚頭間距)

a  # Number of fish#----- content ends here -----

"""
"""
