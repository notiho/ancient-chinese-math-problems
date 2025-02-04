"""
今有酒五百六十五斛八斗三升欲給兵毎人三升問給幾何
術曰置酒數再上十之為升以三除之得兵數
答曰給兵 a人
"""

"""
Suppose there are 565 hu, 8 dou, and 3 sheng of wine. It is desired to distribute it to soldiers, with each soldier receiving 3 sheng.
Question: how many soldiers can be given wine?

The procedure says: Place the amount of wine, convert it to sheng by multiplying by 10 twice.
Divide it by 3, obtaining the number of soldiers.

Answer: *a* soldiers.
"""

# 酒五百六十五斛八斗三升
酒_斛 = 565
酒_斗 = 8
酒_升 = 3

# 置酒數再上十之為升
# 1 斛 = 10 斗, 1 斗 = 10 升
總升 = (酒_斛 * 10 * 10) + (酒_斗 * 10) + 酒_升

# 以三除之，得兵數
a = 總升 // 3  # 整數除法，因為兵數必須是整數
"""
"""
