"""
今有牛、馬、羊食人苗。苗主責之粟五斗。羊主曰：「我羊食半馬。」馬主曰：「我馬食半牛。」今欲衰償之，問︰各出幾何？
術曰：置牛四、馬二、羊一，各自為列衰，副并為法。以五斗乘未并者各自為實。實如法得一斗。
荅曰：牛主出 a(=20/7)斗 。馬主出 b(=10/7)斗 。羊主出 c(=50/7)升 。
"""

"""
Suppose there are a cow, a horse, and a sheep that ate someone's crops. The crop owner demands 5 dou of millet as compensation.
The sheep owner says: "My sheep ate half as much as the horse."
The horse owner says: "My horse ate half as much as the cow."
Now, dividing the compensation proportionally, how much should each pay?

The procedure says: Assign 4 to the cow, 2 to the horse, and 1 to the sheep. Each becomes its own decreasing sequence.
In auxiliary, add them together to form the divisor.
Multiply the 5 dou by the uncombined values, each becoming its own dividend.
Divide the dividends by the divisor to obtain the millet owed.

The answer says: the cow owner pays *a*(=20/7) dou, the horse owner pays *b*(=10/7) dou, and the sheep owner pays *c*(=50/7) sheng.
"""

# 置牛四、馬二、羊一
牛 = 4
馬 = 2
羊 = 1

# 副并為法
法 = 牛 + 馬 + 羊

# 以五斗乘未并者
總補償 = 5  # 5斗
牛實 = 總補償 * 牛
馬實 = 總補償 * 馬
羊實 = 總補償 * 羊

# 各自為實，實如法得一斗
a = Fraction(牛實, 法)  # 20/7 斗
b = Fraction(馬實, 法)  # 10/7 斗
c = Fraction(羊實, 法) * 10  # 50/7 升 (1斗 = 10升)
"""
"""
