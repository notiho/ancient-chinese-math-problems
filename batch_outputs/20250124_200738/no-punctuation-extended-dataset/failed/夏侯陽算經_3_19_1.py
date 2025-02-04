"""
今有布一萬三千四百六十三端二丈五尺六寸毎端直錢一貫八百文問計錢幾何
術曰先置布數丈尺倍之從下八添直至數首退一等即得
答曰 a貫
"""

#----- content starts here -----
"""
Suppose there is cloth measuring 13,463 duan, 2 zhang, 5 chi, and 6 cun. 
Each duan is worth 1 guan and 800 wen.
Question: how much money in total?

The procedure says: First, place the cloth amount in zhang, chi, and multiply it. 
From below, add 8 and extend the value to the top. 
Subtract one rank, and the result is obtained.

Answer: *a* guan.
"""

# 布數
布端 = 13463  # 端
布丈 = 2       # 丈
布尺 = 5       # 尺
布寸 = 6       # 寸

# 每端直錢
每端直錢 = 1 * 1000 + 800  # 1貫 = 1000文, 所以1貫800文 = 1800文

# 將布的長度轉換為總端數
# 1 丈 = 10 尺, 1 尺 = 10 寸
總布長度 = 布端 + Fraction(布丈 * 10 + 布尺 + 布寸 / 10, 10)

# 計算總錢數
總錢數 = 總布長度 * 每端直錢

# 將總錢數轉換為貫
a = Fraction(總錢數, 1000)  # 1貫 = 1000文#----- content ends here -----

"""
Code error: both arguments should be Rational instances"""
