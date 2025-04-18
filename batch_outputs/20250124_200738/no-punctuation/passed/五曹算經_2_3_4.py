"""
今有兵三千八百三十七人人給錢五百五十六文問計㡬何
術曰列兵三千八百三十七人以五百五十六文乘之即得
答曰 a貫 
"""

#----- content starts here -----
"""
Suppose there are 3837 soldiers, and each is given 556 wen.
Question: what is the total amount?

The procedure says: List the 3837 soldiers. Multiply it by 556 wen, and you will obtain the total.
Convert the total into guan (1 guan = 1000 wen).

Answer: *a* guan.
"""

# 兵三千八百三十七人
兵 = 3837

# 每人給錢五百五十六文
每人錢 = 556

# 以五百五十六文乘之，即得總文數
總文數 = 兵 * 每人錢

# 1貫 = 1000文，將總文數轉為貫
a = Fraction(總文數, 1000)#----- content ends here -----

"""
"""
