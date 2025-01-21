"""
今有垣厚五尺，兩鼠對穿。大鼠日一尺，小鼠亦日一尺。大鼠日自倍，小鼠日自半。問︰幾何日相逢？各穿幾何？
術曰：假令二日，不足五寸。令之三日，有餘三尺七寸半。
盈不足術曰：置所出率，盈、不足各居其下。令維乘所出率，并以為實。并盈、不足為法。實如法而一。有分者，通之。盈不足相與同其買物者，置所出率，以少減多，餘，以約法、實。實為物價，法為人數。荅曰： a(=36/17)日 。大鼠穿 b(=59/17)尺 ，小鼠穿 c(=26/17)尺 。
"""

"""
Suppose there is a wall 5 chi thick, and two mice are digging through it from opposite sides.
The large mouse digs 1 chi per day, and the small mouse also digs 1 chi per day.
However, the large mouse doubles its progress each day, while the small mouse halves its progress each day.
Question: after how many days do they meet? How far does each mouse dig?

The procedure says: Suppose for 2 days, the total progress is less than 5 cun.
Suppose for 3 days, the total progress exceeds 3 chi 7 cun and a half.
The "excess and deficiency" procedure says: Place the rates of progress, with the excess and deficiency below them.
Multiply the rates of progress by their respective excess or deficiency, and sum them to form the dividend.
Sum the excess and deficiency to form the divisor.
Divide the dividend by the divisor to find the number of days.
If there is a fraction, simplify it.
To find the distances dug by each mouse, use their respective rates of progress and multiply by the number of days.

Answer: *a*(=36/17) days. The large mouse digs *b*(=59/17) chi, and the small mouse digs *c*(=26/17) chi.
"""

# 垣厚五尺
垣厚 = 5

# 假令二日，不足五寸
不足 = Fraction(5, 10)  # 5 cun = 0.5 chi
假日1 = 2
大鼠率1 = 1 + 2  # 大鼠日自倍
小鼠率1 = 1 / 2 + 1 / 4  # 小鼠日自半
進度1 = 大鼠率1 + 小鼠率1

# 令之三日，有餘三尺七寸半
有餘 = 3 + Fraction(7, 10) + Fraction(5, 20)  # 3 chi 7 cun 5 fen = 3.75 chi
假日2 = 3
大鼠率2 = 1 + 2 + 4  # 大鼠日自倍
小鼠率2 = 1 / 2 + 1 / 4 + 1 / 8  # 小鼠日自半
進度2 = 大鼠率2 + 小鼠率2

# 盈不足術
盈 = 進度2 - 垣厚  # 有餘
不足 = 垣厚 - 進度1  # 不足
所出率1 = 假日1
所出率2 = 假日2

# 置所出率，盈、不足各居其下
實 = 盈 * 所出率1 + 不足 * 所出率2
法 = 盈 + 不足

# 實如法而一
a = Fraction(實, 法)  # 36/17 days

# 大鼠穿
大鼠穿 = 1 + 2  # 初始進度
倍率 = 1
for i in range(2, int(a) + 2):  # 模擬大鼠進度
    倍率 *= 2
    大鼠穿 += 倍率
"""
Code error: both arguments should be Rational instances"""
