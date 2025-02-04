"""
今有絲一千五百二十五斤毎兩一百七十文問錢幾何
術曰先置絲數以二八因之以兩價乗之即得
答曰 a貫
"""

#----- content starts here -----
"""
Suppose there are 1525 jin of silk, with each liang costing 170 wen.
Question: how much money (in guan) is it worth?

The procedure says: First, place the amount of silk. Multiply it by 28 (since 1 jin = 16 liang, and 1 jin = 16 * 10 = 160 liang, which is equivalent to 28 in this context). 
Then multiply it by the price per liang. The result is obtained.

Answer: *a* guan.
"""

# 絲一千五百二十五斤
絲數 = 1525

# 每兩一百七十文
每兩價 = 170

# 以二八因之 (1斤 = 16兩, 1兩 = 10文, so 1斤 = 16 * 10 = 160兩, simplified to 28 in the procedure)
因數 = 28

# 以兩價乘之即得
總文數 = 絲數 * 因數 * 每兩價

# Convert to 貫 (1貫 = 1000文)
a = Fraction(總文數, 1000)#----- content ends here -----

"""
Variable 'a' has wrong value. Expected: 4148, Actual: 7259"""
