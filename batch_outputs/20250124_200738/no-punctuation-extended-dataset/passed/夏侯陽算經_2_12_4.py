"""
今有酒五百六十五斛八斗三升欲給兵毎人三升問給幾何
術曰置酒數再上十之為升以三除之得兵數
答曰給兵 a人
"""

#----- content starts here -----
"""
Suppose there are 565 hu, 8 dou, and 3 sheng of wine. It is desired to distribute it to soldiers, with each soldier receiving 3 sheng.
Question: how many soldiers can be supplied?

The procedure says: Place the amount of wine, convert it to sheng by multiplying by 10 twice.
Divide it by 3, obtaining the number of soldiers.

Answer: it supplies *a* soldiers.
"""

# 酒五百六十五斛八斗三升
斛 = 565
斗 = 8
升 = 3

# 1 斛 = 10 斗, 1 斗 = 10 升
酒數升 = (斛 * 10 * 10) + (斗 * 10) + 升

# 每人三升
每人升 = 3

# 以三除之，得兵數
a = 酒數升 // 每人升  # 整數除法 to get the number of soldiers#----- content ends here -----

"""
"""
