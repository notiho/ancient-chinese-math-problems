"""
今有方田桑生中央從角至桑一百四十七步問為田幾何
術曰置角至桑一百四十七步倍之得二百九十四步以五乘之得一千四百七十步以七除之得二百一十步自相乘得四萬四千一百步以二百四十步除之即得
答曰 a頃 奇 b步 
"""

"""
Suppose there is a square field with a mulberry tree growing at its center.
From one corner to the mulberry tree, the distance is 147 bu.
Question: how large is the field?

The procedure says: Place the distance from the corner to the mulberry tree, 147 bu.
Double it, obtaining 294 bu.
Multiply it by 5, obtaining 1470 bu.
Divide it by 7, obtaining 210 bu.
Square this, obtaining 44100 bu.
Divide it by 240 bu, obtaining the area in mu.
100 mu make 1 qing.

The answer says: *a* qing and *b* bu.
"""

from fractions import Fraction

# 置角至桑一百四十七步
角至桑 = 147

# 倍之得二百九十四步
倍步 = 2 * 角至桑

# 以五乘之得一千四百七十步
乘五步 = 5 * 倍步

# 以七除之得二百一十步
田邊長 = Fraction(乘五步, 7)

# 自相乘得四萬四千一百步
田積步 = 田邊長 * 田邊長

# 以二百四十步除之即得
畝數 = Fraction(田積步, 240)

# 將畝數轉換為頃與奇步
a = 畝數 // 100  # 頃數
b = 畝數 % 100   # 奇步數
"""
Variable 'a' has wrong value. Expected: 183/100, Actual: 1
Variable 'b' has wrong value. Expected: 180, Actual: 335/4"""
