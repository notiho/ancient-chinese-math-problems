"""
今有邑方十里各中開門甲乙俱從邑中央而出乙東出甲南出出門不知步數邪向東北磨邑適與乙會率甲行五乙行三問甲乙行各幾何
術曰令五自乘三亦自乘并而半之為邪行率邪行率減於五自乘者餘為南行率以三乘五為乙東行率置邑方半之以南行率乘之如東行率而一即得出南門步數以增邑方半即南行置南行步求弦者以邪行率乘之求東者以東行率乘之各自為實實如南行率得一步
荅曰甲出南門 a步 邪東北行 b步 及乙乙東行 c步 
"""

#----- content starts here -----
"""
Suppose there is a square city of 10 li on each side. Each side has a gate in the middle.
Two people, Jia and Yi, start from the center of the city and walk out.
Yi exits through the east gate, and Jia exits through the south gate. 
They then walk diagonally northeast and meet at a point outside the city.
Jia walks at a rate of 5 steps for every 3 steps of Yi.
Question: how many steps does Jia walk south, how many steps do they walk diagonally northeast, and how many steps does Yi walk east?

The procedure says:
Let 5 multiply itself, and let 3 multiply itself. Add them together and halve the result to obtain the diagonal walking rate.
Subtract the square of 5 from the diagonal walking rate to obtain the south walking rate.
Multiply 3 by 5 to obtain the east walking rate.
Take half of the city's side length and multiply it by the south walking rate.
Divide the result by the east walking rate to obtain the number of steps Jia walks south to exit the south gate.
Add this to half the city's side length to obtain the total south walking steps.
To find the diagonal walking steps, multiply the diagonal walking rate by the south walking steps.
To find the east walking steps, multiply the east walking rate by the south walking steps.
Divide each result by the south walking rate to obtain the respective steps.

Answer: Jia exits the south gate in *a* steps, walks diagonally northeast for *b* steps, and Yi walks east for *c* steps.
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
邑半 = Fraction(邑方, 2)

# 以南行率乘之，如東行率而一，即得出南門步數
南門步數 = Fraction(邑半 * 南行率, 東行率)

# 以增邑方半，即南行
南行 = 南門步數 + 邑半

# 置南行步，求弦者，以邪行率乘之
弦步 = Fraction(邪行率 * 南行, 南行率)

# 求東者，以東行率乘之
東步 = Fraction(東行率 * 南行, 南行率)

# 各自為實，實如南行率得一步
a = 南行
b = 弦步
c = 東步#----- content ends here -----

"""
Variable 'a' has wrong value. Expected: 800, Actual: 7/3
Variable 'b' has wrong value. Expected: 9775/2, Actual: -119/24
Variable 'c' has wrong value. Expected: 8625/2, Actual: -35/8"""
