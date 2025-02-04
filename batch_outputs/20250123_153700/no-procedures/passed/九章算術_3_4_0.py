"""
今有北鄉算八千七百五十八，西鄉算七千二百三十六，南鄉算八千三百五十六，凡三鄉，發傜三百七十八人。欲以算數多少衰出之，問︰各幾何？
荅曰：北鄉遣 a人 。西鄉遣 b人 。南鄉遣 c人 。
"""

"""
Suppose there are three regions: Beixiang (North Region), Xixiang (West Region), and Nanxiang (South Region), with populations of 8758, 7236, and 8356 respectively. 
In total, 378 people are to be conscripted for labor. 
The conscription is to be distributed proportionally to the population of each region.

Question: how many people are conscripted from each region?

Answer: Beixiang sends *a* people, Xixiang sends *b* people, and Nanxiang sends *c* people.
"""

# 北鄉算
北鄉 = 8758

# 西鄉算
西鄉 = 7236

# 南鄉算
南鄉 = 8356

# 總算數
總算數 = 北鄉 + 西鄉 + 南鄉

# 總傜數
總傜數 = 378

# 各鄉分配傜數
a = Fraction(北鄉 * 總傜數, 總算數)
b = Fraction(西鄉 * 總傜數, 總算數)
c = Fraction(南鄉 * 總傜數, 總算數)

# Results
a, b, c
"""
"""
