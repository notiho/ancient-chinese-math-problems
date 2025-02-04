"""
今有腰鼓田從八十二步两頭各廣三十步中央廣十二步問為田㡬何
術曰并三廣得七十二步以三除之得二十四步以從八十二步乘之得一千九百六十八步以畝法除之即得
答曰 a畝 奇 b步 
"""

#----- content starts here -----
"""
Suppose there is a waist-drum-shaped field. The length is 82 bu. 
The two ends each have a width of 30 bu, and the middle has a width of 12 bu.
Question: how large is the field?

The procedure says: Add the three widths, obtaining 72 bu. Divide it by 3, obtaining 24 bu.
Multiply it by the length of 82 bu, obtaining 1968 bu.
Divide it by the mu-divisor, 240, to obtain the result.

Answer: *a* mu and *b* bu.
"""

from fractions import Fraction

# 從八十二步
從步數 = 82

# 两頭各廣三十步
廣頭 = 30

# 中央廣十二步
廣中 = 12

# 并三廣得七十二步
總廣 = 廣頭 + 廣頭 + 廣中

# 以三除之得二十四步
平均廣 = Fraction(總廣, 3)

# 以從八十二步乘之得一千九百六十八步
積步 = 平均廣 * 從步數

# 以畝法除之即得
畝法 = 240
畝數 = 積步 // 畝法  # 整數部分為畝
餘步 = 積步 % 畝法   # 餘數為步

a = 畝數
b = 餘步#----- content ends here -----

"""
"""
