"""
今有邑方十里，各中開門。甲乙俱從邑中央而出。乙東出；甲南出，出門不知步數，邪向東北磨邑，適與乙會。率甲行五，乙行三。問︰甲、乙行各幾何？
術曰：令五自乘，三亦自乘，并而半之，為邪行率。邪行率減於五自乘者，餘，為南行率。以三乘五，為乙東行率。置邑方半之，以南行率乘之，如東行率而一，即得出南門步數。以增邑方半，即南行。置南行步求弦者，以邪行率乘之，求東者以東行率乘之，各自為實。實如南行率得一步。
荅曰：甲出南門 a步 ，邪東北行 b步 ，及乙。乙東行 c步 。
"""

"""
Suppose there is a square city with sides of 10 li, and gates are opened at the middle of each side.
Both Jia and Yi start from the center of the city and leave. Yi exits through the east gate, and Jia exits through the south gate.
The exact number of steps they take to exit the gates is unknown. Jia then moves diagonally northeast, meeting Yi.
The ratio of their speeds is such that Jia moves 5 steps for every 3 steps Yi takes.
Question: how many steps do Jia and Yi each take?

The procedure says:
1. Let 5 be squared, and 3 also be squared. Add these and halve the result to obtain the diagonal movement rate.
2. Subtract the diagonal movement rate from the square of 5 to get the southward movement rate.
3. Multiply 3 by 5 to get Yi's eastward movement rate.
4. Take half the side length of the city and multiply it by the southward movement rate. Divide this by the eastward movement rate to get the number of steps Jia takes to exit the south gate.
5. Add half the side length of the city to this result to get Jia's total southward movement.
6. To find the diagonal movement, multiply the southward movement by the diagonal movement rate.
7. To find Yi's eastward movement, multiply the southward movement by the eastward movement rate.
8. Divide each result by the southward movement rate to get the respective distances.

Answer: Jia exits the south gate after *a* steps, moves diagonally northeast for *b* steps, and meets Yi. Yi moves eastward for *c* steps.
"""

from fractions import Fraction

# 城邑方十里
邑方 = 10

# 甲行五，乙行三
甲速 = 5
乙速 = 3

# 令五自乘，三亦自乘，并而半之，為邪行率
邪行率 = Fraction(甲速**2 + 乙速**2, 2)

# 邪行率減於五自乘者，餘，為南行率
南行率 = 甲速**2 - 邪行率

# 以三乘五，為乙東行率
東行率 = 乙速 * 甲速

# 置邑方半之，以南行率乘之，如東行率而一，即得出南門步數
出南門步數 = Fraction((邑方 / 2) * 南行率, 東行率)

# 以增邑方半，即南行
南行 = 出南門步數 + (邑方 / 2)

# 置南行步求弦者，以邪行率乘之
邪行 = Fraction(南行 * 邪行率, 南行率)

# 求東者以東行率乘之
東行 = Fraction(南行 * 東行率, 南行率)

# 各自為實
a = 出南門步數
b = 邪行
c = 東行
"""
Code error: both arguments should be Rational instances"""
