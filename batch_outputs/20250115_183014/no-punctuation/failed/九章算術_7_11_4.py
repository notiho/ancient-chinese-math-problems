"""
今有垣厚五尺兩鼠對穿大鼠日一尺小鼠亦日一尺大鼠日自倍小鼠日自半問幾何日相逢各穿幾何
術曰假令二日不足五寸令之三日有餘三尺七寸半
盈不足術曰置所出率盈不足各居其下令維乘所出率并以為實并盈不足為法實如法而一有分者通之盈不足相與同其買物者置所出率以少減多餘以約法實實為物價法為人數荅曰 a日 大鼠穿 b尺 小鼠穿 c尺 
"""

"""
Suppose there is a wall 5 chi thick. Two mice are digging through it from opposite sides.
The large mouse digs 1 chi per day, and the small mouse also digs 1 chi per day.
However, the large mouse doubles its daily progress each day, while the small mouse halves its daily progress each day.
Question: after how many days do they meet, and how far has each mouse dug?

The procedure says: Suppose 2 days are insufficient by 5 cun. Adjust it to 3 days, which exceeds by 3 chi 7 cun and a half.
Using the "Excess and Deficiency" method:
Place the rates of progress for each case under the respective excess and deficiency.
Multiply the rates of progress by the respective excess and deficiency, and sum them to form the dividend.
Sum the excess and deficiency to form the divisor.
Divide the dividend by the divisor to find the number of days. If there is a remainder, adjust it.
If the excess and deficiency are consistent, place the rates of progress, subtract the smaller from the larger, and simplify the divisor and dividend.
The dividend represents the total progress, and the divisor represents the number of days.

Answer: *a* days, the large mouse digs *b* chi, and the small mouse digs *c* chi.
"""

# 垣厚五尺
垣厚 = 5

# 大鼠日自倍，小鼠日自半
大鼠初速 = 1
小鼠初速 = 1

# 假令二日不足五寸
不足 = Fraction(5, 10)

# 令之三日有餘三尺七寸半
有餘 = 3 + Fraction(7, 10) + Fraction(5, 20)

# 盈不足術
# 置所出率盈不足各居其下
大鼠速率 = 2  # 大鼠速度倍增
小鼠速率 = 1.5  # 小鼠速度減半

# 令維乘所出率并以為實
實 = (大鼠速率 * 有餘) + (小鼠速率 * 不足)

# 并盈不足為法
法 = 有餘 + 不足

# 實如法而一
a = Fraction(實, 法)

# 大鼠穿 b 尺
b = 大鼠初速 * a

# 小鼠穿 c 尺
c = 小鼠初速 * a
"""
Code error: both arguments should be Rational instances"""
