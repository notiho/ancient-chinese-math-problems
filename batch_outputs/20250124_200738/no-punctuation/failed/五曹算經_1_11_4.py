"""
今有邱田周六百四十步徑三百八十步問為田㡬何
術曰列周六百四十步半之得三百二十步又列徑三百八十步半之得一百九十步二位相乘得六萬八百步以畝法除之即得
答曰 a頃 奇 b步 
"""

#----- content starts here -----
"""
Suppose there is a mound-shaped field with a circumference of 640 bu and a diameter of 380 bu.
Question: how large is the field?

The procedure says: Take the circumference of 640 bu, halve it, obtaining 320 bu.
Then take the diameter of 380 bu, halve it, obtaining 190 bu.
Multiply the two results, obtaining 60800 bu.
Divide this by the mu-divisor (240 bu), and the result is the field size.

Answer: *a* qing and *b* bu.
"""

from fractions import Fraction

# 周六百四十步
周 = 640

# 徑三百八十步
徑 = 380

# 半之得三百二十步 (for 周)
周半 = Fraction(周, 2)

# 半之得一百九十步 (for 徑)
徑半 = Fraction(徑, 2)

# 二位相乘得六萬八百步
積步 = 周半 * 徑半

# 畝法二百四十步
畝法 = 240

# 以畝法除之即得
畝數 = Fraction(積步, 畝法)

# 百畝為一頃
頃 = 畝數 // 100
奇步 = 畝數 % 100

a = int(頃)
b = 奇步
#----- content ends here -----

"""
Variable 'a' has wrong value. Expected: 253/100, Actual: 2
Variable 'b' has wrong value. Expected: 80, Actual: 160/3"""
