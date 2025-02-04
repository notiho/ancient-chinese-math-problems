"""
今有絲一千五百二十五斤毎兩一百七十文問錢幾何
術曰先置絲數以二八因之以兩價乗之即得
答曰 a貫
"""

#----- content starts here -----
"""
Suppose there are 1525 jin of silk, and each liang costs 170 wen.
Question: how much money is it in total?

The procedure says: First, place the amount of silk. Multiply it by 28 (since 1 jin = 16 liang, and 1 liang = 1/16 jin, so 1 jin = 16 liang, and 16 * 10 = 160 liang per jin). Then multiply it by the price per liang. This gives the total amount in wen.

Answer: *a* guan (1 guan = 1000 wen).
"""

# 絲一千五百二十五斤
絲數 = 1525

# 每兩一百七十文
每兩價 = 170

# 以二八因之 (1斤 = 16兩, 16兩 * 10 = 160兩 per jin)
絲數兩 = 16 * 1525

#----- content ends here -----

"""
Missing variable in output: 'a'"""
