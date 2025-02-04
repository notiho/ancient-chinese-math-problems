"""
今有四不等田東三十五步西四十五步南二十五步北一十五步問為田㡬何
術曰并東西得八十步半之得四十步又并南北得四十步半之得二十步二位相乘得八百步以畝法除之即得
答曰 a畝 奇 b步 
"""

#----- content starts here -----
"""
Suppose there is an irregular quadrilateral field with the following dimensions:
East: 35 bu, West: 45 bu, South: 25 bu, North: 15 bu.
Question: how large is the field?

The procedure says: Add the east and west sides, obtaining 80 bu. Halve it, obtaining 40 bu.
Then add the south and north sides, obtaining 40 bu. Halve it, obtaining 20 bu.
Multiply these two values, obtaining 800 bu.
Divide by the mu-divisor (240), and the result is the area.

Answer: *a* mu and *b* bu.
"""

# 東三十五步
東 = 35

# 西四十五步
西 = 45

# 南二十五步
南 = 25

# 北一十五步
北 = 15

# 并東西得八十步
東西和 = 東 + 西

# 半之得四十步
東西半 = 東西和 / 2

# 并南北得四十步
南北和 = 南 + 北

# 半之得二十步
南北半 = 南北和 / 2

# 二位相乘得八百步
積步 = 東西半 * 南北半

# 以畝法除之即得
畝法 = 240
畝數 = int(積步 // 畝法)  # 整數部分為畝
餘步 = 積步 % 畝法  # 餘數為步

a = 畝數
b = 餘步#----- content ends here -----

"""
"""
