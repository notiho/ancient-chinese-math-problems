"""
今有邑方十里，各中開門。甲乙俱從邑中央而出。乙東出；甲南出，出門不知步數，邪向東北磨邑，適與乙會。率甲行五，乙行三。問︰甲、乙行各幾何？
術曰：令五自乘，三亦自乘，并而半之，為邪行率。邪行率減於五自乘者，餘，為南行率。以三乘五，為乙東行率。置邑方半之，以南行率乘之，如東行率而一，即得出南門步數。以增邑方半，即南行。置南行步求弦者，以邪行率乘之，求東者以東行率乘之，各自為實。實如南行率得一步。
荅曰：甲出南門 a(=800)步 ，邪東北行 b(=9775/2)步 ，及乙。乙東行 c(=8625/2)步 。
"""

#----- content starts here -----
"""
Suppose there is a square city of 10 li on each side, with gates at the middle of each side.
Jia and Yi both start from the center of the city. Yi exits through the east gate, and Jia exits through the south gate.
The number of steps they take to exit the gates is unknown. Jia then moves diagonally northeast along the city boundary and meets Yi.
The ratio of their walking speeds is such that Jia walks 5 steps for every 3 steps Yi walks.
Question: how far do Jia and Yi walk respectively?

The procedure says:
Let 5 multiply itself, and let 3 multiply itself. Add these and halve the result to obtain the diagonal walking rate.
Subtract the diagonal walking rate from 5 multiplied by itself; the remainder is the south walking rate.
Multiply 3 by 5 to obtain the east walking rate.
Take half the side length of the city and multiply it by the south walking rate. Divide this by the east walking rate to obtain the number of steps Jia takes to exit the south gate.
Add this to half the side length of the city to obtain Jia's total southward walking distance.
To find the diagonal distance, multiply the southward walking distance by the diagonal walking rate.
To find the eastward distance, multiply the southward walking distance by the east walking rate.
Divide each result by the south walking rate to obtain the respective distances.

Answer: Jia exits the south gate and walks *a*(=800) steps, then walks diagonally northeast *b*(=9775/2) steps to meet Yi.
Yi walks *c*(=8625/2) steps eastward.
"""

from fractions import Fraction

# 邑方十里
邑方 = 10 * 1800  # Convert li to steps (1 li = 1800 steps)

# 各中開門 (half the side length of the city)
邑方半 = Fraction(邑方, 2)

# 率甲行五，乙行三
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
c = 東行  # 8625/2#----- content ends here -----

"""
Variable 'a' has wrong value. Expected: 800, Actual: 4800
Variable 'b' has wrong value. Expected: 9775/2, Actual: 29325
Variable 'c' has wrong value. Expected: 8625/2, Actual: 25875"""
