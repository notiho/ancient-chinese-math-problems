"""
今有北鄉算八千七百五十八，西鄉算七千二百三十六，南鄉算八千三百五十六，凡三鄉，發傜三百七十八人。欲以算數多少衰出之，問︰各幾何？
術曰：各置算數為列衰，副并為法，以所發傜人數乘未并者，各自為實，實如法得一人。
荅曰：北鄉遣 a(=1655262/12175)人 。西鄉遣 b(=1367604/12175)人 。南鄉遣 c(=1579284/12175)人 。
"""

#----- content starts here -----
"""
Suppose there are three regions: Beixiang (North Region) with 8758 counts, Xixiang (West Region) with 7236 counts, and Nanxiang (South Region) with 8356 counts. 
In total, 378 people are to be conscripted. 
It is desired to distribute the conscription proportionally according to the counts of each region. 
Question: how many people are conscripted from each region?

The procedure says: Place the counts of each region in a line as the decreasing sequence. 
Add them together to obtain the divisor. 
Multiply the number of conscripted people by the unadded counts of each region, making each its own dividend. 
Divide the dividend by the divisor to obtain the number of conscripted people for each region.

Answer: Beixiang sends *a*(=1655262/12175) people, Xixiang sends *b*(=1367604/12175) people, Nanxiang sends *c*(=1579284/12175) people.
"""

# 北鄉算八千七百五十八
北鄉 = 8758

# 西鄉算七千二百三十六
西鄉 = 7236

# 南鄉算八千三百五十六
南鄉 = 8356

# 發傜三百七十八人
發傜 = 378

# 各置算數為列衰
算數 = [北鄉, 西鄉, 南鄉]

# 副并為法
法 = sum(算數)

# 以所發傜人數乘未并者，各自為實
實 = [發傜 * i for i in 算數]

# 實如法得一人
a, b, c = [Fraction(i, 法) for i in 實]  # 1655262/12175, 1367604/12175, 1579284/12175#----- content ends here -----

"""
"""
