"""
今有北鄉算八千七百五十八，西鄉算七千二百三十六，南鄉算八千三百五十六，凡三鄉，發傜三百七十八人。欲以算數多少衰出之，問︰各幾何？
術曰：各置算數為列衰，副并為法，以所發傜人數乘未并者，各自為實，實如法得一人。
荅曰：北鄉遣 a人 。西鄉遣 b人 。南鄉遣 c人 。
"""

"""
To solve this problem, we need to distribute the total number of people (378) among the three regions (北鄉, 西鄉, 南鄉) in proportion to their respective population counts (算數). Here's the Python code to compute the values of `a`, `b`, and `c`:


"""


from fractions import Fraction

# Population counts for each region
北鄉 = 8758
西鄉 = 7236
南鄉 = 8356

# Total number of people to distribute
total_people = 378

# Total population of all three regions
total_population = 北鄉 + 西鄉 + 南鄉

# Calculate the number of people assigned to each region
a = Fraction(北鄉 * total_people, total_population)
b = Fraction(西鄉 * total_people, total_population)
c = Fraction(南鄉 * total_people, total_population)

# Results
a, b, c


"""


This code calculates the number of people (`a`, `b`, `c`) assigned to 北鄉, 西鄉, and 南鄉, respectively, in proportion to their population counts. The results are represented as fractions.
"""


"""
"""
