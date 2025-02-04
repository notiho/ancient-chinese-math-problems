"""
今有北鄉算八千七百五十八，西鄉算七千二百三十六，南鄉算八千三百五十六，凡三鄉，發傜三百七十八人。欲以算數多少衰出之，問︰各幾何？
術曰：各置算數為列衰，副并為法，以所發傜人數乘未并者，各自為實，實如法得一人。
荅曰：北鄉遣 a(=1655262/12175)人 。西鄉遣 b(=1367604/12175)人 。南鄉遣 c(=1579284/12175)人 。
"""

#----- content starts here -----
"""
Suppose there are three regions: the northern region has 8758 suan, the western region has 7236 suan, and the southern region has 8356 suan. 
In total, there are 3 regions, and 378 people need to be conscripted. 
It is desired to distribute the conscription proportionally based on the suan numbers of each region.
Question: how many people are conscripted from each region?

The procedure says: Place the suan numbers of each region in a line as the decreasing sequence.
Add them together to obtain the divisor.
Multiply the total number of conscripted people by the suan numbers that have not been added together, obtaining the dividend for each region.
Divide the dividend by the divisor to obtain the number of conscripted people for each region.

Answer: The northern region sends *a*(=1655262/12175) people, the western region sends *b*(=1367604/12175) people, and the southern region sends *c*(=1579284/12175) people.
"""

# 北鄉算八千七百五十八
北鄉算 = 8758

# 西鄉算七千二百三十六
西鄉算 = 7236

# 南鄉算八千三百五十六
南鄉算 = 8356

# 發傜三百七十八人
發傜人數 = 378

# 各置算數為列衰
算數 = [北鄉算, 西鄉算, 南鄉算]

# 副并為法
法 = sum(算數)

# 以所發傜人數乘未并者，各自為實
實_北鄉 = 發傜人數 * 北鄉算
實_西鄉 = 發傜人數 * 西鄉算
實_南鄉 = 發傜人數 * 南鄉算

# 實如法得一人
a = Fraction(實_北鄉, 法)  # 1655262/12175
b = Fraction(實_西鄉, 法)  # 1367604/12175
c = Fraction(實_南鄉, 法)  # 1579284/12175#----- content ends here -----

"""
"""
