"""
今有牛、馬、羊食人苗。苗主責之粟五斗。羊主曰：「我羊食半馬。」馬主曰：「我馬食半牛。」今欲衰償之，問︰各出幾何？
術曰：置牛四、馬二、羊一，各自為列衰，副并為法。以五斗乘未并者各自為實。實如法得一斗。
荅曰：牛主出 a斗 。馬主出 b斗 。羊主出 c升 。
"""

#----- content starts here -----
"""
Suppose there are oxen, horses, and sheep eating a farmer's crops. The farmer demands compensation of 5 dou of millet.
The sheep owner says: "My sheep eat half as much as a horse."
The horse owner says: "My horse eats half as much as an ox."
Now, it is desired to proportionally compensate. Question: how much does each owner contribute?

The procedure says: Assign weights to the ox, horse, and sheep as 4, 2, and 1, respectively, each forming a decreasing sequence.
Add these weights to obtain the divisor.
Multiply the 5 dou by the weights of the respective animals to obtain the dividend for each.
Divide the dividend by the divisor to obtain the contribution of each in dou.

The answer says: the ox owner contributes *a* dou, the horse owner contributes *b* dou, and the sheep owner contributes *c* sheng.
"""

from fractions import Fraction

# 牛、馬、羊的權重
牛 = 4
馬 = 2
羊 = 1

# 副并為法
法 = 牛 + 馬 + 羊

# 總補償粟五斗
總補償 = 5  # in dou

# 各自為實
牛實 = 牛 * 總補償
馬實 = 馬 * 總補償
羊實 = 羊 * 總補償

# 實如法得一斗
牛補償 = Fraction(牛實, 法)
馬補償 = Fraction(馬實, 法)
羊補償 = Fraction(羊實, 法)

# 轉換羊補償為升 (1 dou = 10 sheng)
羊補償升 = 羊補償 * 10

a = 牛補償
b = 馬補償
c = 羊補償升

# Output the results
a, b, c#----- content ends here -----

"""
"""
