"""
今有北鄉算八千七百五十八，西鄉算七千二百三十六，南鄉算八千三百五十六，凡三鄉，發傜三百七十八人。欲以算數多少衰出之，問︰各幾何？
荅曰：北鄉遣 a人 。西鄉遣 b人 。南鄉遣 c人 。
"""

#----- content starts here -----
"""
Suppose there are three villages: Beixiang (North Village), Xixiang (West Village), and Nanxiang (South Village). 
The population counts are as follows:
- Beixiang: 8758
- Xixiang: 7236
- Nanxiang: 8356

A total of 378 people are to be conscripted (labor tax). The conscription is to be distributed proportionally based on the population of each village.

Question: How many people should each village send?

Answer:
- Beixiang sends *a* people.
- Xixiang sends *b* people.
- Nanxiang sends *c* people.
"""

# Population counts
北鄉 = 8758
西鄉 = 7236
南鄉 = 8356

# Total population
總人口 = 北鄉 + 西鄉 + 南鄉

# Total conscription
發傜 = 378

# Calculate proportional conscription for each village
a = Fraction(發傜 * 北鄉, 總人口)
b = Fraction(發傜 * 西鄉, 總人口)
c = Fraction(發傜 * 南鄉, 總人口)

# Results
a, b, c#----- content ends here -----

"""
"""
