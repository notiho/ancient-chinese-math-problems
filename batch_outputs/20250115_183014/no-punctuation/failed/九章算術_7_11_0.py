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

The procedure says:
1. Assume 2 days are insufficient by 5 cun (0.5 chi). Assume 3 days exceed by 3 chi 7 cun 5 fen (3.75 chi).
2. Use the "Excess and Deficiency" method:
   - Place the rates of progress for each assumption (2 days and 3 days) below the respective deficiencies and excesses.
   - Multiply the rates of progress by the deficiencies and excesses, and sum them to form the dividend.
   - Sum the deficiencies and excesses to form the divisor.
   - Divide the dividend by the divisor to find the number of days (a). If there is a remainder, convert it to fractions.
3. To find how much each mouse has dug:
   - Multiply the number of days by the respective rates of progress for the large and small mice.

Answer: *a* days, the large mouse digs *b* chi, and the small mouse digs *c* chi.
"""

# 垣厚五尺
垣厚 = 5

# 大鼠日自倍，小鼠日自半
大鼠日進 = 1
小鼠日進 = 1

# 假令二日不足五寸 (0.5 尺)
假令_2日 = 2
不足 = Fraction(5, 10)  # 5 寸 = 0.5 尺

# 假令三日有餘三尺七寸半 (3.75 尺)
假令_3日 = 3
有餘 = Fraction(3 * 10 + 7.5, 10)  # 3 尺 7 寸半 = 3.75 尺

# 盈不足術
# 置所出率盈不足各居其下
所出率_2日 = 假令_2日
所出率_3日 = 假令_3日

盈不足_乘積_2日 = 所出率_2日 * 有餘
盈不足_乘積_3日 = 所出率_3日 * 不足

# 令維乘所出率并以為實
實 = 盈不足_乘積_2日 + 盈不足_乘積_3日

# 并盈不足為法
法 = 有餘 + 不足

# 實如法而一
a = Fraction(實, 法)  # 相逢所需天數

# 大鼠穿 b 尺，小鼠穿 c 尺
b = a * 大鼠日進  # 大鼠穿的距離
c = a * 小鼠日進  # 小鼠穿的距離
"""
Code error: both arguments should be Rational instances"""
