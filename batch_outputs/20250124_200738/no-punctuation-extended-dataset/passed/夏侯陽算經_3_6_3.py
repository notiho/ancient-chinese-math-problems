"""
今有下戸欠錢一百二十三貫五百文準條扵上戸均攤今有上戸見在錢三萬一千二百五十貫文問合毎貫均著幾何
術曰置下戸錢數以上戸見在錢除之即得
答曰毎貫 a文
"""

#----- content starts here -----
"""
Suppose there is a lower household owing 123 guan and 500 wen. According to the rules, this debt is to be evenly distributed among the upper households.
Now, the upper households collectively have 31,250 guan of money.
Question: how much debt does each guan of the upper households bear?

The procedure says: Place the amount of money owed by the lower household and divide it by the amount of money present in the upper households. This gives the result.

Answer: each guan bears *a* wen.
"""

# 下戸欠錢一百二十三貫五百文
下戸錢數 = 123 * 1000 + 500  # Convert to wen (1 guan = 1000 wen)

# 上戸見在錢三萬一千二百五十貫
上戸見在錢 = 31250  # In guan

# 置下戸錢數以上戸見在錢除之
a = Fraction(下戸錢數, 上戸見在錢)  # Result in wen per guan#----- content ends here -----

"""
"""
