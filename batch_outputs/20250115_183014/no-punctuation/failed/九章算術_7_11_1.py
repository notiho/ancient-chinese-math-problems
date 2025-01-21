"""
今有垣厚五尺兩鼠對穿大鼠日一尺小鼠亦日一尺大鼠日自倍小鼠日自半問幾何日相逢各穿幾何
術曰假令二日不足五寸令之三日有餘三尺七寸半
盈不足術曰置所出率盈不足各居其下令維乘所出率并以為實并盈不足為法實如法而一有分者通之盈不足相與同其買物者置所出率以少減多餘以約法實實為物價法為人數荅曰 a日 大鼠穿 b尺 小鼠穿 c尺 
"""

"""
Suppose there is a wall 5 chi thick. Two mice dig through it from opposite sides.
The large mouse digs 1 chi per day, and the small mouse also digs 1 chi per day.
However, the large mouse doubles its daily progress, while the small mouse halves its daily progress.
Question: after how many days do they meet, and how much has each mouse dug?

The procedure says: Suppose 2 days are insufficient by 5 cun. Adjust it to 3 days, which exceeds by 3 chi 7 cun and a half.
Using the "Excess and Deficiency" method:
Place the rates of progress for each case, and place the excess and deficiency below them.
Multiply the rates of progress by their respective excess or deficiency, and sum them to form the dividend.
Sum the excess and deficiency to form the divisor.
Divide the dividend by the divisor to find the number of days. If there is a remainder, convert it to a fraction.
If the excess and deficiency are the same, use the smaller rate of progress to subtract the larger, and simplify the divisor and dividend.
The result gives the number of days. Multiply the number of days by the rates of progress to find the distances dug.

Answer: *a* days, the large mouse digs *b* chi, and the small mouse digs *c* chi.
"""

# 垣厚五尺
垣厚 = 5

# 大鼠日一尺，小鼠亦日一尺
大鼠日進 = 1
小鼠日進 = 1

# 大鼠日自倍，小鼠日自半
大鼠日進倍 = 2 * 大鼠日進
小鼠日進半 = Fraction(1, 2) * 小鼠日進

# 假令二日不足五寸
不足 = Fraction(5, 10)  # 5 cun = 0.5 chi
假二日進 = 2 * 大鼠日進倍 + 2 * 小鼠日進半
不足量 = 垣厚 - 假二日進 - 不足

# 令之三日有餘三尺七寸半
有餘 = 3 + Fraction(7, 10)  # 3 chi 7 cun = 3.7 chi
假三日進 = 3 * 大鼠日進倍 + 3 * 小鼠日進半
有餘量 = 假三日進 - 垣厚 - 有餘

# 盈不足術
# 置所出率盈不足各居其下
大鼠率 = 大鼠日進倍
小鼠率 = 小鼠日進半
盈 = 有餘量
不足 = 不足量

# 令維乘所出率并以為實
實 = (大鼠率 * 盈) + (小鼠率 * 不足)

# 并盈不足為法
法 = 盈 + 不足

# 實如法而一
a = Fraction(實, 法)

# 大鼠穿 b 尺
b = a * 大鼠日進倍

# 小鼠穿 c 尺
c = a * 小鼠日進半
"""
Variable 'a' has wrong value. Expected: 36/17, Actual: 53/34
Variable 'b' has wrong value. Expected: 59/17, Actual: 53/17
Variable 'c' has wrong value. Expected: 26/17, Actual: 53/68"""
