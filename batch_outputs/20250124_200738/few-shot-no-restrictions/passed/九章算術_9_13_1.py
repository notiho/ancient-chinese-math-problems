"""
今有二人同所立。甲行率七，乙行率三。乙東行。甲南行十步而邪東北與乙會。問︰甲乙行各幾何？
術曰：令七自乘，三亦自乘，并而半之，以為甲邪行率。邪行率減於七自乘，餘為南行率。以三乘七為乙東行率。置南行十步，以甲邪行率乘之，副置十步，以乙東行率乘之，各自為實。實如南行率而一，各得行數。
荅曰：乙東行 a步 ；甲邪行 b步 及之。
"""

#----- content starts here -----
"""
Suppose there are two people standing at the same location. 
Person A walks at a rate of 7 bu per unit time, and Person B walks at a rate of 3 bu per unit time. 
Person B walks east, while Person A walks south for 10 bu, then diagonally northeast to meet Person B. 
Question: how far does each person walk?

The procedure says:
- Square 7 (A's rate) and square 3 (B's rate), add them together, and halve the result to obtain A's diagonal walking rate.
- Subtract A's diagonal walking rate from the square of 7 to get A's southward walking rate.
- Multiply 3 (B's rate) by 7 (A's rate) to get B's eastward walking rate.
- Place 10 bu (A's southward distance), multiply it by A's diagonal walking rate. 
- Separately, place 10 bu, multiply it by B's eastward walking rate. 
- Each result is divided by A's southward walking rate to get the respective distances.

Answer: B walks *a* bu east, and A walks *b* bu diagonally northeast.
"""

from fractions import Fraction

# Rates of A and B
甲行率 = 7  # A's walking rate
乙行率 = 3  # B's walking rate

# Step 1: Calculate A's diagonal walking rate
甲邪行率 = Fraction((甲行率**2 + 乙行率**2), 2)

# Step 2: Calculate A's southward walking rate
甲南行率 = 甲行率**2 - 甲邪行率

# Step 3: Calculate B's eastward walking rate
乙東行率 = 乙行率 * 甲行率

# Step 4: Place A's southward distance (10 bu)
南行距離 = 10

# Step 5: Calculate A's diagonal distance
甲邪行距離 = Fraction(南行距離 * 甲邪行率, 甲南行率)

# Step 6: Calculate B's eastward distance
乙東行距離 = Fraction(南行距離 * 乙東行率, 甲南行率)

# Final results
a = 乙東行距離  # B's eastward distance
b = 甲邪行距離  # A's diagonal distance

# Output the results
a, b#----- content ends here -----

"""
"""
