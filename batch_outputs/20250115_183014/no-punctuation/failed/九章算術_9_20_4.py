"""
今有邑方十里各中開門甲乙俱從邑中央而出乙東出甲南出出門不知步數邪向東北磨邑適與乙會率甲行五乙行三問甲乙行各幾何
術曰令五自乘三亦自乘并而半之為邪行率邪行率減於五自乘者餘為南行率以三乘五為乙東行率置邑方半之以南行率乘之如東行率而一即得出南門步數以增邑方半即南行置南行步求弦者以邪行率乘之求東者以東行率乘之各自為實實如南行率得一步
荅曰甲出南門 a步 邪東北行 b步 及乙乙東行 c步 
"""

"""
Suppose there is a square city with sides of 10 li. Each side has a gate in the middle. 
Two individuals, Jia and Yi, both start from the center of the city. Yi exits through the east gate, and Jia exits through the south gate. 
The distance they walk is unknown. Jia walks diagonally northeast to meet Yi, who is walking east. 
Jia walks at a rate of 5 while Yi walks at a rate of 3. 
Question: How far do Jia and Yi walk, respectively?

The procedure says:
1. Square 5 and square 3, then add them together and halve the result. This gives the diagonal rate.
2. Subtract the square of 5 from the diagonal rate. The remainder is the southward rate.
3. Multiply 3 by 5 to get the eastward rate.
4. Take half the side of the city and multiply it by the southward rate. Divide by the eastward rate to get the southward distance.
5. Add this southward distance to half the side of the city to get the total southward distance.
6. To find the diagonal distance, multiply the diagonal rate by the southward distance.
7. To find the eastward distance, multiply the eastward rate by the southward distance.
8. Divide each result by the southward rate to get the respective distances.

Answer: Jia exits the south gate and walks *a* bu south, *b* bu northeast diagonally, and Yi walks *c* bu east.
"""

# 城邑方十里
邑方 = 10

# 甲行五，乙行三
甲率 = 5
乙率 = 3

# 令五自乘，三亦自乘，并而半之，為邪行率
邪行率 = Fraction((甲率**2 + 乙率**2), 2)

# 邪行率減於五自乘者，餘為南行率
南行率 = 邪行率 - 甲率**2

# 以三乘五，為乙東行率
東行率 = 乙率 * 甲率

# 置邑方半之
邑方半 = Fraction(邑方, 2)

# 以南行率乘之，如東行率而一，即得出南門步數
南門步數 = Fraction(邑方半 * 南行率, 東行率)

# 以增邑方半，即南行
南行 = 南門步數 + 邑方半

# 置南行步，求弦者，以邪行率乘之
弦步 = Fraction(邪行率 * 南行, 南行率)

# 求東者，以東行率乘之
東步 = Fraction(東行率 * 南行, 南行率)

# 各自為實，實如南行率得一步
a = 南行
b = 弦步
c = 東步
"""
Variable 'a' has wrong value. Expected: 800, Actual: 7/3
Variable 'b' has wrong value. Expected: 9775/2, Actual: -119/24
Variable 'c' has wrong value. Expected: 8625/2, Actual: -35/8"""
