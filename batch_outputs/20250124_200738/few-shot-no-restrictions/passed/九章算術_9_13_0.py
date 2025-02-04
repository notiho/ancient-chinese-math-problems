"""
今有二人同所立。甲行率七，乙行率三。乙東行。甲南行十步而邪東北與乙會。問︰甲乙行各幾何？
術曰：令七自乘，三亦自乘，并而半之，以為甲邪行率。邪行率減於七自乘，餘為南行率。以三乘七為乙東行率。置南行十步，以甲邪行率乘之，副置十步，以乙東行率乘之，各自為實。實如南行率而一，各得行數。
荅曰：乙東行 a步 ；甲邪行 b步 及之。
"""

#----- content starts here -----
"""
Suppose two people stand at the same location. Person A walks at a rate of 7, and Person B walks at a rate of 3. 
Person B walks east, while Person A walks south for 10 bu and then diagonally northeast to meet Person B.
Question: how far does each person walk?

The procedure says:
- Square 7 (Person A's rate) and square 3 (Person B's rate), add them together, and halve the result to obtain Person A's diagonal walking rate.
- Subtract the diagonal walking rate from the square of 7 to get the south walking rate.
- Multiply 3 by 7 to get Person B's east walking rate.
- Place the 10 bu of south walking, multiply it by Person A's diagonal walking rate, and place it as one dividend.
- Multiply the 10 bu by Person B's east walking rate and place it as another dividend.
- Divide each dividend by the south walking rate to get the walking distances.

Answer: Person B walks *a* bu east; Person A walks *b* bu diagonally northeast.
"""

from fractions import Fraction

# Rates of walking
甲行率 = 7  # Person A's walking rate
乙行率 = 3  # Person B's walking rate

# 南行 10 步
南行 = 10

# Step 1: Calculate 甲邪行率 (Person A's diagonal walking rate)
甲行率平方 = 甲行率 ** 2
乙行率平方 = 乙行率 ** 2
甲邪行率 = Fraction(甲行率平方 +乙行率平方, 2)

# Step 2: Calculate 南行率 (south walking rate)
南行率 = 甲行率平方 - 甲邪行率

# Step 3: Calculate 乙東行率 (Person B's east walking rate)
乙東行率 = 乙行率 * 甲行率

# Step 4: Calculate 实 (dividends)
甲邪行實 = 南行 * 甲邪行率
乙東行實 = 南行 * 乙東行率

# Step 5: Calculate 行數 (walking distances)
甲邪行 = Fraction(甲邪行實, 南行率)
乙東行 = Fraction(乙東行實, 南行率)

# Final results
a = 乙東行  # Person B's east walking distance
b = 甲邪行  # Person A's diagonal walking distance

a, b#----- content ends here -----

"""
"""
