"""
今有二人同所立。甲行率七，乙行率三。乙東行。甲南行十步而邪東北與乙會。問︰甲乙行各幾何？
術曰：令七自乘，三亦自乘，并而半之，以為甲邪行率。邪行率減於七自乘，餘為南行率。以三乘七為乙東行率。置南行十步，以甲邪行率乘之，副置十步，以乙東行率乘之，各自為實。實如南行率而一，各得行數。
荅曰：乙東行 a步 ；甲邪行 b步 及之。
"""

"""
Suppose two people start from the same point. Person A has a walking rate of 7, and Person B has a walking rate of 3. 
Person B walks east, while Person A walks south for 10 bu and then diagonally northeast to meet Person B.
Question: how far does each person walk?

The procedure says:
- Square 7 (Person A's rate) and square 3 (Person B's rate), add them together, and halve the result. This gives the diagonal walking rate for Person A.
- Subtract the diagonal walking rate from the square of 7 to get the southward walking rate for Person A.
- Multiply 3 by 7 to get the eastward walking rate for Person B.
- Place the southward distance of 10 bu. Multiply it by Person A's diagonal walking rate. Also place the same 10 bu and multiply it by Person B's eastward walking rate. Each becomes a dividend.
- Divide each dividend by the southward walking rate to get the respective distances walked.

Answer: Person B walks *a* bu east; Person A walks *b* bu diagonally northeast in total.
"""

from fractions import Fraction

# 甲行率七，乙行率三
甲行率 = 7
乙行率 = 3

# 甲南行十步
南行 = 10

# 令七自乘，三亦自乘，并而半之，以為甲邪行率
甲邪行率 = Fraction((甲行率**2 + 乙行率**2), 2)

# 邪行率減於七自乘，餘為南行率
南行率 = 甲行率**2 - 甲邪行率

# 以三乘七為乙東行率
乙東行率 = 乙行率 * 甲行率

# 置南行十步，以甲邪行率乘之
甲實 = 甲邪行率 * 南行

# 副置十步，以乙東行率乘之
乙實 = 乙東行率 * 南行

# 實如南行率而一，各得行數
a = Fraction(乙實, 南行率)  # 乙東行
b = Fraction(甲實, 南行率)  # 甲邪行
"""
"""
