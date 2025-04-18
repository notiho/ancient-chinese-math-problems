"""
今有圓田周七十八步徑二十六步問為田㡬何
術曰先列周七十八步半之得三十九步又列徑二十六步半之得一十三步二位相乘得五百七步以畝法除之即得
答曰 a畝 奇 b步 
"""

#----- content starts here -----
"""
Suppose there is a circular field with a circumference of 78 bu and a diameter of 26 bu.
Question: how large is the field?

The procedure says: First, take the circumference of 78 bu and halve it, obtaining 39 bu.
Then, take the diameter of 26 bu and halve it, obtaining 13 bu.
Multiply these two values, obtaining 507 bu.
Divide this by the mu-divisor (240), obtaining the result.

Answer: *a* mu and *b* bu.
"""

# 圓田周七十八步
周 = 78

# 徑二十六步
徑 = 26

# 先列周七十八步半之，得三十九步
半周 = Fraction(周, 2)

# 又列徑二十六步半之，得一十三步
半徑 = Fraction(徑, 2)

# 二位相乘，得五百七步
積步 = 半周 * 半徑

# 以畝法除之
畝法 = 240
畝數 = 積步 // 畝法  # 整數部分為畝數
餘步 = 積步 % 畝法   # 餘數為剩餘步數

a = 畝數
b = 餘步#----- content ends here -----

"""
"""
