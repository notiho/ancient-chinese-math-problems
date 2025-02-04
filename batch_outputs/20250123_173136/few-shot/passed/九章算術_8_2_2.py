"""
今有上禾二秉，中禾三秉，下禾四秉，實皆不滿斗。上取中，中取下，下取上各一秉而實滿斗。問︰上、中、下禾實一秉各幾何？
術曰：如方程，各置所取，以正負術入之。正負術曰：同名相除，異名相益，正無入負之，負無入正之。其異名相除，同名相益，正無入正之，負無入負之。
方程術曰，置上禾三秉，中禾二秉，下禾一秉，實三十九斗，於右方。中、左禾列如右方。以右行上禾遍乘中行而以直除。又乘其次，亦以直除。然以中行中禾不盡者遍乘左行而以直除。左方下禾不盡者，上為法，下為實。實即下禾之實。求中禾，以法乘中行下實，而除下禾之實。餘如中禾秉數而一，即中禾之實。求上禾亦以法乘右行下實，而除下禾、中禾之實。餘如上禾秉數而一，即上禾之實。實皆如法，各得一斗。
荅曰：上禾一秉實 a斗 ，中禾一秉實 b斗 ，下禾一秉實 c斗 。
"""

"""
This problem involves solving a system of linear equations using ancient Chinese mathematical methods, specifically the "正負術" (positive and negative method) and "方程術" (method of simultaneous equations). Below is the Python implementation of the procedure:


"""


from fractions import Fraction

# 上禾二秉，中禾三秉，下禾四秉
上禾秉數 = 2
中禾秉數 = 3
下禾秉數 = 4

# 實皆不滿斗，上取中，中取下，下取上各一秉而實滿斗
# Translate the problem into equations:
# Let 上禾 = a, 中禾 = b, 下禾 = c (the actual amount of grain per秉)
# 2a + b = 1 (上禾 takes 1秉 of中禾 to fill 1斗)
# 3b + c = 1 (中禾 takes 1秉 of下禾 to fill 1斗)
# 4c + a = 1 (下禾 takes 1秉 of上禾 to fill 1斗)

# Coefficients of the equations
# Equation 1: 2a + b = 1
# Equation 2: 3b + c = 1
# Equation 3: 4c + a = 1

# Step 1: Solve for c in terms of b from Equation 2
# c = 1 - 3b
c = lambda b: 1 - 3 * b

# Step 2: Solve for a in terms of c from Equation 3
# a = 1 - 4c
a = lambda c: 1 - 4 * c

# Step 3: Substitute c = 1 - 3b into a = 1 - 4c
# a = 1 - 4(1 - 3b)
# a = 1 - 4 + 12b
# a = -3 + 12b

a_in_terms_of_b = lambda b: -3 + 12 * b

# Step 4: Substitute a = -3 + 12b into Equation 1
# 2(-3 + 12b) + b = 1
# -6 + 24b + b = 1
# 25b = 7
# b = 7 / 25
b_value = Fraction(7, 25)

# Step 5: Solve for c using c = 1 - 3b
c_value = c(b_value)

# Step 6: Solve for a using a = -3 + 12b
a_value = a_in_terms_of_b(b_value)

# Final results
a = a_value  # 上禾一秉實
b = b_value  # 中禾一秉實
c = c_value  # 下禾一秉實

# Output the results
a, b, c


"""


### Explanation of the Code:
1. The problem is translated into three linear equations based on the relationships between the秉 (bundles) and斗 (volume).
2. The equations are solved step by step using substitution, following the ancient Chinese method described in the problem.
3. The `Fraction` class is used to ensure exact arithmetic, as the results involve fractions.

### Answer:
The results are:
- 上禾一秉實 `a` 斗
- 中禾一秉實 `b` 斗
- 下禾一秉實 `c` 斗
"""


"""
"""
