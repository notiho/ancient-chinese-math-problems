"""
今有邑方十里各中開門甲乙俱從邑中央而出乙東出甲南出出門不知步數邪向東北磨邑適與乙會率甲行五乙行三問甲乙行各幾何
術曰令五自乘三亦自乘并而半之為邪行率邪行率減於五自乘者餘為南行率以三乘五為乙東行率置邑方半之以南行率乘之如東行率而一即得出南門步數以增邑方半即南行置南行步求弦者以邪行率乘之求東者以東行率乘之各自為實實如南行率得一步
荅曰甲出南門 a步 邪東北行 b步 及乙乙東行 c步 
"""

#----- content starts here -----
"""
Suppose there is a square city with sides of 10 li. Each side has a gate at its center.
Person A exits the city center heading south, and Person B exits heading east. 
They meet at a point northeast of the city while walking at different rates: A walks 5 units for every 3 units B walks.
Question: How far does A walk south, how far do they walk diagonally, and how far does B walk east?

The procedure says:
1. Let 5 (A's rate) be squared, and 3 (B's rate) also be squared. Add them together and halve the result to get the diagonal rate.
2. Subtract A's squared rate from the diagonal rate to get the southward rate.
3. Multiply 3 (B's rate) by 5 (A's rate) to get the eastward rate.
4. Take half the city's side length and multiply it by the southward rate. Divide by the eastward rate to get the southward distance.
5. Add the southward distance to half the city's side length to get the total southward distance.
6. To find the diagonal distance, multiply the diagonal rate by the southward distance.
7. To find the eastward distance, multiply the eastward rate by the southward distance.
8. Divide each result by the southward rate to get the respective distances.

Answer: A exits the south gate and walks *a* bu, walks diagonally *b* bu, and B walks east *c* bu.
"""

from fractions import Fraction

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
南行步數 = Fraction(邑方半 * 南行率, 東行率)

# 以增邑方半，即南行置南行步
南行步 = 南行步數 + 邑方半

# 求弦者，以邪行率乘之
弦步 = Fraction(邪行率 * 南行步, 南行率)

# 求東者，以東行率乘之
東步 = Fraction(東行率 * 南行步, 南行率)

# 各自為實，實如南行率得一步
a = 南行步
b = 弦步
c = 東步#----- content ends here -----

"""
Variable 'a' has wrong value. Expected: 800, Actual: 7/3
Variable 'b' has wrong value. Expected: 9775/2, Actual: -119/24
Variable 'c' has wrong value. Expected: 8625/2, Actual: -35/8"""
