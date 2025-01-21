"""
今有北鄉算八千七百五十八，西鄉算七千二百三十六，南鄉算八千三百五十六，凡三鄉，發傜三百七十八人。欲以算數多少衰出之，問︰各幾何？
術曰：各置算數為列衰，副并為法，以所發傜人數乘未并者，各自為實，實如法得一人。
荅曰：北鄉遣 a(=1655262/12175)人 。西鄉遣 b(=1367604/12175)人 。南鄉遣 c(=1579284/12175)人 。
"""

"""
Suppose there are three regions: Beixiang (Northern Region) has 8758 suan, Xixiang (Western Region) has 7236 suan, and Nanxiang (Southern Region) has 8356 suan. 
In total, 378 people are to be conscripted. 
It is desired to distribute the conscription based on the proportion of suan in each region. 
Question: how many people should each region provide?

The procedure says: Place the suan numbers for each region in a sequence as the decreasing weights. 
Add them together to obtain the divisor. 
Multiply the total number of conscripted people by the suan numbers (not yet summed) for each region, making them the dividends. 
Divide each dividend by the divisor to obtain the number of people for each region.

Answer: Beixiang sends *a*(=1655262/12175) people, Xixiang sends *b*(=1367604/12175) people, and Nanxiang sends *c*(=1579284/12175) people.
"""

# 北鄉算
北鄉算 = 8758

# 西鄉算
西鄉算 = 7236

# 南鄉算
南鄉算 = 8356

# 發傜三百七十八人
發傜 = 378

# 各置算數為列衰
算數 = [北鄉算, 西鄉算, 南鄉算]

# 副并為法
法 = sum(算數)

# 以所發傜人數乘未并者，各自為實
實 = [發傜 * suan for suan in 算數]

# 實如法得一人
a, b, c = [Fraction(實[i], 法) for i in range(len(實))] # 1655262/12175, 1367604/12175, 1579284/12175
"""
"""
