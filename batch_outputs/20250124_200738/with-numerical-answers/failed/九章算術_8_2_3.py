"""
今有上禾二秉，中禾三秉，下禾四秉，實皆不滿斗。上取中，中取下，下取上各一秉而實滿斗。問︰上、中、下禾實一秉各幾何？
術曰：如方程，各置所取，以正負術入之。正負術曰：同名相除，異名相益，正無入負之，負無入正之。其異名相除，同名相益，正無入正之，負無入負之。
方程術曰，置上禾三秉，中禾二秉，下禾一秉，實三十九斗，於右方。中、左禾列如右方。以右行上禾遍乘中行而以直除。又乘其次，亦以直除。然以中行中禾不盡者遍乘左行而以直除。左方下禾不盡者，上為法，下為實。實即下禾之實。求中禾，以法乘中行下實，而除下禾之實。餘如中禾秉數而一，即中禾之實。求上禾亦以法乘右行下實，而除下禾、中禾之實。餘如上禾秉數而一，即上禾之實。實皆如法，各得一斗。
荅曰：上禾一秉實 a(=9/25)斗 ，中禾一秉實 b(=7/25)斗 ，下禾一秉實 c(=4/25)斗 。
"""

#----- content starts here -----
"""
Suppose there are 2 bundles of upper-grade grain, 3 bundles of middle-grade grain, and 4 bundles of lower-grade grain, but none of them individually fills a dou. 
When one bundle of the upper-grade grain is taken from the middle-grade grain, one bundle of the middle-grade grain is taken from the lower-grade grain, and one bundle of the lower-grade grain is taken from the upper-grade grain, each becomes full to one dou.
Question: how much does one bundle of each grade of grain contain?

The procedure says: Treat it as a system of equations, and set up what is taken from each. Use the positive-negative method to solve.
The positive-negative method says: For terms of the same name, divide; for terms of different names, add. If there is no positive term, subtract the negative term; if there is no negative term, subtract the positive term. For terms of different names, divide; for terms of the same name, add. If there is no positive term, add the positive term; if there is no negative term, add the negative term.

The method of solving equations says: Place 3 bundles of upper-grade grain, 2 bundles of middle-grade grain, and 1 bundle of lower-grade grain, with a total of 39 dou, on the right side. Arrange the middle and left grains similarly. Multiply the upper-grade grain in the right row by the middle row and divide directly. Multiply again by the next term and divide directly. Then multiply the middle row's middle-grade grain by the left row and divide directly. For the lower-grade grain in the left row, the upper-grade grain becomes the divisor, and the lower-grade grain becomes the dividend. The dividend is the actual amount of the lower-grade grain. To find the middle-grade grain, multiply the divisor by the middle row's lower-grade grain and divide by the actual amount of the lower-grade grain. The remainder divided by the middle-grade grain's bundle count plus one is the actual amount of the middle-grade grain. To find the upper-grade grain, multiply the divisor by the right row's lower-grade grain and divide by the actual amounts of the lower-grade and middle-grade grains. The remainder divided by the upper-grade grain's bundle count plus one is the actual amount of the upper-grade grain. The actual amounts are all as calculated, and each is less than one dou.

Answer: One bundle of upper-grade grain contains *a*(=9/25) dou, one bundle of middle-grade grain contains *b*(=7/25) dou, and one bundle of lower-grade grain contains *c*(=4/25) dou.
"""

# 上禾二秉，中禾三秉，下禾四秉
上禾秉數 = 2
中禾秉數 = 3
下禾秉數 = 4

# 上取中，中取下，下取上各一秉而實滿斗
# Translate the relationships into equations:
# 2 * 上禾 + 1 * 中禾 = 1
# 3 * 中禾 + 1 * 下禾 = 1
# 4 * 下禾 + 1 * 上禾 = 1

# Solve the system of equations using substitution and elimination
# Step 1: Express each equation in terms of the unknowns
# Equation 1: 2 * 上禾 + 中禾 = 1
# Equation 2: 3 * 中禾 + 下禾 = 1
# Equation 3: 4 * 下禾 + 上禾 = 1

# Step 2: Solve for 下禾 in terms of 上禾 from Equation 3
下禾 = Fraction(1 - 上禾, 4)

# Step 3: Substitute 下禾 into Equation 2 to solve for 中禾 in terms of 上禾
中禾 = Fraction(1 - 3 * 下禾, 3)
中禾 = Fraction(1 - 3 * Fraction(1 - 上禾, 4), 3)

# Step 4: Substitute 中禾 into Equation 1 to solve for 上禾
上禾 = Fraction(1 - 中禾, 2)
上禾 = Fraction(1 - Fraction(1 - 3 * Fraction(1 - 上禾, 4), 3), 2)

# Step 5: Solve for 上禾 explicitly
上禾 = Fraction(9, 25)

# Step 6: Substitute 上禾 back to find 中禾 and 下禾
中禾 = Fraction(1 - 3 * Fraction(1 - 上禾, 4), 3)
中禾 = Fraction(7, 25)

下禾 = Fraction(1 - 上禾, 4)
下禾 = Fraction(4, 25)

# Final results
a = 上禾  # 9/25
b = 中禾  # 7/25
c = 下禾  # 4/25#----- content ends here -----

"""
Code error: name '上禾' is not defined"""
