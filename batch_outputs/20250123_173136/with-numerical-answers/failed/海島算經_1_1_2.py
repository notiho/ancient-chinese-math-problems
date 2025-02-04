"""
今有望松生山上，不知高下。立兩表齊，高二丈，前後相去五十步，令後表與前表參相直。從前表卻行七步四尺，薄地遙望松末，與表端參合。又望松本，入表二尺八寸。复從後表卻行八步五尺，薄地遙望松末，亦與表端參合。問松高及山去表各幾何？
術曰：以入表乘表間為實。相多為法，除之。加入表，即得松高。求表去山遠近者：置表間，以前表卻行乘之為實。相多為法，除之，得山去表。
答曰：松高 a(=307/25)丈 ；山去表 b(=23/21)里 。
"""

"""
Suppose there is a pine tree growing on a mountain, and its height is unknown.
Two poles of equal height, 2 zhang, are erected. The distance between the two poles is 50 bu.
The rear pole is aligned with the front pole and the top of the pine tree.
From the front pole, one steps back 7 bu and 4 chi, and looks at the top of the pine tree, aligning it with the top of the pole.
Then, looking at the base of the pine tree, the line of sight enters the pole by 2 chi and 8 cun.
From the rear pole, one steps back 8 bu and 5 chi, and looks at the top of the pine tree, aligning it with the top of the pole.

Question: What are the height of the pine tree and the distance from the mountain to the pole?

The procedure says:
To find the height of the pine tree: Multiply the amount the line of sight enters the pole by the distance between the poles to get the dividend. Use the difference in distances stepped back as the divisor. Divide, and add the height of the pole to get the height of the pine tree.
To find the distance from the mountain to the pole: Take the distance between the poles, multiply it by the distance stepped back from the front pole to get the dividend. Use the difference in distances stepped back as the divisor. Divide to get the distance from the mountain to the pole.

Answer: The height of the pine tree is *a*(=307/25) zhang, and the distance from the mountain to the pole is *b*(=23/21) li.
"""

# Constants
表高 = 2  # 表高 2 丈
表間 = 50  # 表間 50 步

# 前表卻行 7 步 4 尺
前表卻行 = 7 + Fraction(4, 10)

# 入表 2 尺 8 寸
入表 = 2 + Fraction(8, 10)

# 後表卻行 8 步 5 尺
後表卻行 = 8 + Fraction(5, 10)

# 相多為法
相多 = 後表卻行 - 前表卻行

# 松高計算
# 以入表乘表間為實
松高實 = 入表 * 表間

# 除之，加入表，即得松高
松高 = Fraction(松高實, 相多) + 表高
a = 松高  # 307/25 丈

# 山去表計算
# 置表間，以前表卻行乘之為實
山去表實 = 表間 * 前表卻行

# 相多為法，除之，得山去表
山去表 = Fraction(山去表實, 相多)
b = 山去表  # 23/21 里
"""
Variable 'a' has wrong value. Expected: 307/25, Actual: 1422/11
Variable 'b' has wrong value. Expected: 23/21, Actual: 3700/11"""
