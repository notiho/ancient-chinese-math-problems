"""
今有腰鼓田從八十二步两頭各廣三十步中央廣十二步問為田㡬何
術曰并三廣得七十二步以三除之得二十四步以從八十二步乘之得一千九百六十八步以畝法除之即得
答曰 a畝 奇 b步 
"""

#----- content starts here -----
"""
Suppose there is a waist-drum-shaped field. The length is 82 bu. 
The two ends are each 30 bu wide, and the middle is 12 bu wide.
Question: how large is the field?

The procedure says: Add the three widths, obtaining 72 bu. Divide by 3, obtaining 24 bu.
Multiply this by the length of 82 bu, obtaining 1968 bu.
Divide this by the mu-divisor, 240, to obtain the result.

Answer: *a* mu and *b* bu.
"""

# 從八十二步
從步數 = 82

# 两頭各廣三十步
兩頭廣 = 30

# 中央廣十二步
中央廣 = 12

# 并三廣得七十二步
總廣 = 兩頭廣 + 兩頭廣 + 中央廣

# 以三除之得二十四步
平均廣 = 總廣 // 3

# 以從八十二步乘之得一千九百六十八步
積步 = 平均廣 * 從步數

# 畝法二百四十步
畝法 = 240

# 以畝法除之即得
畝數 = 積步 // 畝法
餘步 = 積步 % 畝法

a = 畝數
b = 餘步#----- content ends here -----

"""
"""
