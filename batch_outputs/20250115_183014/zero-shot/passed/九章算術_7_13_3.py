"""
今有大器五、小器一容三斛；大器一、小器五容二斛。問︰大、小器各容幾何？
術曰：假令大器五斗，小器亦五斗，盈一十斗。令之大器五斗五升，小器二斗五升，不足二斗。
盈不足術曰：置所出率，盈、不足各居其下。令維乘所出率，并以為實。并盈、不足為法。實如法而一。有分者，通之。盈不足相與同其買物者，置所出率，以少減多，餘，以約法、實。實為物價，法為人數。荅曰：大器容 a斛 ，小器容 b斛 。
"""

"""
To solve this problem, we will translate the ancient Chinese math problem into Python code. We will use the `Fraction` class to handle fractions and compute the values of `a` (capacity of the large vessel) and `b` (capacity of the small vessel). Here's the Python code:


"""


from fractions import Fraction

# Given equations:
# 1. 5a + b = 3
# 2. a + 5b = 2

# Solve for a and b using substitution or elimination:
# Multiply the first equation by 5 to align coefficients of b:
# 25a + 5b = 15
# Subtract the second equation (a + 5b = 2) from the above:
# (25a + 5b) - (a + 5b) = 15 - 2
# 24a = 13
a = Fraction(13, 24)

# Substitute a into the first equation to solve for b:
# 5a + b = 3
# b = 3 - 5a
b = 3 - 5 * a

# The solutions are:
# a = 13/24 (capacity of the large vessel in hu)
# b = 47/24 (capacity of the small vessel in hu)

# Results:
a  # Capacity of the large vessel in hu
b  # Capacity of the small vessel in hu


"""


### Explanation:
1. The problem gives two equations:
   - \( 5a + b = 3 \) (five large vessels and one small vessel hold 3 hu)
   - \( a + 5b = 2 \) (one large vessel and five small vessels hold 2 hu)
   
2. We solve these equations using substitution or elimination. By aligning coefficients and eliminating \( b \), we find \( a \). Substituting \( a \) back into one of the original equations gives \( b \).

3. The final capacities are:
   - \( a = \frac{13}{24} \) hu (large vessel)
   - \( b = \frac{47}{24} \) hu (small vessel)
"""


"""
"""
