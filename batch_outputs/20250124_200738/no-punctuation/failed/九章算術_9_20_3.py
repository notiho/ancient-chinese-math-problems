"""
今有邑方十里各中開門甲乙俱從邑中央而出乙東出甲南出出門不知步數邪向東北磨邑適與乙會率甲行五乙行三問甲乙行各幾何
術曰令五自乘三亦自乘并而半之為邪行率邪行率減於五自乘者餘為南行率以三乘五為乙東行率置邑方半之以南行率乘之如東行率而一即得出南門步數以增邑方半即南行置南行步求弦者以邪行率乘之求東者以東行率乘之各自為實實如南行率得一步
荅曰甲出南門 a步 邪東北行 b步 及乙乙東行 c步 
"""

#----- content starts here -----
"""
Suppose there is a square city with sides of 10 li. Each side has a gate in the middle.
Person A exits from the south gate, and Person B exits from the east gate. Both start from the center of the city.
Person B walks east, and Person A walks south. They then turn and walk diagonally northeast, meeting at a point outside the city.
The walking rates are such that Person A walks 5 steps for every 3 steps Person B walks.
Question: how many steps does each person walk?

The procedure says:
1. Square 5 (Person A's rate) and square 3 (Person B's rate), add them, and halve the result to get the diagonal rate.
2. Subtract the square of 5 (Person A's rate) from the diagonal rate to get the southward rate.
3. Multiply 3 (Person B's rate) by 5 (Person A's rate) to get the eastward rate.
4. Take half the side of the city and multiply it by the southward rate. Divide by the eastward rate to get the southward steps to exit the gate.
5. Add this to half the side of the city to get the total southward steps.
6. To find the diagonal steps, multiply the diagonal rate by the southward steps.
7. To find the eastward steps, multiply the eastward rate by the southward steps.
8. Divide each result by the southward rate to get the respective steps.

Answer: Person A exits the south gate after *a* steps, walks diagonally northeast for *b* steps, and Person B walks east for *c* steps.
"""

from fractions import Fraction

# Rates of walking
甲率 = 5  # Person A's rate (southward)
乙率 = 3  # Person B's rate (eastward)

# Square the rates and calculate the diagonal rate
甲率平方 = 甲率 ** 2
乙率平方 = 乙率 ** 2
邪行率 = Fraction(甲率平方 +乙率平方, 2)

# Calculate the southward rate
南行率 = 邪行率 - 甲率平方

# Calculate the eastward rate
東行率 = 乙率 * 甲率

# Half the side of the city
邑方半 = Fraction(10, 2)

# Calculate the southward steps to exit the gate
南門步數 = Fraction(邑方半 * 南行率, 東行率)

# Total southward steps
甲南步 = 南門步數 + 邑方半

# Calculate the diagonal steps
邪東北步 = Fraction(邪行率 * 甲南步, 南行率)

# Calculate the eastward steps
乙東步 = Fraction(東行率 * 甲南步, 南行率)

# Assign results
a = 甲南步
b = 邪東北步
c = 乙東步#----- content ends here -----

"""
Variable 'a' has wrong value. Expected: 800, Actual: 7/3
Variable 'b' has wrong value. Expected: 9775/2, Actual: -119/24
Variable 'c' has wrong value. Expected: 8625/2, Actual: -35/8"""
