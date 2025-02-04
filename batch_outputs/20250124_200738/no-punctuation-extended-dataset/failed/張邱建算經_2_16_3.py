"""
今有人持錢之洛賈利五之初返歸一萬六千第二返歸一萬七千第三返歸一萬八千第四返歸一萬九千第五返歸二萬凡五返歸本利俱盡問本錢㡬何
術曰置後返歸錢數以五乗之以七乗第四返歸錢數加之以五乗之以四十九乗第三返歸錢數加之以五乗之以三百四十三乗第二返歸錢數加之以五乗之以二千四百一乗初返歸錢數加之以五乗之以一萬六千八百七而一得本錢數一法盈不足術為之亦得
答曰 a錢
"""

#----- content starts here -----
"""
Suppose someone invests money in Luoyang, with a profit rate of 5 per return. 
After the first return, they receive 16,000. 
After the second return, they receive 17,000. 
After the third return, they receive 18,000. 
After the fourth return, they receive 19,000. 
After the fifth return, they receive 20,000. 
In total, after five returns, the principal and profit are fully repaid.
Question: how much was the initial principal?

The procedure says: 
Place the amount of money from the last return (fifth return) and multiply it by 5.
Then multiply it by 7 and add the amount from the fourth return.
Multiply the result by 5 and then by 49, and add the amount from the third return.
Multiply the result by 5 and then by 343, and add the amount from the second return.
Multiply the result by 5 and then by 2,401, and add the amount from the first return.
Multiply the result by 5 and then by 16,807, and divide by 1 to obtain the principal amount.
Another method using surplus and deficit calculations can also be used.

Answer: the principal is *a* qian.
"""

# 利率
利率 = 5

# 各次返歸錢數
第五返歸 = 20000
第四返歸 = 19000
第三返歸 = 18000
第二返歸 = 17000
第一返歸 = 16000

# 置後返歸錢數，以五乘之
本錢 = 第五返歸 * 利率

# 以七乘，第四返歸錢數加之
本錢 = 本錢 * 7 + 第四返歸

# 以五乘之，以四十九乘，第三返歸錢數加之
本錢 = 本錢 * 利率 * 49 + 第三返歸

# 以五乘之，以三百四十三乘，第二返歸錢數加之
本錢 = 本錢 * 利率 * 343 + 第二返歸

# 以五乘之，以二千四百一乘，初返歸錢數加之
本錢 = 本錢 * 利率 * 2401 + 第一返歸

# 以五乘之，以一萬六千八百七乘，而一得本錢數
本錢 = Fraction(本錢 * 利率 * 16807, 1)

a = 本錢#----- content ends here -----

"""
Variable 'a' has wrong value. Expected: 593730000/16807, Actual: 304807653409349160000"""
