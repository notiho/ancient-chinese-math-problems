"""
今有牛、馬、羊食人苗。苗主責之粟五斗。羊主曰：「我羊食半馬。」馬主曰：「我馬食半牛。」今欲衰償之，問︰各出幾何？
術曰：置牛四、馬二、羊一，各自為列衰，副并為法。以五斗乘未并者各自為實。實如法得一斗。
荅曰：牛主出 a斗 。馬主出 b斗 。羊主出 c升 。
"""

#----- content starts here -----
"""
Suppose there are oxen, horses, and sheep eating a person's crops. The crop owner demands 5 dou of millet as compensation.
The sheep owner says: "My sheep ate half as much as a horse."
The horse owner says: "My horse ate half as much as an ox."
Now, dividing the compensation proportionally, how much does each pay?

The procedure says: Assign values to the ox, horse, and sheep: 4, 2, and 1 respectively.
Each becomes its own term in the decreasing sequence.
Add these values to get the divisor.
Multiply the 5 dou by the uncombined values for each term to get the dividend.
Divide the dividend by the divisor to get the amount of millet each owes.

Answer: The ox owner pays *a* dou. The horse owner pays *b* dou. The sheep owner pays *c* sheng.
"""

from fractions import Fraction

# 牛、馬、羊的比例
牛 = 4
馬 = 2
羊 = 1

# 副并為法
法 = 牛 + 馬 + 羊

# 總賠償粟五斗
總賠償 = 5  # in dou

# 各自為實
牛實 = 總賠償 * 牛
馬實 = 總賠償 * 馬
羊實 = 總賠償 * 羊

# 實如法得一斗
牛賠償 = Fraction(牛實, 法)
馬賠償 = Fraction(馬實, 法)
羊賠償 = Fraction(羊實, 法)

# Convert 羊賠償 to 升 (1 dou = 10 sheng)
羊賠償升 = 羊賠償 * 10

# Final answers
a = 牛賠償
b = 馬賠償
c = 羊賠償升

a, b, c#----- content ends here -----

"""
"""
