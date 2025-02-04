"""
今有鼓田两頭各廣四十步中央廣五十二步從八十五步。問：為田㡬何？
術曰：并三廣得一百三十二步以三除之得四十四步以從八十五步乘之得三千七百四十步以畝法除之即得。
答曰： a畝 奇 b步 。
"""

#----- content starts here -----
"""
Suppose there is a drum-shaped field (trapezoidal field) where the two ends are each 40 bu wide, the center is 52 bu wide, and the length is 85 bu.
Question: how large is the field?

The procedure says: Add the three widths together, obtaining 132 bu. Divide this by 3, obtaining 44 bu.
Multiply this by the length (85 bu), obtaining 3740 bu².
Divide this by the mu-divisor (240 bu² per mu), obtaining the result.

Answer: *a* mu and *b* bu².
"""

from fractions import Fraction

# Two ends each 40 bu wide
廣1 = 40
廣2 = 40

# Central width 52 bu
中央廣 = 52

# Length 85 bu
從 = 85

# Add the three widths together
三廣 = 廣1 + 廣2 + 中央廣

# Divide by 3 to get the average width
平均廣 = Fraction(三廣, 3)

# Multiply by the length to get the total area in bu²
積步 = 平均廣 * 從

# Mu divisor (240 bu² per mu)
畝法 = 240

# Divide the total area by the mu divisor to get the number of mu
畝數 = 積步 // 畝法

# The remainder is the leftover bu²
剩餘步 = 積步 % 畝法

# Final answer
a = 畝數
b = 剩餘步

print(f"Answer: {a} 畝 and {b} 步².")#----- content ends here -----

"""
"""
