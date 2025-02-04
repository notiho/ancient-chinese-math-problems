"""
今有内營周七百二十步中營周九百六十步外營周一千二百步甲乙丙三人值夜甲行内營乙行中營丙行外營俱發南門甲行九乙行七丙行五問各行㡬何周俱到南門
術曰以内中外周步數互乗甲乙丙行率求等數約之各得行周
答曰甲行 a周 乙行 b周 丙行 c周
"""

"""
Suppose there are three enclosures: the inner enclosure with a circumference of 720 bu, the middle enclosure with a circumference of 960 bu, and the outer enclosure with a circumference of 1200 bu. 
Three people, Jia, Yi, and Bing, are assigned to patrol at night. Jia walks the inner enclosure, Yi walks the middle enclosure, and Bing walks the outer enclosure. 
They all start from the south gate. Jia walks 9 steps, Yi walks 7 steps, and Bing walks 5 steps. 
Question: how many full circuits does each person walk such that they all return to the south gate at the same time?

The procedure says: Multiply the circumferences of the inner, middle, and outer enclosures with each other. 
Use the walking rates of Jia, Yi, and Bing to find a common multiple. Simplify the result to determine how many circuits each person walks.

Answer: Jia walks *a* circuits, Yi walks *b* circuits, Bing walks *c* circuits.
"""

from fractions import Fraction

# 内營周 720 步
內營周 = 720

# 中營周 960 步
中營周 = 960

# 外營周 1200 步
外營周 = 1200

# 甲行 9 步
甲行率 = 9

# 乙行 7 步
乙行率 = 7

# 丙行 5 步
丙行率 = 5

# 以内中外周步數互乘
互乘 = 內營周 * 中營周 * 外營周

# 求等數 (最小公倍數)
甲等數 = 互乘 // 內營周 * 甲行率
乙等數 = 互乘 // 中營周 * 乙行率
丙等數 = 互乘 // 外營周 * 丙行率

# 約之 (化簡)
約數 = Fraction(甲等數, 乙等數).denominator  # Find the common denominator for simplification
甲行周 = Fraction(甲等數, 約數)
乙行周 = Fraction(乙等數, 約數)
丙行周 = Fraction(丙等數, 約數)

# 答案
a = 甲行周
b = 乙行周
c = 丙行周
"""
Variable 'a' has wrong value. Expected: 12, Actual: 10368000/7
Variable 'b' has wrong value. Expected: 7, Actual: 864000
Variable 'c' has wrong value. Expected: 4, Actual: 3456000/7"""
