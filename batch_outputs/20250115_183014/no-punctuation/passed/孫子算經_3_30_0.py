"""
今有九里渠三寸魚頭頭相次問魚得幾何
術曰置九里以三百步乘之得二千七百步又以六尺乘之得一萬六千二百尺上十之得一十六萬二千寸以魚三寸除之即得
答曰 a 
"""

"""
Suppose there is a canal 9 li long, with fish heads spaced 3 cun apart, one after another.
Question: how many fish are there?

The procedure says: Place the 9 li, multiply it by 300 bu, obtaining 2700 bu.
Then multiply it by 6 chi, obtaining 16200 chi.
Convert it to cun by multiplying by 10, obtaining 162000 cun.
Divide it by 3 cun (the spacing of the fish), and the result is the number of fish.

Answer: *a* fish.
"""

# 置九里
里 = 9

# 以三百步乘之，得二千七百步
步 = 300 * 里

# 又以六尺乘之，得一萬六千二百尺
尺 = 6 * 步

# 上十之，得一十六萬二千寸
寸 = 10 * 尺

# 以魚三寸除之，即得
魚間距 = 3
a = 寸 // 魚間距
"""
"""
