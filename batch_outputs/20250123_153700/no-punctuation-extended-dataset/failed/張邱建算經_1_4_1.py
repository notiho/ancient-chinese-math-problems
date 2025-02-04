"""
今有内營周七百二十步中營周九百六十步外營周一千二百步甲乙丙三人值夜甲行内營乙行中營丙行外營俱發南門甲行九乙行七丙行五問各行㡬何周俱到南門
術曰以内中外周步數互乗甲乙丙行率求等數約之各得行周
答曰甲行 a周 乙行 b周 丙行 c周
"""

"""
Suppose there are three circular walls: the inner wall has a circumference of 720 bu, the middle wall has a circumference of 960 bu, and the outer wall has a circumference of 1200 bu. 
Three people, Jia, Yi, and Bing, are assigned to patrol at night. Jia walks along the inner wall, Yi walks along the middle wall, and Bing walks along the outer wall. 
They all start from the south gate. Jia walks 9 steps per unit time, Yi walks 7 steps per unit time, and Bing walks 5 steps per unit time.
Question: how many laps does each person walk so that they all return to the south gate at the same time?

The procedure says: Multiply the circumferences of the inner, middle, and outer walls with each other. 
Use the walking rates of Jia, Yi, and Bing to find the common multiple. Simplify the result to find the number of laps each person walks.

Answer: Jia walks *a* laps, Yi walks *b* laps, and Bing walks *c* laps.
"""

# 内營周七百二十步
內營周 = 720

# 中營周九百六十步
中營周 = 960

# 外營周一千二百步
外營周 = 1200

# 甲行九
甲行率 = 9

# 乙行七
乙行率 = 7

# 丙行五
丙行率 = 5

# 以内中外周步數互乘
總步數 = 內營周 * 中營周 * 外營周

# 甲乙丙行率求等數
甲等數 = 總步數 // 甲行率
乙等數 = 總步數 // 乙行率
丙等數 = 總步數 // 丙行率

# 約之各得行周
a = Fraction(甲等數, 內營周)
b = Fraction(乙等數, 中營周)
c = Fraction(丙等數, 外營周)
"""
Variable 'a' has wrong value. Expected: 12, Actual: 128000
Variable 'b' has wrong value. Expected: 7, Actual: 29622857/240
Variable 'c' has wrong value. Expected: 4, Actual: 138240"""
