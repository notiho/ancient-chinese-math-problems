"""
今有邑方十里，各中開門。甲乙俱從邑中央而出。乙東出；甲南出，出門不知步數，邪向東北磨邑，適與乙會。率甲行五，乙行三。問︰甲、乙行各幾何？
術曰：令五自乘，三亦自乘，并而半之，為邪行率。邪行率減於五自乘者，餘，為南行率。以三乘五，為乙東行率。置邑方半之，以南行率乘之，如東行率而一，即得出南門步數。以增邑方半，即南行。置南行步求弦者，以邪行率乘之，求東者以東行率乘之，各自為實。實如南行率得一步。
荅曰：甲出南門 a步 ，邪東北行 b步 ，及乙。乙東行 c步 。
"""

#----- content starts here -----
"""
Suppose there is a square city with sides of 10 li, and gates are opened at the middle of each side.
Both Jia and Yi start from the center of the city and exit.
Yi exits east, and Jia exits south. After exiting the gates, they do not know how many steps they take.
Jia then moves diagonally toward the northeast along the edge of the city and meets Yi.
The ratio of their speeds is such that Jia moves 5 while Yi moves 3.
Question: how far do Jia and Yi each travel?

The procedure says:
Let 5 multiply itself, and let 3 multiply itself. Add these and halve the result to obtain the diagonal movement ratio.
Subtract the diagonal movement ratio from 5 multiplied by itself; the remainder is the southward movement ratio.
Multiply 3 by 5 to obtain Yi's eastward movement ratio.
Take half of the city's side length and multiply it by the southward movement ratio. Divide the result by the eastward movement ratio to obtain the number of steps Jia takes to exit the south gate.
Add this to half the city's side length to obtain the total southward movement of Jia.
To find the diagonal movement, multiply the southward movement by the diagonal movement ratio.
To find the eastward movement of Yi, multiply the southward movement by the eastward movement ratio.
Divide each result by the southward movement ratio to obtain the respective distances.

Answer: Jia exits the south gate and moves *a* steps south, moves *b* steps diagonally northeast, and meets Yi. Yi moves *c* steps east.
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
南門步數 = Fraction((邑方 / 2) * 南行率, 東行率)

# 以增邑方半，即南行
南行 = 南門步數 + (邑方 / 2)

# 置南行步求弦者，以邪行率乘之
邪行 = Fraction(南行 * 邪行率, 南行率)

# 求東者以東行率乘之
東行 = Fraction(南行 * 東行率, 南行率)

# 答案
a = 南行
b = 邪行
c = 東行#----- content ends here -----

"""
Code error: both arguments should be Rational instances"""
