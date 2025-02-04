"""
今有望松生山上不知高下立兩表齊高二丈前後相去五十步令後表與前表參相直從前表卻行七步四尺薄地遙望松末與表端參合又望松本入表二尺八寸复從後表卻行八步五尺薄地遙望松末亦與表端參合問松高及山去表各幾何
術曰以入表乘表間為實相多為法除之加入表即得松高求表去山遠近者置表間以前表卻行乘之為實相多為法除之得山去表
答曰松高 a丈 山去表 b里 
"""

#----- content starts here -----
"""
Suppose there is a pine tree growing on a mountain, and its height and distance are unknown.
Two poles are erected, each 2 zhang high, and the distance between the two poles is 50 bu.
The rear pole is aligned with the front pole and the top of the pine tree.
From the front pole, one walks backward 7 bu and 4 chi, and observes that the top of the pine tree aligns with the top of the pole, and the base of the pine tree aligns 2 chi 8 cun into the pole.
Then, from the rear pole, one walks backward 8 bu and 5 chi, and observes that the top of the pine tree aligns with the top of the pole.

Question: What are the height of the pine tree and the distance from the mountain to the pole?

The procedure says:
To calculate the height of the pine tree:
- Multiply the amount the tree base enters the pole by the distance between the poles to get the dividend.
- Multiply the backward distances (from the front and rear poles) together to get the divisor.
- Divide the dividend by the divisor, then add the height of the pole to get the height of the pine tree.

To calculate the distance from the mountain to the pole:
- Take the distance between the poles and multiply it by the backward distance from the front pole to get the dividend.
- Multiply the backward distances (from the front and rear poles) together to get the divisor.
- Divide the dividend by the divisor to get the distance from the mountain to the pole.

Answer: The pine tree is *a* zhang tall, and the mountain is *b* li away from the pole.
"""

# Constants
表高 = 2  # Each pole is 2 zhang high
表間 = 50  # Distance between the two poles in bu

# Measurements
前表卻行 = 7 + Fraction(4, 10)  # 7 bu and 4 chi (convert chi to fractional bu)
入表 = Fraction(2, 10) + Fraction(8, 100)  # 2 chi and 8 cun (convert chi and cun to fractional bu)
後表卻行 = 8 + Fraction(5, 10)  # 8 bu and 5 chi (convert chi to fractional bu)

# 松高 calculation
# 以入表乘表間為實
松高實 = 入表 * 表間

# 相多為法
松高法 = 前表卻行 * 後表卻行

# 除之加入表即得松高
松高 = Fraction(松高實, 松高法) + 表高

# 山去表 calculation
# 置表間以前表卻行乘之為實
山去表實 = 表間 * 前表卻行

# 相多為法
山去表法 = 松高法

# 除之得山去表
山去表 = Fraction(山去表實, 山去表法)

# Convert 山去表 from bu to li (1 li = 300 bu)
山去表 = Fraction(山去表, 300)

# Final answers
a = 松高  # 松高 in zhang
b = 山去表  # 山去表 in li#----- content ends here -----

"""
Variable 'a' has wrong value. Expected: 307/25, Actual: 1398/629
Variable 'b' has wrong value. Expected: 23/21, Actual: 1/51"""
