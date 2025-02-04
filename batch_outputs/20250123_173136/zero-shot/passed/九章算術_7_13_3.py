"""
今有大器五、小器一容三斛；大器一、小器五容二斛。問︰大、小器各容幾何？
術曰：假令大器五斗，小器亦五斗，盈一十斗。令之大器五斗五升，小器二斗五升，不足二斗。
盈不足術曰：置所出率，盈、不足各居其下。令維乘所出率，并以為實。并盈、不足為法。實如法而一。有分者，通之。盈不足相與同其買物者，置所出率，以少減多，餘，以約法、實。實為物價，法為人數。
荅曰：大器容 a斛 ，小器容 b斛 。
"""

"""
To solve this problem, we will translate the ancient Chinese mathematical method into Python code. The problem involves determining the capacities of a large container (`a`) and a small container (`b`) in units of "斛" (a traditional Chinese unit of volume).

Here is the Python code:


"""


from fractions import Fraction

# Given equations:
# 1. 5a + b = 3
# 2. a + 5b = 2

# Solve for a and b using substitution or elimination:
# Multiply the first equation by 5 to align the coefficients of b:
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
# a = 13/24 斛
# b = 47/24 斛


"""


### Explanation of the solution:
1. The problem provides two linear equations:
   - \( 5a + b = 3 \)
   - \( a + 5b = 2 \)
2. We solve these equations using the elimination method:
   - Multiply the first equation by 5 to align the coefficients of \( b \).
   - Subtract the second equation from the modified first equation to eliminate \( b \) and solve for \( a \).
3. Substitute the value of \( a \) back into one of the original equations to solve for \( b \).
4. The solutions are expressed as fractions using the `Fraction` class.

### Final Values:
- \( a = \frac{13}{24} \) 斛 (capacity of the large container)
- \( b = \frac{47}{24} \) 斛 (capacity of the small container)
"""


"""
"""
