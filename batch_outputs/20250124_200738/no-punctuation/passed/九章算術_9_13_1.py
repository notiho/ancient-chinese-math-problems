"""
今有二人同所立甲行率七乙行率三乙東行甲南行十步而邪東北與乙會問甲乙行各幾何
術曰令七自乘三亦自乘并而半之以為甲邪行率邪行率減於七自乘餘為南行率以三乘七為乙東行率置南行十步以甲邪行率乘之副置十步以乙東行率乘之各自為實實如南行率而一各得行數
荅曰乙東行 a步 甲邪行 b步 及之
"""

#----- content starts here -----
"""
Suppose two people stand at the same location. Person A (Jia) walks at a rate of 7, and person B (Yi) walks at a rate of 3.
Person B walks east, and person A walks south for 10 bu, then diagonally northeast to meet person B.
Question: how far does each person walk?

The procedure says:
- Square 7 and square 3, add them together, and halve the result to obtain Jia's diagonal walking rate.
- Subtract Jia's diagonal walking rate from the square of 7 to obtain Jia's southward walking rate.
- Multiply 3 by 7 to obtain Yi's eastward walking rate.
- Place the southward distance of 10 bu, and multiply it by Jia's diagonal walking rate to obtain one dividend.
- Place the same 10 bu, and multiply it by Yi's eastward walking rate to obtain another dividend.
- Divide each dividend by the respective rate to obtain the walking distances.

Answer: Yi walks *a* bu east, Jia walks *b* bu diagonally northeast, and they meet.
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

# 以三乘七，為乙東行率
乙東行率 = 乙行率 * 甲行率

# 置南行十步，以甲邪行率乘之，副置十步，以乙東行率乘之，各自為實
甲實 = 南行 * 甲邪行率
乙實 = 南行 *乙東行率

# 實如南行率而一，各得行數
b = Fraction(甲實, 南行率)  # 甲邪行 (diagonal distance)
a = Fraction(乙實, 南行率)  # 乙東行 (eastward distance)#----- content ends here -----

"""
"""
