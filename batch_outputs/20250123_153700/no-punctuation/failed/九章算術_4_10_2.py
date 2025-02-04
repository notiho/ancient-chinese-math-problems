"""
今有田廣一步半三分步之一四分步之一五分步之一六分步之一七分步之一八分步之一九分步之一十分步之一十一分步之一十二分步之一求田一畝問從幾何
術曰下有一十二分以一為八萬三千一百六十半為四萬一千五百八十三分之一為二萬七千七百二十四分之一為二萬七百九十五分之一為一萬六千六百三十二六分之一為一萬三千八百六十七分之一為一萬一千八百八十八分之一為一萬三百九十五九分之一為九千二百四十一十分之一為八千三百一十六十一分之一為七千五百六十十二分之一為六千九百三十并之得二十五萬八千六十三以為法置田二百四十步亦以一為八萬三千一百六十乘之為實實如法得從步
荅曰 a步 
"""

"""
Suppose there is a field with a width of 1 bu, 1/2 bu, 1/3 bu, 1/4 bu, 1/5 bu, 1/6 bu, 1/7 bu, 1/8 bu, 1/9 bu, 1/10 bu, 1/11 bu, and 1/12 bu.
A field of 1 mu is sought.
Question: how large is the length?

The procedure says: Below, there is 1/12. 
Take 1 as 83160, 1/2 as 41583, 1/3 as 27724, 1/4 as 20795, 1/5 as 16632, 1/6 as 13867, 1/7 as 11888, 1/8 as 10395, 1/9 as 9241, 1/10 as 8316, 1/11 as 7560, and 1/12 as 6930.
Add these, obtaining 258063 as the divisor.
Place the field of 240 bu, and also multiply it by taking 1 as 83160, giving the dividend.
Do the division, obtaining the number of steps of the length.

The answer says: *a* bu.
"""

# 廣一步半三分步之一四分步之一五分步之一六分步之一七分步之一八分步之一九分步之一十分步之一十一分步之一十二分步之一
廣 = [
    83160,  # 1
    41583,  # 1/2
    27724,  # 1/3
    20795,  # 1/4
    16632,  # 1/5
    13867,  # 1/6
    11888,  # 1/7
    10395,  # 1/8
    9241,   # 1/9
    8316,   # 1/10
    7560,   # 1/11
    6930    # 1/12
]

# 并之得二十五萬八千六十三，以為法
法 = sum(廣)

# 置田二百四十步
田 = 240

# 亦以一為八萬三千一百六十乘之，為實
實 = 83160 * 田

# 實如法得從步
a = Fraction(實, 法)
"""
Variable 'a' has wrong value. Expected: 6652800/86021, Actual: 19958400/258091"""
