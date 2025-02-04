"""
今有牛、馬、羊食人苗。苗主責之粟五斗。羊主曰：「我羊食半馬。」馬主曰：「我馬食半牛。」今欲衰償之，問︰各出幾何？
術曰：置牛四、馬二、羊一，各自為列衰，副并為法。以五斗乘未并者各自為實。實如法得一斗。
荅曰：牛主出 a斗 。馬主出 b斗 。羊主出 c升 。
"""

"""
Suppose there are a cow, a horse, and a sheep eating someone's crops. The owner of the crops demands 5 dou of millet as compensation.
The sheep's owner says: "My sheep eats half as much as a horse."
The horse's owner says: "My horse eats half as much as a cow."
Now, dividing the compensation proportionally, how much does each owe?

The procedure says: Assign 4 to the cow, 2 to the horse, and 1 to the sheep. Each becomes its own term in the decreasing sequence.
Add these together to form the divisor.
Multiply the 5 dou by each of the uncombined terms to form the dividends.
Divide each dividend by the divisor to obtain the amount of millet owed.

The answer says: the cow's owner owes *a* dou, the horse's owner owes *b* dou, and the sheep's owner owes *c* sheng.
"""

# 置牛四、馬二、羊一
牛 = 4
馬 = 2
羊 = 1

# 副并為法
法 = 牛 + 馬 + 羊

# 以五斗乘未并者各自為實
總斗 = 5
牛實 = 總斗 * 牛
馬實 = 總斗 * 馬
羊實 = 總斗 * 羊

# 實如法得一斗
a = Fraction(牛實, 法)  # 牛主出 a 斗
b = Fraction(馬實, 法)  # 馬主出 b 斗
c = Fraction(羊實, 法) * 10  # 羊主出 c 升 (1 斗 = 10 升)
"""
"""
