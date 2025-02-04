"""
今有人持錢之洛賈利五之初返歸一萬六千第二返歸一萬七千第三返歸一萬八千第四返歸一萬九千第五返歸二萬凡五返歸本利俱盡問本錢㡬何
術曰置後返歸錢數以五乗之以七乗第四返歸錢數加之以五乗之以四十九乗第三返歸錢數加之以五乗之以三百四十三乗第二返歸錢數加之以五乗之以二千四百一乗初返歸錢數加之以五乗之以一萬六千八百七而一得本錢數一法盈不足術為之亦得
答曰 a錢
"""

#----- content starts here -----
"""
Suppose someone invests money in Luoyang with an interest rate of 5%. 
At the end of the first period, they return with 16,000. 
At the end of the second period, they return with 17,000. 
At the end of the third period, they return with 18,000. 
At the end of the fourth period, they return with 19,000. 
At the end of the fifth period, they return with 20,000. 
In total, they return five times, with both principal and interest fully repaid.
Question: how much was the original principal?

The procedure says: Place the amount of money returned in the last period and multiply it by 5. 
Then multiply it by 7 and add the amount of money returned in the fourth period. 
Multiply the result by 5 and then multiply it by 49, adding the amount of money returned in the third period. 
Multiply the result by 5 and then multiply it by 343, adding the amount of money returned in the second period. 
Multiply the result by 5 and then multiply it by 2,401, adding the amount of money returned in the first period. 
Multiply the result by 5 and then multiply it by 16,807. 
Divide by 1 to obtain the principal amount.

The answer says: *a* qian.
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

# 置後返歸錢數，以五乘之
結果 = 5 * 第五返歸

# 以七乘，第四返歸錢數加之
結果 = 7 * 結果 + 第四返歸

# 以五乘之，以四十九乘，第三返歸錢數加之
結果 = 5 * 結果 * 49 + 第三返歸

# 以五乘之，以三百四十三乘，第二返歸錢數加之
結果 = 5 * 結果 * 343 + 第二返歸

# 以五乘之，以二千四百一乘，初返歸錢數加之
結果 = 5 * 結果 * 2401 + 初返歸

# 以五乘之，以一萬六千八百七乘
結果 = 5 * 結果 * 16807

# 而一得本錢數
a = 結果  # The principal amount#----- content ends here -----

"""
Variable 'a' has wrong value. Expected: 593730000/16807, Actual: 304807653409349160000"""
