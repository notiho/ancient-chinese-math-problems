"""
今有望松生山上，不知高下。立兩表齊，高二丈，前後相去五十步，令後表與前表參相直。從前表卻行七步四尺，薄地遙望松末，與表端參合。又望松本，入表二尺八寸。复從後表卻行八步五尺，薄地遙望松末，亦與表端參合。問松高及山去表各幾何？
術曰：以入表乘表間為實。相多為法，除之。加入表，即得松高。求表去山遠近者：置表間，以前表卻行乘之為實。相多為法，除之，得山去表。
答曰：松高 a丈 ；山去表 b里 。
"""

#----- content starts here -----
"""
Suppose there is a pine tree growing on a mountain, and its height is unknown.
Two poles are erected, both of equal height, each 2 zhang tall. The distance between the two poles is 50 bu.
The rear pole, the front pole, and the top of the pine tree are aligned in a straight line.
From the front pole, one steps back 7 bu and 4 chi, and from the ground, the top of the pine tree aligns with the top of the front pole.
Then, the base of the pine tree aligns 2 chi and 8 cun into the front pole.
From the rear pole, one steps back 8 bu and 5 chi, and from the ground, the top of the pine tree aligns with the top of the rear pole.
Question: What are the height of the pine tree and the distance from the mountain to the poles?

The procedure says:
To find the height of the pine tree: Multiply the amount the pole is entered by the distance between the poles to obtain the dividend.
The difference between the distances stepped back is the divisor. Divide the dividend by the divisor, and add the height of the pole to obtain the height of the pine tree.
To find the distance from the mountain to the poles: Take the distance between the poles and multiply it by the distance stepped back from the front pole to obtain the dividend.
The difference between the distances stepped back is the divisor. Divide the dividend by the divisor to obtain the distance from the mountain to the poles.

Answer: The pine tree is *a* zhang tall; the distance from the mountain to the poles is *b* li.
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

# 松高計算
# 以入表乘表間為實
松高實 = 入表 * 表間

# 相多為法
松高法 = 後表卻行 - 前表卻行

# 除之，加入表，即得松高
松高 = Fraction(松高實, 松高法) + 表高
a = 松高

# 山去表計算
# 置表間，以前表卻行乘之為實
山去表實 = 表間 * 前表卻行

# 相多為法
山去表法 = 松高法

# 除之，得山去表
山去表 = Fraction(山去表實, 山去表法)
b = 山去表#----- content ends here -----

"""
Variable 'a' has wrong value. Expected: 307/25, Actual: 1422/11
Variable 'b' has wrong value. Expected: 23/21, Actual: 3700/11"""
