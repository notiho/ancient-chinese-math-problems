"""
今有北鄉算八千七百五十八，西鄉算七千二百三十六，南鄉算八千三百五十六，凡三鄉，發傜三百七十八人。欲以算數多少衰出之，問︰各幾何？
術曰：各置算數為列衰，副并為法，以所發傜人數乘未并者，各自為實，實如法得一人。
荅曰：北鄉遣 a人 。西鄉遣 b人 。南鄉遣 c人 。
"""

#----- content starts here -----
"""
Suppose there are three regions: Beixiang (North Region), Xixiang (West Region), and Nanxiang (South Region). 
The population counts are as follows:
- Beixiang: 8758
- Xixiang: 7236
- Nanxiang: 8356
In total, 378 people are to be conscripted for labor. 

Question: How many people should each region contribute, proportional to their population?

The procedure says: Place the population counts in a sequence as the weights. 
Add them together to form the divisor. 
Multiply the total number of conscripted people by the individual population counts (not yet summed), forming the dividends. 
Divide each dividend by the divisor to obtain the number of conscripted people for each region.

Answer: Beixiang sends *a* people, Xixiang sends *b* people, and Nanxiang sends *c* people.
"""

from fractions import Fraction

# Population counts for each region
北鄉 = 8758
西鄉 = 7236
南鄉 = 8356

# Total conscripted people
發傜 = 378

# Add all population counts to form the divisor (法)
法 = 北鄉 + 西鄉 + 南鄉

# Calculate the number of conscripted people for each region
a = Fraction(發傜 * 北鄉, 法)
b = Fraction(發傜 * 西鄉, 法)
c = Fraction(發傜 * 南鄉, 法)

# Results
a, b, c  # These are the number of people each region sends.#----- content ends here -----

"""
"""
