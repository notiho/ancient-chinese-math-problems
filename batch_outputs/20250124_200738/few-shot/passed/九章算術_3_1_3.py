"""
今有牛、馬、羊食人苗。苗主責之粟五斗。羊主曰：「我羊食半馬。」馬主曰：「我馬食半牛。」今欲衰償之，問︰各出幾何？
術曰：置牛四、馬二、羊一，各自為列衰，副并為法。以五斗乘未并者各自為實。實如法得一斗。
荅曰：牛主出 a斗 。馬主出 b斗 。羊主出 c升 。
"""

#----- content starts here -----
"""
Suppose there are cattle, horses, and sheep eating a farmer's crops. The farmer demands compensation of 5 dou of millet.
The sheep owner says: "My sheep eat half as much as a horse."
The horse owner says: "My horse eats half as much as a cow."
Now, it is desired to proportionally compensate. Question: how much does each pay?

The procedure says: Assign weights to the cow as 4, the horse as 2, and the sheep as 1. Each is placed as its own decreasing sequence.
Add these weights together to form the divisor.
Multiply the 5 dou by the uncombined weights, each becoming its own dividend.
Divide the dividends by the divisor to obtain the compensation in dou.

The answer says: the cow owner pays *a* dou, the horse owner pays *b* dou, and the sheep owner pays *c* sheng.
"""

# 置牛四、馬二、羊一
牛 = 4
馬 = 2
羊 = 1

# 各自為列衰
權重 = [牛, 馬, 羊]

# 副并為法
法 = sum(權重)

# 以五斗乘未并者
總補償 = 5  # 5斗
牛補償 = 總補償 * 牛
馬補償 = 總補償 * 馬
羊補償 = 總補償 * 羊

# 各自為實，實如法得一斗
a = Fraction(牛補償, 法)  # 牛主出 a斗
b = Fraction(馬補償, 法)  # 馬主出 b斗
c = Fraction(羊補償, 法) * 10  # 羊主出 c升 (1斗 = 10升)#----- content ends here -----

"""
"""
