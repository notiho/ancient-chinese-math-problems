"""
今有布一萬三千四百六十三端二丈五尺六寸毎端直錢一貫八百文問計錢幾何
術曰先置布數丈尺倍之從下八添直至數首退一等即得
答曰 a貫
"""

#----- content starts here -----
"""
Suppose there is cloth totaling 13,463 duan, 2 zhang, 5 chi, and 6 cun. 
Each duan is worth 1 guan and 800 wen.
Question: how much money is the total worth?

The procedure says: First, place the number of cloth (in duan), zhang, and chi.
Double the zhang and chi from below.
Add the value (in wen) to the topmost number.
Subtract one rank (unit) from the topmost number.
This gives the total.

Answer: *a* guan.
"""

# 布數
布端數 = 13463
布丈數 = 2
布尺數 = 5
布寸數 = 6

# 每端直錢一貫八百文
每端直錢 = 1 * 1000 + 800  # 1貫 = 1000文

# 將布丈數與布尺數倍之
布丈數 = 2 * 布丈數
布尺數 = 2 * 布尺數

# 計算總文數
總文數 = 布端數 * 每端直錢

# 換算為貫
a = Fraction(總文數, 1000)  # 1貫 = 1000文#----- content ends here -----

"""
Variable 'a' has wrong value. Expected: 15146451/625, Actual: 121167/5"""
