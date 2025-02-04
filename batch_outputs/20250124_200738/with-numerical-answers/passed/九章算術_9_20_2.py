"""
今有邑方十里，各中開門。甲乙俱從邑中央而出。乙東出；甲南出，出門不知步數，邪向東北磨邑，適與乙會。率甲行五，乙行三。問︰甲、乙行各幾何？
術曰：令五自乘，三亦自乘，并而半之，為邪行率。邪行率減於五自乘者，餘，為南行率。以三乘五，為乙東行率。置邑方半之，以南行率乘之，如東行率而一，即得出南門步數。以增邑方半，即南行。置南行步求弦者，以邪行率乘之，求東者以東行率乘之，各自為實。實如南行率得一步。
荅曰：甲出南門 a(=800)步 ，邪東北行 b(=9775/2)步 ，及乙。乙東行 c(=8625/2)步 。
"""

#----- content starts here -----
"""
Suppose there is a square city with sides of 10 li, and gates are opened at the middle of each side.
Jia and Yi both start from the center of the city. Yi exits through the east gate, and Jia exits through the south gate.
The number of steps taken to exit the gates is unknown. Jia then moves diagonally northeast along the city boundary and meets Yi.
The ratio of Jia's speed to Yi's speed is 5:3.
Question: How many steps do Jia and Yi each take?

The procedure says:
Let 5 multiply itself, and let 3 also multiply itself. Add these and halve the result to obtain the diagonal movement ratio.
Subtract the diagonal movement ratio from 5 multiplied by itself; the remainder is the southward movement ratio.
Multiply 3 by 5 to obtain Yi's eastward movement ratio.
Take half the side of the city and multiply it by the southward movement ratio. Divide this by the eastward movement ratio to obtain the number of steps Jia takes to exit the south gate.
Add this to half the side of the city to obtain the total southward movement of Jia.
To find the diagonal movement, multiply the southward movement by the diagonal movement ratio.
To find the eastward movement of Yi, multiply the southward movement by the eastward movement ratio.
Each of these becomes its own dividend. Divide each by the southward movement ratio to obtain the respective distances.

Answer: Jia exits the south gate and moves *a*(=800) steps southward, then moves diagonally northeast *b*(=9775/2) steps to meet Yi. Yi moves *c*(=8625/2) steps eastward.
"""

from fractions import Fraction

# 城邑方十里
邑方 = 10 * 300  # Convert li to bu (1 li = 300 bu)

# 速率比：甲行五，乙行三
甲速率 = 5
乙速率 = 3

# 令五自乘，三亦自乘，并而半之，為邪行率
甲速率平方 = 甲速率 ** 2
乙速率平方 =乙速率 ** 2
邪行率 = Fraction(甲速率平方 + 乙速率平方, 2)

# 邪行率減於五自乘者，餘，為南行率
南行率 = 甲速率平方 - 邪行率

# 以三乘五，為乙東行率
東行率 = 乙速率 * 甲速率

# 置邑方半之
邑方半 = Fraction(邑方, 2)

# 以南行率乘之，如東行率而一，即得出南門步數
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
"""
