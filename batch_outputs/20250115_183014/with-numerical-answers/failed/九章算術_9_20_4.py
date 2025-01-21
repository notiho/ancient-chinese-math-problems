"""
今有邑方十里，各中開門。甲乙俱從邑中央而出。乙東出；甲南出，出門不知步數，邪向東北磨邑，適與乙會。率甲行五，乙行三。問︰甲、乙行各幾何？
術曰：令五自乘，三亦自乘，并而半之，為邪行率。邪行率減於五自乘者，餘，為南行率。以三乘五，為乙東行率。置邑方半之，以南行率乘之，如東行率而一，即得出南門步數。以增邑方半，即南行。置南行步求弦者，以邪行率乘之，求東者以東行率乘之，各自為實。實如南行率得一步。
荅曰：甲出南門 a(=800)步 ，邪東北行 b(=9775/2)步 ，及乙。乙東行 c(=8625/2)步 。
"""

"""
Suppose there is a square city with sides of 10 li, and gates are opened at the middle of each side.
Jia and Yi both start from the center of the city. Yi exits through the east gate, while Jia exits through the south gate.
The number of steps taken to exit the gates is unknown. Jia then moves diagonally northeast along the city boundary and meets Yi.
The ratio of their speeds is such that Jia travels 5 units for every 3 units Yi travels.
Question: How far do Jia and Yi each travel?

The procedure says:
Let 5 square itself, and 3 also square itself. Add these and halve the result to obtain the diagonal travel rate.
Subtract the diagonal travel rate from 5 squared to get the southward travel rate.
Multiply 3 by 5 to obtain Yi's eastward travel rate.
Take half the city's side length, multiply it by the southward travel rate, and divide by the eastward travel rate to find the number of steps Jia takes to exit the south gate.
Add this to half the city's side length to get Jia's total southward travel.
To find the diagonal distance, multiply the southward travel by the diagonal travel rate.
To find the eastward distance, multiply the southward travel by the eastward travel rate.
Divide each result by the southward travel rate to find the respective distances.

Answer: Jia exits the south gate and travels *a*(=800) steps south, then travels diagonally northeast for *b*(=9775/2) steps to meet Yi. Yi travels *c*(=8625/2) steps east.
"""

from fractions import Fraction

# 城邑方十里，各中開門
邑方 = 10  # li
邑方半 = Fraction(邑方, 2)  # Half the city's side length

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
出南門步數 = Fraction(邑方半 * 南行率, 東行率)

# 以增邑方半，即南行
南行 = 出南門步數 + 邑方半

# 置南行步求弦者，以邪行率乘之
邪行 = Fraction(南行 * 邪行率, 南行率)

# 求東者以東行率乘之
東行 = Fraction(南行 * 東行率, 南行率)

# 答案
a = 出南門步數  # 800
b = 邪行  # 9775/2
c = 東行  # 8625/2
"""
Variable 'a' has wrong value. Expected: 800, Actual: 8/3
Variable 'b' has wrong value. Expected: 9775/2, Actual: 391/24
Variable 'c' has wrong value. Expected: 8625/2, Actual: 115/8"""
