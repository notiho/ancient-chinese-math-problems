"""
今有大器五、小器一容三斛；大器一、小器五容二斛。問︰大、小器各容幾何？
術曰：假令大器五斗，小器亦五斗，盈一十斗。令之大器五斗五升，小器二斗五升，不足二斗。
盈不足術曰：置所出率，盈、不足各居其下。令維乘所出率，并以為實。并盈、不足為法。實如法而一。有分者，通之。盈不足相與同其買物者，置所出率，以少減多，餘，以約法、實。實為物價，法為人數。荅曰：大器容 a斛 ，小器容 b斛 。
"""

"""
To solve this problem, we will translate the ancient Chinese math problem into Python code. The problem involves two unknowns, the capacity of the large container (`a`) and the capacity of the small container (`b`), both measured in "斛". We will use the `Fraction` class to ensure precise calculations.

Here is the Python code:


"""


from fractions import Fraction

# Given equations:
# 1. 5a + b = 3
# 2. a + 5b = 2

# Solve the system of equations:
# Multiply the first equation by 5 to align the coefficients of b:
# 25a + 5b = 15
# Subtract the second equation from this result:
# (25a + 5b) - (a + 5b) = 15 - 2
# 24a = 13
a = Fraction(13, 24)

# Substitute a into the first equation to solve for b:
# 5a + b = 3
# b = 3 - 5a
b = 3 - 5 * a

# The solutions:
# a is the capacity of the large container in "斛"
# b is the capacity of the small container in "斛"

print("大器容 a =", a, "斛")
print("小器容 b =", b, "斛")


"""


### Explanation of the Code:
1. The problem provides two equations:
   - \( 5a + b = 3 \)
   - \( a + 5b = 2 \)
2. We solve this system of linear equations using substitution and elimination.
3. The solution is expressed using the `Fraction` class to ensure exact results.

### Output:
The capacities of the large and small containers are:
- \( a = \frac{13}{24} \) 斛 (capacity of the large container)
- \( b = \frac{47}{24} \) 斛 (capacity of the small container)
"""


"""
"""
