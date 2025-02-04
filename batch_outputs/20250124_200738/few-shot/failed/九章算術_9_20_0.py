"""
今有邑方十里，各中開門。甲乙俱從邑中央而出。乙東出；甲南出，出門不知步數，邪向東北磨邑，適與乙會。率甲行五，乙行三。問︰甲、乙行各幾何？
術曰：令五自乘，三亦自乘，并而半之，為邪行率。邪行率減於五自乘者，餘，為南行率。以三乘五，為乙東行率。置邑方半之，以南行率乘之，如東行率而一，即得出南門步數。以增邑方半，即南行。置南行步求弦者，以邪行率乘之，求東者以東行率乘之，各自為實。實如南行率得一步。
荅曰：甲出南門 a步 ，邪東北行 b步 ，及乙。乙東行 c步 。
"""

#----- content starts here -----
"""
Suppose there is a square city with sides of 10 li, and gates are opened at the middle of each side.
Person A and Person B both start from the center of the city. 
Person B exits to the east, while Person A exits to the south. 
After exiting, Person A walks diagonally northeast along the city boundary and meets Person B. 
The walking rates are such that Person A walks 5 units while Person B walks 3 units in the same time.
Question: how far do Person A and Person B walk?

The procedure says:
Let 5 multiply itself, and let 3 multiply itself. Add these and halve the result to obtain the diagonal walking rate.
Subtract the diagonal walking rate from 5 multiplied by itself. The remainder is the southward walking rate.
Multiply 3 by 5 to obtain the eastward walking rate.
Take half the side of the city and multiply it by the southward walking rate. Divide this by the eastward walking rate to obtain the number of steps Person A takes to exit the south gate.
Add this to half the side of the city to obtain the southward distance walked by Person A.
To find the diagonal distance, multiply the southward distance by the diagonal walking rate.
To find the eastward distance, multiply the southward distance by the eastward walking rate.
Divide each result by the southward walking rate to obtain the respective distances.

Answer: Person A exits the south gate after walking *a* steps, walks *b* steps diagonally northeast, and meets Person B. Person B walks *c* steps eastward.
"""

from fractions import Fraction

# 邑方十里
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
a = 南行
b = 邪行
c = 東行#----- content ends here -----

"""
Variable 'a' has wrong value. Expected: 800, Actual: 23/3
Variable 'b' has wrong value. Expected: 9775/2, Actual: 391/24
Variable 'c' has wrong value. Expected: 8625/2, Actual: 115/8"""
