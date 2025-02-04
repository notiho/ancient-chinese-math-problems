"""
今有望松生山上，不知高下。立兩表齊，高二丈，前後相去五十步，令後表與前表參相直。從前表卻行七步四尺，薄地遙望松末，與表端參合。又望松本，入表二尺八寸。复從後表卻行八步五尺，薄地遙望松末，亦與表端參合。問松高及山去表各幾何？
術曰：以入表乘表間為實。相多為法，除之。加入表，即得松高。求表去山遠近者：置表間，以前表卻行乘之為實。相多為法，除之，得山去表。
答曰：松高 a丈 ；山去表 b里 。
"""

#----- content starts here -----
"""
Suppose there is a pine tree growing on a mountain, and its height is unknown.
Two poles are erected, both of equal height, 2 zhang. The distance between the two poles is 50 bu.
The rear pole is aligned with the front pole and the top of the pine tree.
From the front pole, one walks backward 7 bu and 4 chi, and from the ground, the top of the pine tree aligns with the top of the pole.
Looking at the base of the pine tree, the alignment enters the pole by 2 chi and 8 cun.
From the rear pole, one walks backward 8 bu and 5 chi, and from the ground, the top of the pine tree again aligns with the top of the pole.

Question: What are the height of the pine tree and the distance from the mountain to the pole?

The procedure says: To find the height of the pine tree:
Multiply the amount the alignment enters the pole by the distance between the poles, obtaining the dividend.
The difference in backward walking distances is the divisor.
Divide the dividend by the divisor, and add the height of the pole. This gives the height of the pine tree.

To find the distance from the mountain to the pole:
Take the distance between the poles, and multiply it by the backward walking distance from the front pole, obtaining the dividend.
The difference in backward walking distances is the divisor.
Divide the dividend by the divisor. This gives the distance from the mountain to the pole.

Answer: The height of the pine tree is *a* zhang; the distance from the mountain to the pole is *b* li.
"""

# Known values
表高 = 2  # 表高 2 丈
表間 = 50  # 表間 50 步

# 前表卻行 7 步 4 尺
前表卻行 = 7 + Fraction(4, 10)  # Convert 4 尺 to 步 (1 步 = 10 尺)

# 入表 2 尺 8 寸
入表 = 2 + Fraction(8, 10)  # Convert 8 寸 to 尺 (1 尺 = 10 寸)

# 後表卻行 8 步 5 尺
後表卻行 = 8 + Fraction(5, 10)  # Convert 5 尺 to 步

# 松高 calculation
# 以入表乘表間為實
松高實 = 入表 * 表間

# 相多為法
松高法 = 後表卻行 - 前表卻行

# 除之，加入表，即得松高
松高 = Fraction(松高實, 松高法) + 表高

# 山去表 calculation
# 置表間，以前表卻行乘之為實
山去表實 = 表間 * 前表卻行

# 相多為法
山去表法 = 後表卻行 - 前表卻行

# 除之，得山去表
山去表 = Fraction(山去表實, 山去表法)

# Convert 山去表 from 步 to 里 (1 里 = 300 步)
山去表 = Fraction(山去表, 300)

# Final answers
a = 松高  # 松高 in 丈
b = 山去表  # 山去表 in 里#----- content ends here -----

"""
Variable 'a' has wrong value. Expected: 307/25, Actual: 1422/11
Variable 'b' has wrong value. Expected: 23/21, Actual: 37/33"""
