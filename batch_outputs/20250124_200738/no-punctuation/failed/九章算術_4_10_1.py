"""
今有田廣一步半三分步之一四分步之一五分步之一六分步之一七分步之一八分步之一九分步之一十分步之一十一分步之一十二分步之一求田一畝問從幾何
術曰下有一十二分以一為八萬三千一百六十半為四萬一千五百八十三分之一為二萬七千七百二十四分之一為二萬七百九十五分之一為一萬六千六百三十二六分之一為一萬三千八百六十七分之一為一萬一千八百八十八分之一為一萬三百九十五九分之一為九千二百四十一十分之一為八千三百一十六十一分之一為七千五百六十十二分之一為六千九百三十并之得二十五萬八千六十三以為法置田二百四十步亦以一為八萬三千一百六十乘之為實實如法得從步
荅曰 a步 
"""

#----- content starts here -----
"""
Suppose there is a field with a width of 1 bu, 1/2 bu, 1/3 bu, 1/4 bu, 1/5 bu, 1/6 bu, 1/7 bu, 1/8 bu, 1/9 bu, 1/10 bu, 1/11 bu, and 1/12 bu.
A field of 1 mu is sought.
Question: how large is the length?

The procedure says: Below, there is 1/12. Take 1 as 83160, 1/2 as 41583, 1/3 as 27724, 1/4 as 20795, 1/5 as 16632, 1/6 as 13867, 1/7 as 11888, 1/8 as 10395, 1/9 as 9241, 1/10 as 8316, 1/11 as 7560, and 1/12 as 6930.
Add these, obtaining 258063 as the divisor.
Place the field of 240 bu, and also multiply it by taking 1 as 83160, giving the dividend.
Do the division, obtaining the number of steps of the length.

The answer says: *a* bu.
"""

# 廣一步半三分步之一四分步之一五分步之一六分步之一七分步之一八分步之一九分步之一十分步之一十一分步之一十二分步之一
廣 = Fraction(1, 1) + Fraction(1, 2) + Fraction(1, 3) + Fraction(1, 4) + Fraction(1, 5) + Fraction(1, 6) + Fraction(1, 7) + Fraction(1, 8) + Fraction(1, 9) + Fraction(1, 10) + Fraction(1, 11) + Fraction(1, 12)

# 以一為八萬三千一百六十，半為四萬一千五百八十三，分之一為二萬七千七百二十四，依次類推
一 = 83160
半 = 41583
三分之一 = 27724
四分之一 = 20795
五分之一 = 16632
六分之一 = 13867
七分之一 = 11888
八分之一 = 10395
九分之一 = 9241
十分之一 = 8316
十一分之一 = 7560
十二分之一 = 6930

# 并之得二十五萬八千六十三，以為法
法 = 一 + 半 + 三分之一 + 四分之一 + 五分之一 + 六分之一 + 七分之一 + 八分之一 + 九分之一 + 十分之一 + 十一分之一 + 十二分之一

# 置田二百四十步
田 = 240

# 亦以一為八萬三千一百六十，乘之為實
實 = 田 * 一

# 實如法得從步
a = Fraction(實, 法)#----- content ends here -----

"""
Variable 'a' has wrong value. Expected: 6652800/86021, Actual: 19958400/258091"""
