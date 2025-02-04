"""
今有蛇田頭廣三十三步胷廣五十七步尾廣十八步從九十二步問為田㡬何
術曰并三廣得一百八步以三除之得三十六步以從九十二步乘之得三千三百一十二步以畝法除之即得
答曰 a畝 奇 b步 
"""

#----- content starts here -----
"""
Suppose there is a snake-shaped field. The width at the head is 33 bu, the width at the middle is 57 bu, and the width at the tail is 18 bu. The length is 92 bu.
Question: how large is the field?

The procedure says: Add the three widths, obtaining 108 bu. Divide by 3, obtaining 36 bu. Multiply this by the length, 92 bu, obtaining 3312 bu. Divide by the mu-divisor, 240, to obtain the result.

Answer: *a* mu and *b* bu.
"""

# 頭廣三十三步
頭廣 = 33

# 胷廣五十七步
胷廣 = 57

# 尾廣十八步
尾廣 = 18

# 從九十二步
從步 = 92

# 并三廣得一百八步
總廣 = 頭廣 + 胷廣 + 尾廣

# 以三除之得三十六步
平均廣 = Fraction(總廣, 3)

# 以從九十二步乘之得三千三百一十二步
積步 = 平均廣 * 從步

# 畝法二百四十步
畝法 = 240

# 以畝法除之即得
畝數 = Fraction(積步, 畝法)

# 分離畝數為整數畝和餘步
a = 畝數.numerator // 畝數.denominator  # 整數畝
b = 畝數.numerator % 畝數.denominator  # 餘步#----- content ends here -----

"""
Variable 'b' has wrong value. Expected: 192, Actual: 4"""
