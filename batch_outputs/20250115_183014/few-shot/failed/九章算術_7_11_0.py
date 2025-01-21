"""
今有垣厚五尺，兩鼠對穿。大鼠日一尺，小鼠亦日一尺。大鼠日自倍，小鼠日自半。問︰幾何日相逢？各穿幾何？
術曰：假令二日，不足五寸。令之三日，有餘三尺七寸半。
盈不足術曰：置所出率，盈、不足各居其下。令維乘所出率，并以為實。并盈、不足為法。實如法而一。有分者，通之。盈不足相與同其買物者，置所出率，以少減多，餘，以約法、實。實為物價，法為人數。荅曰： a日 。大鼠穿 b尺 ，小鼠穿 c尺 。
"""

"""
Suppose there is a wall 5 chi thick, and two mice are digging through it from opposite sides.
The large mouse digs 1 chi per day, and the small mouse also digs 1 chi per day.
However, the large mouse doubles its progress each day, while the small mouse halves its progress each day.
Question: after how many days do they meet? How much does each mouse dig?

The procedure says: Suppose for 2 days, the total is less than 5 cun. Suppose for 3 days, the total exceeds 3 chi 7 cun and a half.
The "Excess and Deficit" procedure says: Place the rates of progress under the respective excess and deficit. Multiply the rates by the respective excess or deficit, and add them together to form the dividend. Add the excess and deficit together to form the divisor. Divide the dividend by the divisor to find the number of days. If there is a fraction, simplify it. To find the amount dug by each mouse, use the rates of progress, subtract the smaller from the larger, and simplify the result.

Answer: *a* days. The large mouse digs *b* chi, and the small mouse digs *c* chi.
"""

from fractions import Fraction

# 垣厚五尺
垣厚 = 5

# 大鼠日一尺，小鼠亦日一尺
大鼠初速 = 1
小鼠初速 = 1

# 大鼠日自倍，小鼠日自半
大鼠速率 = [大鼠初速 * (2 ** i) for i in range(10)]  # Example for 10 days
小鼠速率 = [小鼠初速 * (1 / (2 ** i)) for i in range(10)]  # Example for 10 days

# 假令二日，不足五寸
不足 = Fraction(5, 10)  # 5 cun = 5/10 chi
不足日 = 2
不足進度 = sum(大鼠速率[:不足日]) + sum(小鼠速率[:不足日]) - 垣厚

# 令之三日，有餘三尺七寸半
有餘 = Fraction(3 * 10 + 7.5, 10)  # 3 chi 7 cun 5 fen = 3.75 chi
有餘日 = 3
有餘進度 = sum(大鼠速率[:有餘日]) + sum(小鼠速率[:有餘日]) - 垣厚

# 盈不足術
# 置所出率，盈、不足各居其下
盈率 = 有餘日
不足率 = 不足日

# 令維乘所出率，并以為實
實 = (盈率 * abs(不足進度)) + (不足率 * abs(有餘進度))

# 并盈、不足為法
法 = abs(不足進度) + abs(有餘進度)

# 實如法而一
a = Fraction(實, 法)

# 計算各鼠穿的距離
大鼠穿 = sum(大鼠速率[:int(a)])
小鼠穿 = sum(小鼠速率[:int(a)])

b = 大鼠穿
c = 小鼠穿
"""
Code error: both arguments should be Rational instances"""
