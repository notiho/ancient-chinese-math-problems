"""
今有布一萬三千四百六十三端二丈五尺六寸毎端直錢一貫八百文問計錢幾何
術曰先置布數丈尺倍之從下八添直至數首退一等即得
答曰 a貫
"""

#----- content starts here -----
"""
Suppose there is cloth totaling 13,463 bolts, each bolt being 2 zhang, 5 chi, and 6 cun in length.
Each bolt is worth 1 guan and 800 wen.
Question: how much money is the total worth?

The procedure says: First, place the number of bolts.
Multiply the zhang, chi, and cun by their respective values.
From below, add 800 wen to the total value of 1 guan for each bolt.
Proceed to calculate the total value.

Answer: *a* guan.
"""

# 布數
布數 = 13463

# 每端直錢一貫八百文
每端直錢 = 1 * 1000 + 800  # 1貫 = 1000文

# 計算總錢數
總錢數 = 布數 * 每端直錢

# 換算為貫
a = Fraction(總錢數, 1000)  # 1貫 = 1000文#----- content ends here -----

"""
Variable 'a' has wrong value. Expected: 15146451/625, Actual: 121167/5"""
