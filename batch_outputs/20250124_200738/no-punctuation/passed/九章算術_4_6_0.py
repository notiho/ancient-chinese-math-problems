"""
今有田廣一步半三分步之一四分步之一五分步之一六分步之一七分步之一八分步之一求田一畝問從幾何
術曰下有八分以一為八百四十半為四百二十三分之一為二百八十四分之一為二百一十五分之一為一百六十八六分之一為一百四十七分之一為一百二十八分之一為一百五并之得二千二百八十三以為法置田二百四十步亦以一為八百四十乘之為實實如法得從步
荅曰 a步 
"""

#----- content starts here -----
"""
Suppose there is a field with a width of 1 bu, 1/2 bu, 1/3 bu, 1/4 bu, 1/5 bu, 1/6 bu, 1/7 bu, and 1/8 bu.
A field of 1 mu is sought.
Question: how large is the length?

The procedure says: Below, there is 1/8. Take 1 as 840, 1/2 as 420, 1/3 as 280, 1/4 as 210, 1/5 as 168, 1/6 as 140, 1/7 as 120, and 1/8 as 105.
Add these, obtaining 2283 as the divisor.
Place the field of 240 bu, and also multiply it by taking 1 as 840, giving the dividend.
Do the division, obtaining the number of steps of the length.

The answer says: *a* bu.
"""

# 廣一步半三分步之一四分步之一五分步之一六分步之一七分步之一八分步之一
廣 = [
    1,  # 1 bu
    Fraction(1, 2),  # 1/2 bu
    Fraction(1, 3),  # 1/3 bu
    Fraction(1, 4),  # 1/4 bu
    Fraction(1, 5),  # 1/5 bu
    Fraction(1, 6),  # 1/6 bu
    Fraction(1, 7),  # 1/7 bu
    Fraction(1, 8),  # 1/8 bu
]

# 以一為八百四十
基準 = 840

# 計算每部分的權重
權重 = [基準 * x for x in 廣]

# 并之得二千二百八十三，以為法
法 = sum(權重)

# 置田二百四十步
田 = 240

# 亦以一為八百四十乘之，為實
實 = 田 * 基準

# 實如法得從步
a = Fraction(實, 法)#----- content ends here -----

"""
"""
