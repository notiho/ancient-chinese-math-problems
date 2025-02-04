"""
今有二人同所立。甲行率七，乙行率三。乙東行。甲南行十步而邪東北與乙會。問︰甲乙行各幾何？
術曰：令七自乘，三亦自乘，并而半之，以為甲邪行率。邪行率減於七自乘，餘為南行率。以三乘七為乙東行率。置南行十步，以甲邪行率乘之，副置十步，以乙東行率乘之，各自為實。實如南行率而一，各得行數。
荅曰：乙東行 a步 ；甲邪行 b步 及之。
"""

#----- content starts here -----
"""
Suppose two people stand at the same location. Person A walks at a rate of 7, and Person B walks at a rate of 3.
Person B walks east. Person A walks south for 10 bu and then diagonally northeast to meet Person B.
Question: how far does each person walk?

The procedure says:
- Square 7, and square 3. Add them together, then halve the result. This gives the diagonal walking rate for Person A.
- Subtract the diagonal walking rate from the square of 7. The remainder is the southward walking rate for Person A.
- Multiply 3 by 7 to get the eastward walking rate for Person B.
- Place the southward distance of 10 bu. Multiply it by Person A's diagonal walking rate. Separately, multiply 10 bu by Person B's eastward walking rate. These are the respective dividends.
- Divide each dividend by the southward walking rate to get the distances walked by each person.

Answer: Person B walks *a* bu east; Person A walks *b* bu diagonally northeast to meet them.
"""

from fractions import Fraction

# 行速率
甲行率 = 7
乙行率 = 3

# 甲南行 10 步
南行距離 = 10

# 計算甲的邪行率
甲行率平方 = 甲行率**2
乙行率平方 = 乙行率**2
甲邪行率 = Fraction(甲行率平方 +乙行率平方, 2)

# 計算甲的南行率
甲南行率 = 甲行率平方 - 甲邪行率

# 計算乙的東行率
乙東行率 = 甲行率 * 乙行率

# 計算甲和乙的實
甲實 = 南行距離 * 甲邪行率
乙實 = 南行距離 * 乙東行率

# 計算甲和乙的行距離
甲邪行距離 = Fraction(甲實, 甲南行率)
乙東行距離 = Fraction(乙實, 甲南行率)

# 答案
a = 乙東行距離
b = 甲邪行距離#----- content ends here -----

"""
"""
