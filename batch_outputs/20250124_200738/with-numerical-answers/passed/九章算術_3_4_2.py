"""
今有北鄉算八千七百五十八，西鄉算七千二百三十六，南鄉算八千三百五十六，凡三鄉，發傜三百七十八人。欲以算數多少衰出之，問︰各幾何？
術曰：各置算數為列衰，副并為法，以所發傜人數乘未并者，各自為實，實如法得一人。
荅曰：北鄉遣 a(=1655262/12175)人 。西鄉遣 b(=1367604/12175)人 。南鄉遣 c(=1579284/12175)人 。
"""

#----- content starts here -----
"""
Suppose there are three regions: Beixiang (Northern Region) with 8758 counts, Xixiang (Western Region) with 7236 counts, and Nanxiang (Southern Region) with 8356 counts. 
In total, 378 people are to be conscripted. 
It is desired to distribute the conscription proportionally based on the counts of each region.
Question: how many people are conscripted from each region?

The procedure says: Place the counts of each region in a line as the decreasing sequence. 
Add them together to get the divisor. 
Multiply the total number of conscripted people by the individual counts (not yet summed), making each its own dividend. 
Divide the dividend by the divisor to get the number of conscripted people for each region.

Answer: Beixiang sends *a*(=1655262/12175) people, Xixiang sends *b*(=1367604/12175) people, and Nanxiang sends *c*(=1579284/12175) people.
"""

# 北鄉算數
北鄉 = 8758

# 西鄉算數
西鄉 = 7236

# 南鄉算數
南鄉 = 8356

# 發傜人數
發傜 = 378

# 副并為法
法 = 北鄉 + 西鄉 + 南鄉

# 以所發傜人數乘未并者，各自為實
北鄉實 = 發傜 * 北鄉
西鄉實 = 發傜 * 西鄉
南鄉實 = 發傜 * 南鄉

# 實如法得一人
a = Fraction(北鄉實, 法)  # 1655262/12175
b = Fraction(西鄉實, 法)  # 1367604/12175
c = Fraction(南鄉實, 法)  # 1579284/12175#----- content ends here -----

"""
"""
