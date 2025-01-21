"""
今有北鄉算八千七百五十八，西鄉算七千二百三十六，南鄉算八千三百五十六，凡三鄉，發傜三百七十八人。欲以算數多少衰出之，問︰各幾何？
術曰：各置算數為列衰，副并為法，以所發傜人數乘未并者，各自為實，實如法得一人。
荅曰：北鄉遣 a人 。西鄉遣 b人 。南鄉遣 c人 。
"""

"""
To solve this problem, we will translate the ancient Chinese math problem into Python code. The problem involves distributing 378 people among three regions (North, West, and South) in proportion to their respective populations. The populations are given as follows:

- North (北鄉): 8758
- West (西鄉): 7236
- South (南鄉): 8356

The solution involves proportional distribution based on the populations. Here's the Python code:


"""


from fractions import Fraction

# Given data
north_population = 8758
west_population = 7236
south_population = 8356
total_people = 378

# Total population
total_population = north_population + west_population + south_population

# Proportional distribution
a = Fraction(north_population * total_people, total_population)  # People sent from North
b = Fraction(west_population * total_people, total_population)   # People sent from West
c = Fraction(south_population * total_people, total_population)  # People sent from South

# Results
a, b, c


"""


### Explanation:
1. The total population is calculated by summing the populations of the three regions.
2. The number of people sent from each region is proportional to its population relative to the total population.
3. The `Fraction` class is used to ensure accurate calculations, even if the results are not integers.

### Output:
The variables `a`, `b`, and `c` will contain the number of people sent from the North, West, and South regions, respectively, as fractions.
"""


"""
"""
