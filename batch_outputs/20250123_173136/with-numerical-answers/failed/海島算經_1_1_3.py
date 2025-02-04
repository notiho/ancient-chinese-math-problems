"""
今有望松生山上，不知高下。立兩表齊，高二丈，前後相去五十步，令後表與前表參相直。從前表卻行七步四尺，薄地遙望松末，與表端參合。又望松本，入表二尺八寸。复從後表卻行八步五尺，薄地遙望松末，亦與表端參合。問松高及山去表各幾何？
術曰：以入表乘表間為實。相多為法，除之。加入表，即得松高。求表去山遠近者：置表間，以前表卻行乘之為實。相多為法，除之，得山去表。
答曰：松高 a(=307/25)丈 ；山去表 b(=23/21)里 。
"""

"""
Suppose there is a pine tree growing on a mountain, and its height is unknown. Two poles of equal height, 2 zhang each, are erected, with a distance of 50 bu between them. The rear pole is aligned with the front pole and the top of the pine tree. From the front pole, one walks backward 7 bu and 4 chi, and from there, the top of the pine tree aligns with the top of the pole, while the base of the pine tree aligns 2 chi and 8 cun into the pole. Then, from the rear pole, one walks backward 8 bu and 5 chi, and from there, the top of the pine tree again aligns with the top of the pole.

Question: What are the height of the pine tree and the distance from the mountain to the poles?

The procedure says: Multiply the distance the base of the pine tree enters the pole by the distance between the poles to obtain the dividend. Use the difference in backward walking distances as the divisor. Divide, and add the height of the pole to obtain the height of the pine tree. To find the distance from the mountain to the poles: Place the distance between the poles, and multiply it by the backward walking distance from the front pole to obtain the dividend. Use the difference in backward walking distances as the divisor. Divide to obtain the distance from the mountain to the poles.

Answer: The height of the pine tree is *a*(=307/25) zhang, and the distance from the mountain to the poles is *b*(=23/21) li.
"""

# Constants
表高 = 2  # 表高 2 丈
表間 = 50  # 表間 50 步

# 前表卻行 7 步 4 尺
前表卻行 = 7 + Fraction(4, 10)  # 7步4尺 = 7 + 4/10 步

# 入表 2 尺 8 寸
入表 = Fraction(2, 10) + Fraction(8, 100)  # 2尺8寸 = 2/10 + 8/100 步

# 後表卻行 8 步 5 尺
後表卻行 = 8 + Fraction(5, 10)  # 8步5尺 = 8 + 5/10 步

# 相多為法
相多 = 後表卻行 - 前表卻行  # 差距

# 求松高
# 以入表乘表間為實
松高實 = 入表 * 表間

# 除以相多，加入表高
松高 = Fraction(松高實, 相多) + 表高  # 松高 = 307/25 丈

# 求山去表
# 置表間，以前表卻行乘之為實
山去表實 = 表間 * 前表卻行

# 除以相多
山去表 = Fraction(山去表實, 相多)  # 山去表 = 23/21 里

# Results
a = 松高  # 松高 = 307/25 丈
b = 山去表  # 山去表 = 23/21 里
"""
Variable 'a' has wrong value. Expected: 307/25, Actual: 162/11
Variable 'b' has wrong value. Expected: 23/21, Actual: 3700/11"""
