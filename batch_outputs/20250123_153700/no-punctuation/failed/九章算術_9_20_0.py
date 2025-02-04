"""
今有邑方十里各中開門甲乙俱從邑中央而出乙東出甲南出出門不知步數邪向東北磨邑適與乙會率甲行五乙行三問甲乙行各幾何
術曰令五自乘三亦自乘并而半之為邪行率邪行率減於五自乘者餘為南行率以三乘五為乙東行率置邑方半之以南行率乘之如東行率而一即得出南門步數以增邑方半即南行置南行步求弦者以邪行率乘之求東者以東行率乘之各自為實實如南行率得一步
荅曰甲出南門 a步 邪東北行 b步 及乙乙東行 c步 
"""

"""
Suppose there is a square city with sides of 10 li. Each side has a gate in the middle.
Two people, Jia and Yi, start from the center of the city. Yi exits through the east gate, and Jia exits through the south gate.
The two then walk diagonally northeast along the city's boundary and meet at a point. Jia walks at a rate of 5 steps, and Yi walks at a rate of 3 steps.
Question: How many steps does Jia walk south, how many steps do they walk diagonally northeast, and how many steps does Yi walk east?

The procedure says:
- Let 5 be squared and 3 also be squared. Add these and halve the result to get the diagonal walking rate.
- Subtract the square of 5 from the diagonal walking rate to get the south walking rate.
- Multiply 3 by 5 to get the east walking rate.
- Take half the city's side length and multiply it by the south walking rate. Divide the result by the east walking rate to get the steps Jia walks south.
- Add this to half the city's side length to get the diagonal walking steps.
- To find the diagonal walking steps, multiply the diagonal walking rate by the south walking steps.
- To find the east walking steps, multiply the east walking rate by the south walking steps.
- Divide each result by the south walking rate to get the respective steps.

Answer: Jia walks *a* steps south, walks *b* steps diagonally northeast, and Yi walks *c* steps east.
"""

# 城邑方十里
邑方 = 10

# 甲行五，乙行三
甲率 = 5
乙率 = 3

# 令五自乘，三亦自乘，并而半之為邪行率
邪行率 = Fraction(甲率**2 + 乙率**2, 2)

# 邪行率減於五自乘者，餘為南行率
南行率 = 邪行率 - 甲率**2

# 以三乘五為乙東行率
東行率 = 乙率 * 甲率

# 置邑方半之
邑方半 = Fraction(邑方, 2)

# 以南行率乘之，如東行率而一，即得出南門步數
南行步數 = Fraction(邑方半 * 南行率, 東行率)

# 以增邑方半，即南行置南行步
邪行步數 = 南行步數 + 邑方半

# 求弦者，以邪行率乘之
邪行步數 = Fraction(邪行率 * 南行步數, 南行率)

# 求東者，以東行率乘之
東行步數 = Fraction(東行率 * 南行步數, 南行率)

# 各自為實，實如南行率得一步
a = 南行步數
b = 邪行步數
c = 東行步數
"""
Variable 'a' has wrong value. Expected: 800, Actual: -8/3
Variable 'b' has wrong value. Expected: 9775/2, Actual: 17/3
Variable 'c' has wrong value. Expected: 8625/2, Actual: 5"""
