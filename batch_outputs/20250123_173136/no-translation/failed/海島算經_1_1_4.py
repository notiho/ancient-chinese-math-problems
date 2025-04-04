"""
今有望松生山上，不知高下。立兩表齊，高二丈，前後相去五十步，令後表與前表參相直。從前表卻行七步四尺，薄地遙望松末，與表端參合。又望松本，入表二尺八寸。复從後表卻行八步五尺，薄地遙望松末，亦與表端參合。問松高及山去表各幾何？
術曰：以入表乘表間為實。相多為法，除之。加入表，即得松高。求表去山遠近者：置表間，以前表卻行乘之為實。相多為法，除之，得山去表。
答曰：松高 a丈 ；山去表 b里 。
"""

"""

"""


from fractions import Fraction

# Given data
表高 = 2  # 表高二丈
表間 = 50  # 前後表相去五十步

# 前表觀測數據
前表卻行 = 7 + Fraction(4, 10)  # 卻行七步四尺
前表入表 = Fraction(2, 10) + Fraction(8, 100)  # 入表二尺八寸

# 後表觀測數據
後表卻行 = 8 + Fraction(5, 10)  # 卻行八步五尺

# 術曰：以入表乘表間為實，相多為法，除之，加入表，即得松高。
實_松高 = 表間 * 前表入表
法_松高 = 後表卻行 - 前表卻行
松高 = Fraction(實_松高, 法_松高) + 表高

# 術曰：置表間，以前表卻行乘之為實，相多為法，除之，得山去表。
實_山去表 = 表間 * 前表卻行
法_山去表 = 後表卻行 - 前表卻行
山去表 = Fraction(實_山去表, 法_山去表)

# Convert 松高 to 丈 and 山去表 to 里 (assuming 1 步 = 6 尺, 1 里 = 300 步)
松高_丈 = 松高  # 松高 is already in 丈
山去表_里 = Fraction(山去表, 300)

# Results
a = 松高_丈
b = 山去表_里


"""

"""


"""
Variable 'a' has wrong value. Expected: 307/25, Actual: 162/11
Variable 'b' has wrong value. Expected: 23/21, Actual: 37/33"""
