"""
今有邑方十里，各中開門。甲乙俱從邑中央而出。乙東出；甲南出，出門不知步數，邪向東北磨邑，適與乙會。率甲行五，乙行三。問︰甲、乙行各幾何？
術曰：令五自乘，三亦自乘，并而半之，為邪行率。邪行率減於五自乘者，餘，為南行率。以三乘五，為乙東行率。置邑方半之，以南行率乘之，如東行率而一，即得出南門步數。以增邑方半，即南行。置南行步求弦者，以邪行率乘之，求東者以東行率乘之，各自為實。實如南行率得一步。
荅曰：甲出南門 a步 ，邪東北行 b步 ，及乙。乙東行 c步 。
"""

"""
Suppose there is a square city with sides of 10 li, and gates are opened at the middle of each side.
Both Jia and Yi start from the center of the city and exit. Yi exits east, and Jia exits south. 
After exiting the gates, Jia does not know how many steps he takes but moves diagonally northeast and meets Yi.
The ratio of Jia's movement to Yi's movement is 5:3.
Question: how far do Jia and Yi each travel?

The procedure says: Square 5, and square 3, then add them together and halve the result. This gives the diagonal movement ratio.
Subtract the diagonal movement ratio from the square of 5. The remainder is the southward movement ratio.
Multiply 3 by 5 to get Yi's eastward movement ratio.
Take half of the city's side length, multiply it by the southward movement ratio, and divide it by the eastward movement ratio. This gives the number of steps Jia takes to exit the south gate.
Add this to half of the city's side length to get Jia's southward movement.
To find the diagonal movement, multiply the southward movement by the diagonal movement ratio.
To find Yi's eastward movement, multiply the southward movement by the eastward movement ratio.
Divide each result by the southward movement ratio to get the actual distances.

Answer: Jia exits the south gate and moves *a* steps south, then moves *b* steps diagonally northeast to meet Yi. Yi moves *c* steps east.
"""

from fractions import Fraction

# 城邑方十里
邑方 = 10

# 甲行五，乙行三
甲率 = 5
乙率 = 3

# 令五自乘，三亦自乘，并而半之，為邪行率
邪行率 = Fraction(甲率**2 + 乙率**2, 2)

# 邪行率減於五自乘者，餘，為南行率
南行率 = 甲率**2 - 邪行率

# 以三乘五，為乙東行率
東行率 = 乙率 * 甲率

# 置邑方半之
邑半 = Fraction(邑方, 2)

# 以南行率乘之，如東行率而一，即得出南門步數
出南門步數 = Fraction(邑半 * 南行率, 東行率)

# 以增邑方半，即南行
南行 = 出南門步數 + 邑半

# 置南行步求弦者，以邪行率乘之
邪行 = Fraction(南行 * 邪行率, 南行率)

# 求東者以東行率乘之
東行 = Fraction(南行 * 東行率, 南行率)

# 各自為實
a = 南行
b = 邪行
c = 東行
"""
Variable 'a' has wrong value. Expected: 800, Actual: 23/3
Variable 'b' has wrong value. Expected: 9775/2, Actual: 391/24
Variable 'c' has wrong value. Expected: 8625/2, Actual: 115/8"""
