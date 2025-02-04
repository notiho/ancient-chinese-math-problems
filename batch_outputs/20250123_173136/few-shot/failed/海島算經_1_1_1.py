"""
今有望松生山上，不知高下。立兩表齊，高二丈，前後相去五十步，令後表與前表參相直。從前表卻行七步四尺，薄地遙望松末，與表端參合。又望松本，入表二尺八寸。复從後表卻行八步五尺，薄地遙望松末，亦與表端參合。問松高及山去表各幾何？
術曰：以入表乘表間為實。相多為法，除之。加入表，即得松高。求表去山遠近者：置表間，以前表卻行乘之為實。相多為法，除之，得山去表。
答曰：松高 a丈 ；山去表 b里 。
"""

"""
Suppose there is a pine tree growing on a mountain, and its height is unknown.
Two poles are erected, each 2 zhang tall, and the distance between the two poles is 50 bu.
The rear pole is aligned with the front pole and the pine tree in a straight line.
From the front pole, one walks backward 7 bu and 4 chi, and from the ground, the top of the pine tree aligns with the top of the pole.
Looking at the base of the pine tree, the line of sight enters the pole by 2 chi and 8 cun.
Then, from the rear pole, one walks backward 8 bu and 5 chi, and from the ground, the top of the pine tree again aligns with the top of the pole.
Question: What is the height of the pine tree and the distance from the mountain to the poles?

The procedure says:
1. To find the height of the pine tree:
   Multiply the amount the line of sight enters the pole by the distance between the poles to get the dividend.
   Use the difference in backward walking distances as the divisor.
   Divide, and add the height of the pole to get the height of the pine tree.
2. To find the distance from the mountain to the poles:
   Take the distance between the poles, multiply it by the backward walking distance from the front pole to get the dividend.
   Use the difference in backward walking distances as the divisor.
   Divide to get the distance from the mountain to the poles.

Answer: The height of the pine tree is *a* zhang; the distance from the mountain to the poles is *b* li.
"""

# Constants
表高 = 2  # Each pole is 2 zhang tall
表間 = 50  # Distance between the two poles in bu

# 前表卻行 7步4尺
前表卻行 = 7 + Fraction(4, 10)  # Convert 4 chi to fractional bu (1 bu = 10 chi)

# 入表 2尺8寸
入表 = Fraction(2, 10) + Fraction(8, 100)  # Convert 2 chi 8 cun to fractional bu (1 bu = 10 chi, 1 chi = 10 cun)

# 後表卻行 8步5尺
後表卻行 = 8 + Fraction(5, 10)  # Convert 5 chi to fractional bu

# Difference in backward walking distances
相多 = 後表卻行 - 前表卻行

# 松高 calculation
# 以入表乘表間為實
松高實 = 入表 * 表間

# 相多為法，除之
松高 = 松高實 / 相多

# 加入表，即得松高
a = 松高 + 表高

# 山去表 calculation
# 置表間，以前表卻行乘之為實
山去表實 = 表間 * 前表卻行

# 相多為法，除之
b = 山去表實 / 相多
"""
Variable 'a' has wrong value. Expected: 307/25, Actual: 162/11
Variable 'b' has wrong value. Expected: 23/21, Actual: 3700/11"""
