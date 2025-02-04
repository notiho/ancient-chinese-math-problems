"""
今有垣厚五尺兩鼠對穿大鼠日一尺小鼠亦日一尺大鼠日自倍小鼠日自半問幾何日相逢各穿幾何
術曰假令二日不足五寸令之三日有餘三尺七寸半
盈不足術曰置所出率盈不足各居其下令維乘所出率并以為實并盈不足為法實如法而一有分者通之盈不足相與同其買物者置所出率以少減多餘以約法實實為物價法為人數
荅曰 a日 大鼠穿 b尺 小鼠穿 c尺 
"""

"""
Suppose there is a wall 5 chi thick. Two mice dig through it from opposite sides.
The large mouse digs 1 chi per day, and the small mouse also digs 1 chi per day.
The large mouse doubles its daily progress, while the small mouse halves its daily progress.
Question: after how many days do they meet, and how much has each mouse dug?

The procedure says: Suppose 2 days are insufficient by 5 cun. Then suppose 3 days exceed by 3 chi 7 cun and a half.
The "Excess and Deficit" procedure says: Place the rates of progress, and the excess and deficit, each below their respective terms.
Multiply the rates of progress by their respective terms, and sum them to form the dividend.
Sum the excess and deficit to form the divisor.
Divide the dividend by the divisor, and if there is a remainder, simplify it.
If the excess and deficit are equal, the result is the number of days.
To find how much each mouse digs, place the rates of progress, subtract the smaller from the larger, and simplify the result.

Answer: *a* days, the large mouse digs *b* chi, and the small mouse digs *c* chi.
"""

# 垣厚五尺
垣厚 = 5

# 大鼠日自倍，小鼠日自半
大鼠初速 = 1
小鼠初速 = 1
大鼠日速 = 2 * 大鼠初速
小鼠日速 = Fraction(1, 2) * 小鼠初速

# 假令二日不足五寸
不足 = Fraction(5, 10)  # 5 cun = 0.5 chi
二日進度 = 2 * (大鼠日速 + 小鼠日速)
不足差 = 垣厚 - 二日進度

# 令之三日有餘三尺七寸半
有餘 = 3 + Fraction(7, 10) + Fraction(5, 20)  # 3 chi 7 cun 5 fen = 3.75 chi
三日進度 = 3 * (大鼠日速 + 小鼠日速)
有餘差 = 三日進度 - 垣厚

# 盈不足術
# 置所出率盈不足各居其下
盈不足 = 不足差 + 有餘差
所出率 = (2 * 有餘差) + (3 * 不足差)

# 實如法而一
a = Fraction(所出率, 盈不足)

# 大鼠穿
b = a * 大鼠日速

# 小鼠穿
c = a * 小鼠日速
"""
Variable 'a' has wrong value. Expected: 36/17, Actual: 2
Variable 'b' has wrong value. Expected: 59/17, Actual: 4
Variable 'c' has wrong value. Expected: 26/17, Actual: 1"""
