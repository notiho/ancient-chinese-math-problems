"""
今有内營周七百二十步中營周九百六十步外營周一千二百步甲乙丙三人值夜甲行内營乙行中營丙行外營俱發南門甲行九乙行七丙行五問各行㡬何周俱到南門
術曰以内中外周步數互乗甲乙丙行率求等數約之各得行周
答曰甲行 a周 乙行 b周 丙行 c周
"""

"""
Suppose there are three circular paths: the inner path has a circumference of 720 bu, the middle path has a circumference of 960 bu, and the outer path has a circumference of 1200 bu.
Three people, Jia, Yi, and Bing, are assigned to patrol these paths at night. Jia walks the inner path, Yi walks the middle path, and Bing walks the outer path.
They all start from the southern gate. Jia walks 9 steps per unit of time, Yi walks 7 steps per unit of time, and Bing walks 5 steps per unit of time.
Question: how many complete laps does each person walk before they all return to the southern gate at the same time?

The procedure says: Multiply the circumferences of the inner, middle, and outer paths with each other.
Use the walking rates of Jia, Yi, and Bing to find a common multiple.
Simplify the result to find the number of laps each person walks.

Answer: Jia walks *a* laps, Yi walks *b* laps, and Bing walks *c* laps.
"""

# 内營周七百二十步
內營周 = 720

# 中營周九百六十步
中營周 = 960

# 外營周一千二百步
外營周 = 1200

# 甲行9
甲行率 = 9

# 乙行7
乙行率 = 7

# 丙行5
丙行率 = 5

# 以内中外周步數互乘
總周 = 內營周 * 中營周 * 外營周

# 甲乙丙行率求等數
甲等數 = 總周 // 內營周 // 甲行率
乙等數 = 總周 // 中營周 // 乙行率
丙等數 = 總周 // 外營周 // 丙行率

# 約之各得行周
最大公約數 = gcd(甲等數, gcd(乙等數, 丙等數))
a = Fraction(甲等數, 最大公約數)
b = Fraction(乙等數, 最大公約數)
c = Fraction(丙等數, 最大公約數)
"""
Code error: name 'gcd' is not defined"""
