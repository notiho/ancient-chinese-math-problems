"""
今有二人同所立。甲行率七，乙行率三。乙東行。甲南行十步而邪東北與乙會。問︰甲乙行各幾何？
術曰：令七自乘，三亦自乘，并而半之，以為甲邪行率。邪行率減於七自乘，餘為南行率。以三乘七為乙東行率。置南行十步，以甲邪行率乘之，副置十步，以乙東行率乘之，各自為實。實如南行率而一，各得行數。
荅曰：乙東行 a步 ；甲邪行 b步 及之。
"""

#----- content starts here -----
"""
Suppose two people stand at the same location. Person A has a walking rate of 7, and Person B has a walking rate of 3.
Person B walks east. Person A walks south for 10 bu and then diagonally northeast to meet Person B.
Question: how far do Person A and Person B each walk?

The procedure says: Square 7, and square 3, then add them together and halve the result to obtain Person A's diagonal walking rate.
Subtract the diagonal walking rate from the square of 7 to get the southward walking rate.
Multiply 3 by 7 to get Person B's eastward walking rate.
Place the southward walk of 10 bu, multiply it by Person A's diagonal walking rate, and separately multiply it by Person B's eastward walking rate.
Each result is divided by the southward walking rate to obtain the respective walking distances.

Answer: Person B walks *a* bu east; Person A walks *b* bu diagonally northeast.
"""

from fractions import Fraction

# 甲行率七
甲行率 = 7

# 乙行率三
乙行率 = 3

# 南行十步
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

# 各自為實，實如南行率而一，各得行數
b = Fraction(甲實, 南行率)  # 甲邪行
a = Fraction(乙實, 南行率)  # 乙東行#----- content ends here -----

"""
"""
