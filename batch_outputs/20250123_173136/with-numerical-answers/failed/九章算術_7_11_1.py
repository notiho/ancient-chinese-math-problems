"""
今有垣厚五尺，兩鼠對穿。大鼠日一尺，小鼠亦日一尺。大鼠日自倍，小鼠日自半。問︰幾何日相逢？各穿幾何？
術曰：假令二日，不足五寸。令之三日，有餘三尺七寸半。
盈不足術曰：置所出率，盈、不足各居其下。令維乘所出率，并以為實。并盈、不足為法。實如法而一。有分者，通之。盈不足相與同其買物者，置所出率，以少減多，餘，以約法、實。實為物價，法為人數。
荅曰： a(=36/17)日 。大鼠穿 b(=59/17)尺 ，小鼠穿 c(=26/17)尺 。
"""

"""
Suppose there is a wall 5 chi thick, and two mice are digging through it from opposite sides.
The large mouse digs 1 chi per day, and the small mouse also digs 1 chi per day.
The large mouse doubles its progress each day, while the small mouse halves its progress each day.
Question: after how many days do they meet? How much does each mouse dig?

The procedure says: Suppose 2 days, the total is less than 5 cun. Suppose 3 days, the total exceeds 3 chi 7.5 cun.
The "excess and deficiency" procedure says: Place the rates of progress under the excess and deficiency values respectively.
Multiply the rates of progress by the corresponding excess or deficiency, and sum them to form the dividend.
Sum the excess and deficiency to form the divisor.
Divide the dividend by the divisor to find the number of days. If there is a fraction, simplify it.
For the amounts dug by the mice, use the same rates of progress, subtract the smaller from the larger, and reduce the dividend and divisor accordingly.
The dividend becomes the amount dug, and the divisor becomes the number of days.

Answer: *a*(=36/17) days. The large mouse digs *b*(=59/17) chi, and the small mouse digs *c*(=26/17) chi.
"""

# 垣厚五尺
垣厚 = 5

# 大鼠日一尺，小鼠亦日一尺
大鼠日進 = 1
小鼠日進 = 1

# 大鼠日自倍，小鼠日自半
大鼠進率 = [1, 2, 4]  # 每日進度倍增
小鼠進率 = [1, 0.5, 0.25]  # 每日進度減半

# 假令二日，不足五寸
不足 = Fraction(5, 10)  # 5 寸 = 0.5 尺

# 令之三日，有餘三尺七寸半
有餘 = 3 + Fraction(7, 10)  # 3 尺 7 寸半 = 3.75 尺

# 盈不足術
# 置所出率，盈、不足各居其下
盈率 = sum(大鼠進率[:3]) + sum(小鼠進率[:3])  # 3 日進度
不足率 = sum(大鼠進率[:2]) + sum(小鼠進率[:2])  # 2 日進度

# 令維乘所出率，并以為實
實 = (盈率 * 不足) + (不足率 * 有餘)

# 并盈、不足為法
法 = 有餘 + 不足

# 實如法而一
a = Fraction(實, 法)  # 36/17 日

# 各穿幾何？
# 大鼠穿
大鼠穿 = sum(大鼠進率[:3]) * a
b = Fraction(大鼠穿, 1)  # 59/17 尺

# 小鼠穿
小鼠穿 = sum(小鼠進率[:3]) * a
c = Fraction(小鼠穿, 1)  # 26/17 尺
"""
Code error: both arguments should be Rational instances"""
