"""
今有垣厚五尺兩鼠對穿大鼠日一尺小鼠亦日一尺大鼠日自倍小鼠日自半問幾何日相逢各穿幾何
術曰假令二日不足五寸令之三日有餘三尺七寸半
盈不足術曰置所出率盈不足各居其下令維乘所出率并以為實并盈不足為法實如法而一有分者通之盈不足相與同其買物者置所出率以少減多餘以約法實實為物價法為人數
荅曰 a日 大鼠穿 b尺 小鼠穿 c尺 
"""

"""
Suppose there is a wall 5 chi thick. Two mice are digging through it from opposite sides.
The large mouse digs 1 chi per day, and the small mouse also digs 1 chi per day.
However, the large mouse's daily progress doubles itself, while the small mouse's daily progress halves itself.
Question: after how many days do they meet, and how much has each mouse dug?

The procedure says: Suppose 2 days are insufficient by 5 cun. Let it be 3 days, which exceeds by 3 chi 7 cun and a half.
Using the "Excess and Deficit" procedure: Place the rates of progress, the excess, and the deficit below each other.
Multiply the rates of progress by their respective excess or deficit, and sum them to form the dividend.
Sum the excess and deficit to form the divisor.
Divide the dividend by the divisor to find the number of days. If there is a remainder, convert it to a fraction.
If the excess and deficit are the same, place the rates of progress, subtract the smaller from the larger, and reduce the divisor and dividend proportionally.
The dividend becomes the price of the goods, and the divisor becomes the number of people.

Answer: *a* days, the large mouse digs *b* chi, and the small mouse digs *c* chi.
"""

# 垣厚五尺
垣厚 = 5

# 大鼠日自倍，小鼠日自半
大鼠日率 = 2
小鼠日率 = Fraction(1, 2)

# 假令二日不足五寸 (2 days deficit of 5 cun)
不足 = Fraction(5, 10)  # Convert 5 cun to chi

# 令之三日有餘三尺七寸半 (3 days excess of 3 chi 7.5 cun)
有餘 = 3 + Fraction(7.5, 10)  # Convert 7.5 cun to chi

# 盈不足術
# 置所出率盈不足各居其下
大鼠所出率 = 2 * 2  # Large mouse's rate for 2 days
小鼠所出率 = 3 * Fraction(1, 2)  # Small mouse's rate for 3 days

# 令維乘所出率并以為實
實 = (大鼠所出率 * 有餘) + (小鼠所出率 * 不足)

# 并盈不足為法
法 = 有餘 + 不足

# 實如法而一
a = Fraction(實, 法)  # Days until they meet

# 大鼠穿 b 尺
b = a * 大鼠日率

# 小鼠穿 c 尺
c = a * 小鼠日率
"""
Code error: both arguments should be Rational instances"""
