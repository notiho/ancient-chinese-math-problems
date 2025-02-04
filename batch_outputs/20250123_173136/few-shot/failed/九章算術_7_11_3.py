"""
今有垣厚五尺，兩鼠對穿。大鼠日一尺，小鼠亦日一尺。大鼠日自倍，小鼠日自半。問︰幾何日相逢？各穿幾何？
術曰：假令二日，不足五寸。令之三日，有餘三尺七寸半。
盈不足術曰：置所出率，盈、不足各居其下。令維乘所出率，并以為實。并盈、不足為法。實如法而一。有分者，通之。盈不足相與同其買物者，置所出率，以少減多，餘，以約法、實。實為物價，法為人數。
荅曰： a日 。大鼠穿 b尺 ，小鼠穿 c尺 。
"""

"""
Suppose there is a wall 5 chi thick, and two rats are digging through it from opposite sides.
The large rat digs 1 chi per day, and the small rat also digs 1 chi per day.
The large rat doubles its progress each day, while the small rat halves its progress each day.
Question: after how many days will they meet? How much will each rat have dug?

The procedure says: Suppose for 2 days, the progress is less than 5 cun. Suppose for 3 days, the progress exceeds 3 chi 7.5 cun.
The procedure for excess and deficiency says: Place the rates of progress, with the excess and deficiency below them respectively.
Multiply the rates of progress by the respective excess and deficiency, and add them to form the dividend.
Add the excess and deficiency to form the divisor.
Divide the dividend by the divisor to find the result. If there is a fraction, simplify it.
If the excess and deficiency correspond to the same object, place the rates of progress, subtract the smaller from the larger, and simplify the divisor and dividend.
The dividend is the price of the object, and the divisor is the number of people.

Answer: *a* days. The large rat digs *b* chi, and the small rat digs *c* chi.
"""

# 垣厚五尺
垣厚 = 5

# 大鼠日一尺，小鼠亦日一尺
大鼠初速 = 1
小鼠初速 = 1

# 大鼠日自倍，小鼠日自半
大鼠速率 = [大鼠初速 * (2 ** i) for i in range(10)]  # Generate rates for several days
小鼠速率 = [小鼠初速 * (1 / (2 ** i)) for i in range(10)]  # Generate rates for several days

# 假令二日，不足五寸
不足 = Fraction(5, 10)  # 5 cun = 5/10 chi
大鼠二日 = sum(大鼠速率[:2])
小鼠二日 = sum(小鼠速率[:2])
二日進度 = 大鼠二日 + 小鼠二日

# 令之三日，有餘三尺七寸半
有餘 = 3 + Fraction(7, 10)  # 3 chi 7.5 cun = 3 + 7/10 chi
大鼠三日 = sum(大鼠速率[:3])
小鼠三日 = sum(小鼠速率[:3])
三日進度 = 大鼠三日 + 小鼠三日

# 盈不足術
# 置所出率，盈、不足各居其下
盈 = 三日進度 - 垣厚
不足 = 垣厚 - 二日進度

# 令維乘所出率，并以為實
實 = (盈 * 2) + (不足 * 3)

# 并盈、不足為法
法 = 盈 + 不足

# 實如法而一
a = Fraction(實, 法)

# 大鼠穿 b尺，小鼠穿 c尺
大鼠穿 = sum(大鼠速率[:int(a)])
小鼠穿 = sum(小鼠速率[:int(a)])

b = 大鼠穿
c = 小鼠穿
"""
Code error: both arguments should be Rational instances"""
