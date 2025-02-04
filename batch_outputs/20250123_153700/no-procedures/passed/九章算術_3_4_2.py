"""
今有北鄉算八千七百五十八，西鄉算七千二百三十六，南鄉算八千三百五十六，凡三鄉，發傜三百七十八人。欲以算數多少衰出之，問︰各幾何？
荅曰：北鄉遣 a人 。西鄉遣 b人 。南鄉遣 c人 。
"""

"""
Suppose there are three regions: Beixiang (North Region), Xixiang (West Region), and Nanxiang (South Region). 
The population counts (算) for these regions are as follows:
- Beixiang: 8758
- Xixiang: 7236
- Nanxiang: 8356

A total of 378 people are to be conscripted (發傜) from these three regions, distributed proportionally to their population counts.
Question: how many people are conscripted from each region?

Answer: Beixiang sends *a* people, Xixiang sends *b* people, and Nanxiang sends *c* people.
"""

# Population counts for each region
北鄉 = 8758
西鄉 = 7236
南鄉 = 8356

# Total population
總人口 = 北鄉 + 西鄉 + 南鄉

# Total conscription
總傜 = 378

# Calculate conscription for each region proportionally
a = Fraction(北鄉 * 總傜, 總人口)
b = Fraction(西鄉 * 總傜, 總人口)
c = Fraction(南鄉 * 總傜, 總人口)

# Results
a, b, c
"""
"""
