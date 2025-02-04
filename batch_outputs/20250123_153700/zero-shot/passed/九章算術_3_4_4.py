"""
今有北鄉算八千七百五十八，西鄉算七千二百三十六，南鄉算八千三百五十六，凡三鄉，發傜三百七十八人。欲以算數多少衰出之，問︰各幾何？
術曰：各置算數為列衰，副并為法，以所發傜人數乘未并者，各自為實，實如法得一人。
荅曰：北鄉遣 a人 。西鄉遣 b人 。南鄉遣 c人 。
"""

"""
To solve this problem, we need to distribute the total number of people (378) among the three regions (北鄉, 西鄉, 南鄉) in proportion to their respective population counts. The populations are given as follows:

- 北鄉: 8758
- 西鄉: 7236
- 南鄉: 8356

The solution involves proportional distribution. Here's the Python code to compute the values of `a`, `b`, and `c`:


"""


from fractions import Fraction

# Population counts
north_population = 8758
west_population = 7236
south_population = 8356

# Total population
total_population = north_population + west_population + south_population

# Total number of people to distribute
total_people = 378

# Proportional distribution
a = Fraction(north_population * total_people, total_population)  # 北鄉
b = Fraction(west_population * total_people, total_population)   # 西鄉
c = Fraction(south_population * total_people, total_population)  # 南鄉

# Results
a, b, c


"""


This code calculates the number of people (`a`, `b`, `c`) to be sent from each region in proportion to their population sizes. The results are stored as fractions for precise representation.
"""


"""
"""
