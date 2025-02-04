"""
今有布一萬三千四百六十三端二丈五尺六寸毎端直錢一貫八百文問計錢幾何
術曰先置布數丈尺倍之從下八添直至數首退一等即得
答曰 a貫
"""

#----- content starts here -----
"""
Suppose there is cloth, 13,463 bolts, each bolt being 2 zhang, 5 chi, and 6 cun in length. 
Each bolt is worth 1 guan and 800 wen.
Question: how much money in total?

The procedure says: First, place the number of bolts. Multiply the zhang, chi, and cun by their respective values. 
From below, add 800 wen to the total for each bolt. 
Carry over to the next unit (guan) as needed.

Answer: *a* guan.
"""

# 布數
布數 = 13463

# 每端長度
丈 = 2
尺 = 5
寸 = 6

# 每端價格
每端貫 = 1
每端文 = 800

# 計算總文數
總文數 = 布數 * (每端貫 * 1000 + 每端文)

# 換算為貫
a = Fraction(總文數, 1000)  # 1貫 = 1000文#----- content ends here -----

"""
Variable 'a' has wrong value. Expected: 15146451/625, Actual: 121167/5"""
