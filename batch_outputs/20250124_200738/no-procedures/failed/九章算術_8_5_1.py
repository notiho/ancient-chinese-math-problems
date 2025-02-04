"""
今有上禾三秉，益實六斗，當下禾十秉。下禾五秉，益實一斗，當上禾二秉。問︰上、下禾實一秉各幾何？
荅曰：上禾一秉實 a斗 ，下禾一秉實 b斗 。
"""

#----- content starts here -----
"""
Suppose there are two types of grain: "upper grain" (上禾) and "lower grain" (下禾).
- 3 bundles of upper grain plus 6 dou of grain are equivalent to 10 bundles of lower grain.
- 5 bundles of lower grain plus 1 dou of grain are equivalent to 2 bundles of upper grain.

Question: How much grain does one bundle of upper grain (上禾) and one bundle of lower grain (下禾) yield?

Answer: One bundle of upper grain yields *a* dou, and one bundle of lower grain yields *b* dou.
"""

from fractions import Fraction

# Let 上禾一秉 yield `a` dou, and 下禾一秉 yield `b` dou.
# From the problem:
# 3a + 6 = 10b  (Equation 1)
# 5b + 1 = 2a   (Equation 2)

# Solve for `a` and `b` using substitution.

# From Equation 2: 2a = 5b + 1 => a = (5b + 1) / 2
a = Fraction(5, 2) * b + Fraction(1, 2)

# Substitute `a` into Equation 1:
# 3((5b + 1) / 2) + 6 = 10b
# Multiply through by 2 to eliminate the fraction:
# 3(5b + 1) + 12 = 20b
# 15b + 3 + 12 = 20b
# 15b + 15 = 20b
# 15 = 5b
# b = 3

b = Fraction(15, 5)

# Substitute `b` back into the expression for `a`:
# a = (5b + 1) / 2
# a = (5(3) + 1) / 2
# a = (15 + 1) / 2
# a = 8

a = Fraction(16, 2)

# Final results:
# 上禾一秉 yields `a` dou.
# 下禾一秉 yields `b` dou.

print(f"上禾一秉實 {a} 斗")
print(f"下禾一秉實 {b} 斗")#----- content ends here -----

"""
Code error: name 'b' is not defined"""
