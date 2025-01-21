"""
今有人持錢之洛賈利五之初返歸一萬六千第二返歸一萬七千第三返歸一萬八千第四返歸一萬九千第五返歸二萬凡五返歸本利俱盡問本錢㡬何
術曰置後返歸錢數以五乗之以七乗第四返歸錢數加之以五乗之以四十九乗第三返歸錢數加之以五乗之以三百四十三乗第二返歸錢數加之以五乗之以二千四百一乗初返歸錢數加之以五乗之以一萬六千八百七而一得本錢數一法盈不足術為之亦得
答曰 a錢
"""

"""
Suppose someone invests money in Luoyang with a profit rate of 1/5 (5% per return).
After the first return, they receive 16,000 qian.
After the second return, they receive 17,000 qian.
After the third return, they receive 18,000 qian.
After the fourth return, they receive 19,000 qian.
After the fifth return, they receive 20,000 qian.
In total, they have received all the principal and profit after five returns.
Question: how much was the initial principal?

The procedure says: Place the amount of money from the last return.
Multiply it by 5, then multiply it by 7.
Add the amount of money from the fourth return.
Multiply it by 5, then multiply it by 49.
Add the amount of money from the third return.
Multiply it by 5, then multiply it by 343.
Add the amount of money from the second return.
Multiply it by 5, then multiply it by 2,401.
Add the amount of money from the first return.
Multiply it by 5, then multiply it by 16,807.
Divide by 1, and the result is the initial principal.
Another method for excess or deficiency can also be used.

Answer: *a* qian.
"""

# 第五返歸錢數
第五返歸 = 20000

# 第四返歸錢數
第四返歸 = 19000

# 第三返歸錢數
第三返歸 = 18000

# 第二返歸錢數
第二返歸 = 17000

# 初返歸錢數
初返歸 = 16000

# 置後返歸錢數，以五乘之，以七乘
本錢 = 5 * 7 * 第五返歸

# 加第四返歸錢數，以五乘之，以四十九乘
本錢 += 5 * 49 * 第四返歸

# 加第三返歸錢數，以五乘之，以三百四十三乘
本錢 += 5 * 343 * 第三返歸

# 加第二返歸錢數，以五乘之，以二千四百一乘
本錢 += 5 * 2401 * 第二返歸

# 加初返歸錢數，以五乘之，以一萬六千八百七乘
本錢 += 5 * 16807 * 初返歸

# 而一得本錢數
a = Fraction(本錢, 1)  # Divide by 1 to get the principal amount

"""
Variable 'a' has wrong value. Expected: 593730000/16807, Actual: 1584870000"""
