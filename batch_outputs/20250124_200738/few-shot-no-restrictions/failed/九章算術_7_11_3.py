"""
今有垣厚五尺，兩鼠對穿。大鼠日一尺，小鼠亦日一尺。大鼠日自倍，小鼠日自半。問︰幾何日相逢？各穿幾何？
術曰：假令二日，不足五寸。令之三日，有餘三尺七寸半。
盈不足術曰：置所出率，盈、不足各居其下。令維乘所出率，并以為實。并盈、不足為法。實如法而一。有分者，通之。盈不足相與同其買物者，置所出率，以少減多，餘，以約法、實。實為物價，法為人數。
荅曰： a日 。大鼠穿 b尺 ，小鼠穿 c尺 。
"""

#----- content starts here -----
"""
Suppose there is a wall 5 chi thick, and two mice are digging through it from opposite sides.
The large mouse digs 1 chi per day, and the small mouse also digs 1 chi per day.
However, the large mouse doubles its daily progress each day, while the small mouse halves its daily progress each day.
Question: after how many days do they meet? How far does each mouse dig?

The procedure says: Suppose after 2 days, the total progress is less than 5 cun. Suppose after 3 days, the total progress exceeds 3 chi 7.5 cun.
The "Excess and Deficiency" method says: Place the rates of progress for each day, and place the excess and deficiency below them.
Multiply the rates of progress by the corresponding excess or deficiency, and sum them to obtain the dividend.
Sum the excess and deficiency to obtain the divisor.
Divide the dividend by the divisor to find the number of days. If there is a remainder, adjust accordingly.
To find the distances dug by each mouse, use their respective rates of progress for the calculated number of days.

Answer: *a* days. The large mouse digs *b* chi, and the small mouse digs *c* chi.
"""

from fractions import Fraction

# 垣厚五尺
垣厚 = 5  # chi

# 大鼠日一尺，小鼠亦日一尺
大鼠初速 = 1  # chi/day
小鼠初速 = 1  # chi/day

# 大鼠日自倍，小鼠日自半
大鼠速率 = lambda 日: 大鼠初速 * (2 ** (日 - 1))
小鼠速率 = lambda 日: 小鼠初速 * (1 / (2 ** (日 - 1)))

# 盈不足術
# 假令二日，不足五寸 (5 cun = 5/10 chi)
不足 = Fraction(5, 10)  # chi
# 令之三日，有餘三尺七寸半 (3 chi 7.5 cun = 3 + 7.5/10 chi)
有餘 = 3 + Fraction(7.5, 10)  # chi

# Rates of progress for 2 days and 3 days
大鼠二日 = 大鼠速率(1) + 大鼠速率(2)
小鼠二日 = 小鼠速率(1) + 小鼠速率(2)
總進度二日 = 大鼠二日 + 小鼠二日

大鼠三日 = 大鼠速率(1) + 大鼠速率(2) + 大鼠速率(3)
小鼠三日 = 小鼠速率(1) + 小鼠速率(2) + 小鼠速率(3)
總進度三日 = 大鼠三日 + 小鼠三日

# 盈不足術計算
# 置所出率
所出率二日 = 總進度二日
所出率三日 = 總進度三日

# 盈、不足各居其下
盈 = 有餘
不足 = 垣厚 - 不足

# 令維乘所出率，并以為實
實 = (所出率二日 * 盈) + (所出率三日 * 不足)

# 并盈、不足為法
法 = 盈 + 不足

# 實如法而一
a = Fraction(實, 法)

# 計算各鼠穿距離
大鼠穿 = sum(大鼠速率(日) for 日 in range(1, int(a) + 1))
小鼠穿 = sum(小鼠速率(日) for 日 in range(1, int(a) + 1))

b = 大鼠穿
c = 小鼠穿

# Output results
a, b, c#----- content ends here -----

"""
Code error: both arguments should be Rational instances"""
