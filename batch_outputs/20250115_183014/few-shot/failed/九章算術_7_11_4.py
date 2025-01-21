"""
今有垣厚五尺，兩鼠對穿。大鼠日一尺，小鼠亦日一尺。大鼠日自倍，小鼠日自半。問︰幾何日相逢？各穿幾何？
術曰：假令二日，不足五寸。令之三日，有餘三尺七寸半。
盈不足術曰：置所出率，盈、不足各居其下。令維乘所出率，并以為實。并盈、不足為法。實如法而一。有分者，通之。盈不足相與同其買物者，置所出率，以少減多，餘，以約法、實。實為物價，法為人數。荅曰： a日 。大鼠穿 b尺 ，小鼠穿 c尺 。
"""

"""
Suppose there is a wall 5 chi thick, and two mice are digging through it from opposite sides.
The large mouse digs 1 chi per day, and the small mouse also digs 1 chi per day.
However, the large mouse doubles its daily progress each day, while the small mouse halves its daily progress each day.
Question: after how many days do they meet? How much has each mouse dug?

The procedure says: Suppose for 2 days, the total progress is less than 5 cun. Suppose for 3 days, the total progress exceeds 3 chi and 7.5 cun.
The "excess and deficiency" procedure says: Place the rates of progress, and place the excess and deficiency below them respectively.
Multiply the rates of progress by their respective days, and add them together to form the dividend.
Add the excess and deficiency together to form the divisor.
Divide the dividend by the divisor to find the number of days. If there is a remainder, adjust it accordingly.
For the total progress of each mouse, use their respective rates of progress to calculate their contributions.

Answer: *a* days. The large mouse digs *b* chi, and the small mouse digs *c* chi.
"""

from fractions import Fraction

# 垣厚五尺
垣厚 = 5

# 大鼠日一尺，小鼠亦日一尺
大鼠初速 = 1
小鼠初速 = 1

# 大鼠日自倍，小鼠日自半
大鼠速率 = [大鼠初速 * (2**i) for i in range(10)]  # Precompute rates for 10 days
小鼠速率 = [小鼠初速 * (1 / (2**i)) for i in range(10)]  # Precompute rates for 10 days

# 假令二日，不足五寸
不足 = Fraction(5, 10)  # 5 cun = 0.5 chi
大鼠二日 = 大鼠速率[0] + 大鼠速率[1]
小鼠二日 = 小鼠速率[0] + 小鼠速率[1]
總二日 = 大鼠二日 + 小鼠二日

# 令之三日，有餘三尺七寸半
餘 = 3 + Fraction(7.5, 10)  # 3 chi 7.5 cun = 3.75 chi
大鼠三日 = 大鼠速率[0] + 大鼠速率[1] + 大鼠速率[2]
小鼠三日 = 小鼠速率[0] + 小鼠速率[1] + 小鼠速率[2]
總三日 = 大鼠三日 + 小鼠三日

# 盈不足術
# 置所出率，盈、不足各居其下
盈 = 總三日 - 垣厚
不足 = 垣厚 - 總二日

# 令維乘所出率，并以為實
實 = (盈 * 2) + (不足 * 3)

# 并盈、不足為法
法 = 盈 + 不足

# 實如法而一
a = Fraction(實, 法)

# 計算各鼠穿過的距離
大鼠穿 = sum(大鼠速率[i] for i in range(int(a)))
小鼠穿 = sum(小鼠速率[i] for i in range(int(a)))

b = 大鼠穿
c = 小鼠穿
"""
Code error: both arguments should be Rational instances"""
