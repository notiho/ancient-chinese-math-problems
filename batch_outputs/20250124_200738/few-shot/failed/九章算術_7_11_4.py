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
Question: after how many days do they meet? How much does each mouse dig?

The procedure says: Suppose for 2 days, the total progress is less than 5 cun. Suppose for 3 days, the total progress exceeds 3 chi and 7.5 cun.
The "excess and deficiency" procedure says: Place the rates of progress, and put the excess and deficiency below them respectively.
Multiply the rates of progress by their respective days, and add them together to form the dividend.
Add the excess and deficiency together to form the divisor.
Divide the dividend by the divisor to find the number of days. If there is a remainder, adjust it accordingly.
For the total progress of both mice, place their rates of progress, subtract the smaller from the larger, and simplify the divisor and dividend.
The dividend represents the total progress, and the divisor represents the number of days.

Answer: *a* days. The large mouse digs *b* chi, and the small mouse digs *c* chi.
"""

# 垣厚五尺
垣厚 = 5

# 大鼠日一尺，小鼠亦日一尺
大鼠初速 = 1
小鼠初速 = 1

# 大鼠日自倍，小鼠日自半
大鼠速率 = [大鼠初速 * (2 ** i) for i in range(10)]  # Generate rates for 10 days
小鼠速率 = [小鼠初速 * (1 / (2 ** i)) for i in range(10)]  # Generate rates for 10 days

# 假令二日，不足五寸
不足 = Fraction(5, 10)  # 5 cun = 0.5 chi

# 令之三日，有餘三尺七寸半
有餘 = 3 + Fraction(7.5, 10)  # 3 chi and 7.5 cun = 3.75 chi

# 盈不足術
# 置所出率，盈、不足各居其下
盈日 = 3
不足日 = 2

盈速率 = sum(大鼠速率[:盈日]) + sum(小鼠速率[:盈日])
不足速率 = sum(大鼠速率[:不足日]) + sum(小鼠速率[:不足日])

# 令維乘所出率，并以為實
實 = (盈速率 * 不足) + (不足速率 * 有餘)

# 并盈、不足為法
法 = 有餘 + 不足

# 實如法而一
a = Fraction(實, 法)

# 計算各鼠穿多少
大鼠穿 = sum(大鼠速率[:int(a)])
小鼠穿 = sum(小鼠速率[:int(a)])

b = 大鼠穿
c = 小鼠穿#----- content ends here -----

"""
Code error: both arguments should be Rational instances"""
