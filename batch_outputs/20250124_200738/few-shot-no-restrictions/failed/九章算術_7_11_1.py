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
Question: after how many days will they meet? How much will each mouse have dug?

The procedure says: Suppose after 2 days, the progress is less than 5 cun. Suppose after 3 days, the progress exceeds 3 chi 7.5 cun.
The "excess and deficiency" method says: Place the rates of progress, and the excess and deficiency below them.
Multiply the rates of progress by the respective excess and deficiency, and sum them to obtain the dividend.
Sum the excess and deficiency to obtain the divisor.
Divide the dividend by the divisor to find the number of days. If there is a fraction, simplify it.
For the progress of each mouse, use the rates of progress and calculate accordingly.

Answer: *a* days. The large mouse digs *b* chi, and the small mouse digs *c* chi.
"""

from fractions import Fraction

# 垣厚五尺
垣厚 = 5  # chi

# 大鼠日自倍，小鼠日自半
大鼠日進 = lambda n: 2 ** (n - 1)  # Large mouse's progress on day n
小鼠日進 = lambda n: Fraction(1, 2 ** (n - 1))  # Small mouse's progress on day n

# 假令二日，不足五寸
# 假令三日，有餘三尺七寸半
不足 = Fraction(5, 10)  # 5 cun = 0.5 chi
有餘 = 3 + Fraction(7.5, 10)  # 3 chi 7.5 cun = 3.75 chi

# 盈不足術
# 置所出率
大鼠率 = 大鼠日進(2) + 大鼠日進(3)  # Large mouse's progress in 2 and 3 days
小鼠率 = 小鼠日進(2) + 小鼠日進(3)  # Small mouse's progress in 2 and 3 days

# 盈、不足各居其下
盈 = 有餘
不足 = 不足

# 令維乘所出率，并以為實
實 = (大鼠率 * 盈) + (小鼠率 * 不足)

# 并盈、不足為法
法 = 盈 + 不足

# 實如法而一
a = Fraction(實, 法)  # Number of days

# 計算各鼠穿多少
大鼠穿 = sum([大鼠日進(n) for n in range(1, int(a) + 1)])
小鼠穿 = sum([小鼠日進(n) for n in range(1, int(a) + 1)])

b = 大鼠穿
c = 小鼠穿

# Final results
a, b, c#----- content ends here -----

"""
Code error: both arguments should be Rational instances"""
