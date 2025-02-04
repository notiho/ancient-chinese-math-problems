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
- Square 7 (Person A's rate) and square 3 (Person B's rate), add them together, and halve the sum. This gives the diagonal walking rate for Person A.
- Subtract the diagonal walking rate from the square of 7 to get the southward walking rate for Person A.
- Multiply 3 (Person B's rate) by 7 to get Person B's eastward walking rate.
- Place the southward distance of 10 bu, multiply it by Person A's diagonal walking rate. 
- Separately, place the same 10 bu and multiply it by Person B's eastward walking rate. 
- Divide each result by the southward walking rate to obtain the distances walked by each person.

Answer: Person B walks *a* bu east; Person A walks *b* bu diagonally northeast.
"""

from fractions import Fraction

# Given rates
甲行率 = 7  # Person A's walking rate
乙行率 = 3  # Person B's walking rate

# Southward distance walked by Person A
南行距離 = 10  # bu

# Step 1: Calculate Person A's diagonal walking rate
甲邪行率 = Fraction(甲行率**2 + 乙行率**2, 2)

# Step 2: Calculate Person A's southward walking rate
南行率 = 甲行率**2 - 甲邪行率

# Step 3: Calculate Person B's eastward walking rate
乙東行率 = 甲行率 * 乙行率

# Step 4: Calculate the distances walked
甲邪行距離 = Fraction(南行距離 * 甲邪行率, 南行率)
乙東行距離 = Fraction(南行距離 * 乙東行率, 南行率)

# Final answers
a = 乙東行距離  # Distance walked by Person B (eastward)
b = 甲邪行距離  # Distance walked by Person A (diagonally northeast)

a, b  # Output the results#----- content ends here -----

"""
"""
