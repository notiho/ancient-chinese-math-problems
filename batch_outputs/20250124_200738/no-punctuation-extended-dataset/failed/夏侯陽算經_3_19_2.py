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

The procedure says: First, place the number of cloth [duan], zhang, chi, and multiply them. 
From below, add 8 to the price, and continue up to the top of the number. 
Subtract one rank, and the result is obtained.

Answer: *a* guan.
"""

# 布數
布端數 = 13463
布丈數 = 2
布尺數 = 5
布寸數 = 6

# 每端直錢一貫八百文
每端價值 = 1 * 1000 + 800  # 1貫 = 1000文

# 計算總布的長度（以寸為單位）
總布寸 = 布端數 * 10 * 10 + 布丈數 * 10 + 布尺數 + 布寸數 / 10

# 計算總價值
總價值文 = 布端數 * 每端價值

# 換算為貫
a = Fraction(總價值文, 1000)  # 1貫 = 1000文#----- content ends here -----

"""
Variable 'a' has wrong value. Expected: 15146451/625, Actual: 121167/5"""
