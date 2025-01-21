"""
今有垣厚五尺，兩鼠對穿。大鼠日一尺，小鼠亦日一尺。大鼠日自倍，小鼠日自半。問︰幾何日相逢？各穿幾何？
術曰：假令二日，不足五寸。令之三日，有餘三尺七寸半。
盈不足術曰：置所出率，盈、不足各居其下。令維乘所出率，并以為實。并盈、不足為法。實如法而一。有分者，通之。盈不足相與同其買物者，置所出率，以少減多，餘，以約法、實。實為物價，法為人數。荅曰： a日 。大鼠穿 b尺 ，小鼠穿 c尺 。
"""

"""
Suppose there is a wall 5 chi thick, and two mice are digging through it from opposite sides.
The large mouse digs 1 chi per day, and the small mouse also digs 1 chi per day.
However, the large mouse doubles its daily progress each day, while the small mouse halves its daily progress each day.
Question: after how many days do they meet? How far does each mouse dig?

The procedure says: Suppose 2 days, it is insufficient by 5 cun. Suppose 3 days, it exceeds by 3 chi 7 cun and a half.
The "Excess and Deficiency" procedure says: Place the rates of progress, and the excess and deficiency below each rate respectively.
Multiply each rate by its respective excess or deficiency, and sum them to obtain the dividend.
Sum the excess and deficiency to obtain the divisor.
Divide the dividend by the divisor to obtain the number of days.
If there is a remainder, simplify it.
For the distances dug by each mouse, use the rates of progress, subtract the smaller from the larger, and simplify accordingly.
The dividend represents the total progress, and the divisor represents the number of days.

Answer: *a* days. The large mouse digs *b* chi, and the small mouse digs *c* chi.
"""

# 垣厚五尺
垣厚 = 5

# 大鼠日自倍，小鼠日自半
# 大鼠日一尺
大鼠初速 = 1
# 小鼠亦日一尺
小鼠初速 = 1

# 假令二日，不足五寸
不足 = Fraction(5, 10)  # 5 cun = 5/10 chi

# 令之三日，有餘三尺七寸半
有餘 = 3 + Fraction(7.5, 10)  # 3 chi 7.5 cun = 3 + 7.5/10 chi

# 盈不足術
# 置所出率
大鼠率 = 大鼠初速 * 2  # 大鼠日自倍
小鼠率 = 小鼠初速 / 2  # 小鼠日自半

# 盈、不足各居其下
# Multiply rates by respective excess or deficiency
大鼠實 = 大鼠率 * 有餘
小鼠實 = 小鼠率 * 不足

# 并以為實
實 = 大鼠實 + 小鼠實

# 并盈、不足為法
法 = 有餘 + 不足

# 實如法而一
a = Fraction(實, 法)

# 大鼠穿
b = 大鼠初速 * (2 ** (a - 1))

# 小鼠穿
c = 小鼠初速 * (1 / (2 ** (a - 1)))
"""
Code error: both arguments should be Rational instances"""
