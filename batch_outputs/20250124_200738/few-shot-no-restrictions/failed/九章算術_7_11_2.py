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
However, the large mouse doubles its progress each day, while the small mouse halves its progress each day. 
Question: After how many days will they meet? How far will each mouse have dug?

The procedure says: Suppose after 2 days, they have not yet reached 5 chi. 
Suppose after 3 days, they exceed 5 chi by 3 chi and 7 cun (3.7 chi). 
Using the method of excess and deficiency: Place the rates of progress, and place the excess and deficiency below them. 
Multiply the rates of progress by the excess and deficiency, and add them to form the dividend. 
Add the excess and deficiency to form the divisor. 
Divide the dividend by the divisor to find the number of days. 
If there is a remainder, simplify it. 
To find how far each mouse has dug, use their rates of progress and multiply by the number of days.

Answer: *a* days. The large mouse digs *b* chi, and the small mouse digs *c* chi.
"""

from fractions import Fraction

# Wall thickness
垣厚 = 5  # chi

# Rates of progress
大鼠日進 = 1  # chi/day
小鼠日進 = 1  # chi/day

# Progress multiplier per day
大鼠倍增 = 2  # Doubles each day
小鼠半減 = Fraction(1, 2)  # Halves each day

# Excess and deficiency
不足 = Fraction(5, 10)  # 5 cun = 0.5 chi
有餘 = 3 + Fraction(7, 10)  # 3 chi 7 cun = 3.7 chi

# Rates of progress after 2 and 3 days
大鼠進度_2日 = 大鼠日進 * (1 + 大鼠倍增)
小鼠進度_2日 = 小鼠日進 * (1 + 小鼠半減)
總進度_2日 = 大鼠進度_2日 + 小鼠進度_2日

大鼠進度_3日 = 大鼠日進 * (1 + 大鼠倍增 + 大鼠倍增**2)
小鼠進度_3日 = 小鼠日進 * (1 + 小鼠半減 + 小鼠半減**2)
總進度_3日 = 大鼠進度_3日 + 小鼠進度_3日

# 盈不足術
實 = (總進度_2日 * 有餘) + (總進度_3日 * 不足)
法 = 有餘 + 不足

# Number of days
a = Fraction(實, 法)

# Distance dug by each mouse
b = 大鼠日進 * (1 + 大鼠倍增 + 大鼠倍增**2) * a
c = 小鼠日進 * (1 + 小鼠半減 + 小鼠半減**2) * a

# Final answer
a_days = float(a)
b_chi = float(b)
c_chi = float(c)

a_days, b_chi, c_chi#----- content ends here -----

"""
Variable 'a' has wrong value. Expected: 36/17, Actual: 841/168
Variable 'b' has wrong value. Expected: 59/17, Actual: 841/24
Variable 'c' has wrong value. Expected: 26/17, Actual: 841/96"""
