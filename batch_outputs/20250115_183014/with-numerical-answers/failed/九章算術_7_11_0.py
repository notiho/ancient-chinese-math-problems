"""
今有垣厚五尺，兩鼠對穿。大鼠日一尺，小鼠亦日一尺。大鼠日自倍，小鼠日自半。問︰幾何日相逢？各穿幾何？
術曰：假令二日，不足五寸。令之三日，有餘三尺七寸半。
盈不足術曰：置所出率，盈、不足各居其下。令維乘所出率，并以為實。并盈、不足為法。實如法而一。有分者，通之。盈不足相與同其買物者，置所出率，以少減多，餘，以約法、實。實為物價，法為人數。荅曰： a(=36/17)日 。大鼠穿 b(=59/17)尺 ，小鼠穿 c(=26/17)尺 。
"""

"""
Suppose there is a wall 5 chi thick, and two mice are digging through it from opposite sides.
The large mouse digs 1 chi per day, and the small mouse also digs 1 chi per day.
The large mouse doubles its progress each day, while the small mouse halves its progress each day.
Question: after how many days will they meet? How much will each mouse have dug?

The procedure says: Suppose after 2 days, the progress is less than 5 cun. Suppose after 3 days, the progress exceeds 3 chi 7 cun and a half.
The "Excess and Deficiency" procedure says: Place the rates of progress, and the excess and deficiency below each rate.
Multiply each rate by the corresponding excess or deficiency, and sum them to obtain the dividend.
Sum the excess and deficiency to obtain the divisor.
Divide the dividend by the divisor to find the number of days. If there is a remainder, simplify it.
For the progress of each mouse, use the same rates. Subtract the smaller rate from the larger rate, and use the remainder to simplify the divisor and dividend.
The dividend represents the progress, and the divisor represents the number of days.

Answer: *a*(=36/17) days. The large mouse digs *b*(=59/17) chi, and the small mouse digs *c*(=26/17) chi.
"""

from fractions import Fraction

# 垣厚五尺
垣厚 = 5

# 大鼠日一尺，小鼠亦日一尺
大鼠日進 = 1
小鼠日進 = 1

# 大鼠日自倍，小鼠日自半
大鼠進率 = [1, 2]  # 每日進度倍增
小鼠進率 = [1, Fraction(1, 2)]  # 每日進度減半

# 假令二日，不足五寸
不足 = Fraction(5, 10)  # 5 寸 = 1/2 尺

# 令之三日，有餘三尺七寸半
有餘 = 3 + Fraction(7, 10) + Fraction(5, 20)  # 3 尺 7 寸半 = 3 + 7/10 + 1/20

# 盈不足術
# 置所出率，盈、不足各居其下
大鼠率 = 大鼠日進 * 2  # 2 日
小鼠率 = 小鼠日進 * 2  # 2 日

# 盈、不足
盈 = 有餘
不足 = 不足

# 令維乘所出率，并以為實
實 = (大鼠率 * 盈) + (小鼠率 * 不足)

# 并盈、不足為法
法 = 盈 + 不足

# 實如法而一
a = Fraction(實, 法)  # 36/17 日

# 大鼠穿
大鼠穿 = 大鼠日進 * a + 大鼠日進 * (a - 1) 
"""
Variable 'a' has wrong value. Expected: 36/17, Actual: 2
Missing variable in output: 'b'
Missing variable in output: 'c'"""
